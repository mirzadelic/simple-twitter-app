<template>
  <div v-if="loading" class="alert alert-warning">
    Loading..
  </div>
  <table class="table" v-else>
    <thead>
      <tr>
        <th scope="col">Name</th>
        <th scope="col">Tweet</th>
        <th scope="col" @click="orderByDate()">
          <span v-if="dateSortDir === '-'">↑</span>
          <span v-else>↓</span>
          Created at
        </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="tweet in tweets" :key="tweet.id">
        <th>{{ tweet.name }}</th>
        <th>{{ tweet.content }}</th>
        <th>{{ formatDate(tweet.created_at) }}</th>
      </tr>
    </tbody>
  </table>
</template>

<script>
import moment from 'moment'
import store from '@/store'
import TweetService from '@/services/TweetService'

export default {
  data () {
    return {
      loading: true,
      dateSortDir: '-'
    }
  },
  computed: {
    tweets () {
      return store.getters.tweets.map(x => {
        x['created_at'] = moment(x.created_at)
        return x
      })
    }
  },
  created () {
    this.getTweets()
  },
  methods: {
    orderByDate () {
      this.dateSortDir = (this.dateSortDir === '-') ? '' : '-'
      this.getTweets()
    },
    formatDate (date) {
      return moment(date).format('MM/DD/YYYY HH:mm:ss')
    },
    async getTweets () {
      this.loading = true
      const params = { ordering: this.dateSortDir + 'created_at' }
      const response = await TweetService.getAll(params)
      store.dispatch('setTweets', response.data)
      this.loading = false
    }
  }
}
</script>

<style scoped>
  .red-border {
    border-color: red;
  }
</style>
