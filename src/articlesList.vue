<template>
  <div>
    <div v-if="articles.length > 0">
      <div class="columns" v-for="article in articles">
        <div class="column has-text-left">
          <a :href="article.url">{{ article.title }}</a>
        </div>
        <div class="column is-1">
          <span class="tag is-light">{{article.lang}}</span>
        </div>
        <div class="column is-2 is-size-7 has-text-right">
          {{ article.date }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import moment from 'moment'

export default {
  name: 'articleslist',
  props: {
    articles: {
      default: [],
      type: Array
    }
  }
}
</script>

<style lang="sass">
</style>
