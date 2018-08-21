<template>
  <div>
    <vue-markdown :source="source"></vue-markdown>
  </div>
</template>

<script>

import * as d3 from 'd3'
import VueMarkdown from 'vue-markdown'

export default {
  name: 'single-article',
  components: {
    VueMarkdown
  },
  data() {
    return {
      source: ""
    }
  },
  created() {
    var slug = this.$route.params.slug

    // Fetches the markdown file
    var self = this
    d3.text("src/articles/" + slug + ".md").then(function(text) {
      console.log(text)
      self.source = text
    });
  }

}
</script>

<style lang="sass">
</style>
