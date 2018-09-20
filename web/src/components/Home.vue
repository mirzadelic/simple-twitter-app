<template>
  <div class="row">
    <div class="col-12">
      <tweet-form />
      <tweet-list />
    </div>
  </div>
</template>

<script>
import TweetForm from '@/components/TweetForm'
import TweetList from '@/components/TweetList'

export default {
  name: 'Home',
  components: {
    TweetForm,
    TweetList
  },
  props: {
    msg: String
  }
}
</script>
