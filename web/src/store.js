import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    tweets: []
  },
  getters: {
    tweets: state => state.tweets
  },
  mutations: {
    setTweets: (state, tweets) => {
      state.tweets = tweets
    },
    addTweet: (state, tweet) => {
      state.tweets.unshift(tweet)
    }
  },
  actions: {
    setTweets: ({ commit }, tweets) => commit('setTweets', tweets),
    addTweet: ({ commit }, tweet) => commit('addTweet', tweet)
  }
})
