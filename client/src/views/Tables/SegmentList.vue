<template>
  <div class="card shadow" :class="type === 'dark' ? 'bg-default': ''">
    <div class="card-header border-0" :class="type === 'dark' ? 'bg-transparent': ''">
      <div class="row align-items-center">
        <div class="col">
          <h3 class="mb-0" :class="type === 'dark' ? 'text-white': ''">{{title}}</h3>
        </div>
        <div class="col text-right">
          <base-button type="primary" size="sm">See all</base-button>
        </div>
      </div>
    </div>

    <div class="table-responsive">
      <base-table
        class="table align-items-center table-flush"
        :class="type === 'dark' ? 'table-dark': ''"
        :thead-classes="type === 'dark' ? 'thead-dark': 'thead-light'"
        tbody-classes="list"
        :data="tableData"
      >
        <template slot="columns">
          <th>Piece Title</th>
          <th>Budget</th>
          <th>Status</th>
          <th>Users</th>
          <th>Completion</th>
          <th></th>
        </template>

        <template slot-scope="{row}">
          <th scope="row">
            <div class="media align-items-center">
              <a href="#" class="avatar rounded-circle mr-3">
                <img alt="Image placeholder" src="img/theme/audio.png" />
              </a>
              <div class="media-body">
                <span class="name mb-0 text-sm">{{row.title}}</span>
              </div>
            </div>
          </th>
          <td class="budget">{{row.name}}</td>
          <td>
            <badge class="badge-dot mr-4" :type="row.statusType">
              <i :class="`bg-${row.status}`"></i>
              <span class="status">{{row.status}}</span>
            </badge>
          </td>
          <td>
            <div class>
              <a
                href="#"
                class="avatar avatar-sm rounded-circle"
                data-toggle="tooltip"
                data-original-title="Jessica Doe"
              >
                <img alt="Image placeholder" src="img/theme/team-4-800x800.jpg" />
              </a>
            </div>
          </td>

          <td>
            <div class="d-flex align-items-center">
              <span class="completion mr-2">{{row.state}}%</span>
              <div>
                <base-progress
                  :type="row.statusType"
                  :show-percentage="false"
                  class="pt-0"
                  :value="row.completion"
                />
              </div>
            </div>
          </td>

          <td class="text-right">
            <base-dropdown class="dropdown" position="right">
              <a
                slot="title"
                class="btn btn-sm btn-icon-only text-light"
                role="button"
                data-toggle="dropdown"
                aria-haspopup="true"
                aria-expanded="false"
              >
                <i class="fas fa-ellipsis-v"></i>
              </a>

              <template>
                <router-link v-bind:to="`/segment/${row.id}/`" class="dropdown-item">Edit</router-link>
                <a class="dropdown-item" href="#">Delete</a>
              </template>
            </base-dropdown>
          </td>
        </template>
      </base-table>
    </div>

    <div
      class="card-footer d-flex justify-content-end"
      :class="type === 'dark' ? 'bg-transparent': ''"
    >
      <base-pagination total="30"></base-pagination>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: "segment-table",
  props: {
    type: {
      type: String
    },
    title: String
  },
  data() {
    return {
      id: 0,
      tableData: null,
      audioData: null
    };
  },
  created() {
    this.id = this.$route.params.id;
  },
  mounted() {
    axios.defaults.headers.common["Authorization"] =
      "token " + this.$store.state.token;

    axios
      .get("http://127.0.0.1:8000/segment?id=" + this.id)
      .then(response => {
        //console.log(response.data);
        this.tableData = response.data;
      })
      .catch(error => {
        console.log(error);
        this.errored = true;
      });
    axios
      .get("http://127.0.0.1:8000/api/audio/" + this.id)
      .then(response => {
        //console.log(response.data);
        this.audioData = response.data;
        if (
          this.audioData.editorUser != this.$store.state.user_id &&
          this.audioData.editorUser != 0
        ) {
          this.$router.push({
            path: "/audios/"
          });
        }
      })
      .catch(error => {
        console.log(error);
        this.errored = true;
      });
    console.log("que je l'aimerai toujours  " + this.id);
  }
};
</script>
<style>
</style>
