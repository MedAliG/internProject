<template>
  <div>
    <base-header class="header pb-8 pt-5 pt-lg-8 d-flex align-items-center">
      <!-- Mask -->
      <span class="mask bg-gradient-success opacity-8"></span>
      <!-- Header container -->
      <div class="container-fluid d-flex align-items-center">
        <div class="row">
          <div class="col-lg-7 col-md-10">
            <h1 class="display-2 text-white">Hello {{this.$store.state.user_id}}</h1>
            <p
              class="text-white mt-0 mb-5"
            >The submitted transcribed text should follow the rules of submission !</p>
          </div>
        </div>
      </div>
    </base-header>

    <div class="container-fluid mt--7">
      <base-alert type="danger" v-if="this.error">
        <strong>Submission Error</strong> Please recheck the text you submitted !
      </base-alert>
      <div class="row">
        <div class="col-xl-12 order-xl-1">
          <card shadow type="secondary">
            <div slot="header" class="bg-white border-0">
              <div class="row align-items-center">
                <div class="col-8">
                  <h3 class="mb-0">Segment</h3>
                </div>
                <div class="col-4 text-right">
                  <a href="#!" class="btn btn-sm btn-primary">Settings</a>
                </div>
              </div>
            </div>
            <template>
              <!-- Description -->
              <form action="#" @submit.prevent="submitText">
                <h6 class="heading-small text-muted mb-4">Transcription Test</h6>
                <div class="pl-lg-4">
                  <div class="form-group">
                    <base-input alternative label="Input text">
                      <textarea
                        rows="4"
                        class="form-control form-control-alternative"
                        placeholder="A few words about you ..."
                        v-model="model.text"
                      ></textarea>
                    </base-input>
                  </div>
                </div>
                <div class="row">
                  <div class="col-12">
                    <button href="#!" class="btn btn-sm btn-primary float-right" type="submit">Save</button>
                  </div>
                </div>
                <hr />
              </form>
              <div class="row" style="height:50px">
                <div id="audio" class="col-12">
                  <audio controls class="float-center" v-bind:src="track">
                    <!--<source src="horse.ogg" type="audio/ogg" />-->
                    <source v-bind:src="this.track" type="audio/mp3" />
                  </audio>
                </div>
              </div>
            </template>
          </card>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "segment",
  data() {
    return {
      textData: "",
      id: 0,
      error: false,
      dataTable: null,
      model: {
        text: "",
        segmentId: 0
      },
      track: ""
    };
  },
  created() {
    this.id = this.$route.params.id;
    this.model.segmentId = this.id;
  },
  mounted() {
    axios.defaults.headers.common["Authorization"] =
      "token " + this.$store.state.token;
    axios
      .get("http://127.0.0.1:8000/seg?id=" + this.id)
      .then(response => {
        this.data = response.data;
        this.track = "http://127.0.0.1:8000" + this.data.audio.path;
        this.model.text = response.data.text.text;
        /*console.log(this.data);
        console.log("http://127.0.0.1:8000" + this.data.audio.path);*/
      })
      .catch(error => {
        console.log(error);
        this.errored = true;
      });
  },
  methods: {
    submitText() {
      console.log(this.model.segmentId);
      this.$store
        .dispatch("submitData", {
          text: this.model.text,
          segmentId: this.model.segmentId
        })
        .then(response => {
          this.error = false
          //this.$router.push({ name: "audios" });
        })
        .catch(reason => {
          this.error = true
        });
    }
  }
};
</script>
<style></style>

<!-- http://127.0.0.1:8000/data/{{this.data.audio.path}}-->