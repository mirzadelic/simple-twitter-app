<template>
  <form
    class="my-5"
    ref="form"
    @submit.prevent="addTweet($v)"
    novalidate>
    <div class="row">
      <div class="col-sm-3 col-12">
        <input
          type="text"
          class="form-control"
          :class="{ 'red-border': $v.tweet.name.$error }"
          v-model="tweet.name"
          placeholder="Full name">
      </div>
      <div class="col-sm-7 col-12">
        <div class="input-group mb-3">
          <input
            type="text"
            class="form-control"
            :class="{ 'red-border': $v.tweet.content.$error }"
            v-model="tweet.content"
            placeholder="Tweet">
          <div class="input-group-append">
            <span class="input-group-text">{{ charsLeft }}</span>
          </div>
        </div>
      </div>
      <div class="col-sm-2 col-12">
        <button type="submit" class="btn btn-success">Add tweet</button>
      </div>
    </div>
    <div class="row" v-if="$v.tweet.$invalid && $v.tweet.$dirty">
      <div class="col-12 mt-2 text-danger">
        Please check all fields.
      </div>
    </div>
  </form>
</template>

<script>
import { required, maxLength } from 'vuelidate/lib/validators'
import TweetService from '@/services/TweetService'
import store from '@/store'

export default {
  data () {
    return {
      tweet: null
    }
  },
  validations: {
    tweet: {
      name: {
        required
      },
      content: {
        required,
        maxLength: maxLength(50)
      }
    }
  },
  created () {
    this.initForm()
  },
  computed: {
    charsLeft () {
      return 50 - this.tweet.content.length || 0
    }
  },
  methods: {
    initForm () {
      this.tweet = {
        name: '',
        content: ''
      }
    },
    addTweet ($v) {
      $v.tweet.$touch()
      if ($v.tweet.$invalid) return

      TweetService.save(this.tweet)
        .then(response => {
          store.dispatch('addTweet', response.data)
          this.initForm()
          $v.tweet.$reset()
        })
        .catch(error => {
          alert(error.response)
        })
    }
  }
}
</script>

<style scoped>
  .red-border {
    border-color: red;
  }
</style>
