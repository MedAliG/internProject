import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'


Vue.use(Vuex)
axios.defaults.baseURL = 'http://127.0.0.1:8000/'

export const store = new Vuex.Store({

    state: {
        token: localStorage.getItem('access_token') || null,
        user_id: localStorage.getItem('user_id') || null,
        username: localStorage.getItem('username') || null,
    },
    getters: {
        tokenGetter(state) {
            return state.token;
        },
        loggedIn(state) {
            return state.token !== null
        },
    },
    mutations: {
        retrieveToken(state, token) {
            state.token = token
            state.user_id = localStorage.getItem('user_id')
            state.username = localStorage.getItem('username')
        },
        destroyToken(state) {
            state.token = null
            state.user_id = null
            state.username = null
        },
    },

    actions: {
        destroyToken(context) {
            if (context.getters.loggedIn) {
                return new Promise(() => {
                    localStorage.removeItem('access_token')
                    localStorage.removeItem('user_id')
                    localStorage.removeItem('username')
                    context.commit('destroyToken')

                })
            }
        },


        retrieveToken(context, credentials) {
            return new Promise((resolve, reject) => {

                axios.post('login', {
                    username: credentials.username,
                    password: credentials.password,
                })
                    .then(response => {

                        const token = response.data.token
                        const user_id = response.data.user_id
                        const username = response.data.username
                        localStorage.setItem('access_token', token)
                        localStorage.setItem('user_id', user_id)
                        localStorage.setItem('username', username)
                        context.commit('retrieveToken', token)
                        //context.commit('user_id',user_id)

                        resolve(response)
                        // console.log(response);
                        // context.commit('addTodo', response.data)
                    })
                    .catch(error => {
                        console.log(error)

                        reject(error)
                    })
            })
        },

        submitData(context, dataSet) {
            axios.defaults.headers.common["Authorization"] =
                "token " + localStorage.getItem('access_token');
            return new Promise((resolve, reject) => {
                axios.post('textData/', {
                    text: dataSet.text,
                    segementId: dataSet.segmentId,
                    userId: localStorage.getItem('user_id'),
                })
                    .then(response => {
                        resolve(response)
                    }).catch(error => {
                        reject(error)
                    })
            })
        }
    }


})