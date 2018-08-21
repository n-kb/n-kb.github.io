<template>
  <div>
    <div v-if="articles.length > 0">
      <div class="columns" v-for="article in articles">
        <div class="column has-text-left">
          <router-link :to="{ name: 'single-article', params: { slug: article.url }}">{{ article.title }}</router-link>
          <span class="is-size-7 is-hidden-tablet">
            {{ article.date }}
          </span>
        </div>
        <div class="column is-1 is-hidden-mobile">
          <span class="tag is-light">{{article.lang}}</span>
        </div>
        <div class="column is-2 is-size-7 has-text-right is-hidden-mobile">
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
