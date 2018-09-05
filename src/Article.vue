<template>
  <div>
    <navbar></navbar>
    <section class="section">
      <div class="container is-fluid">
        <div class="columns">
          <div class="column is-2 is-offset-10">
            <shareitem :title="title" :shareText="share" :description="description"></shareitem>
          </div>
        </div>
        <div class="columns">
          <div class="column is-half is-offset-one-quarter">
            <div class="content">
              <h1 class="title is-1 has-text-centered is-size-3-mobile">{{ title }}</h1>
              <div class="columns">
                <div class="column has-text-centered">
                  <p class="byline">{{ intro }} <strong><router-link :to="{ name: 'home'}" class="byline--link">Nicolas Kayser-Bril</router-link></strong></p>
                </div>
                <div class="column byline has-text-centered">
                  <p class="byline">{{ date }}</p>
                </div>
              </div>
              <vue-markdown :source="source" class="article-content"></vue-markdown>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>

import { json } from 'd3'
import VueMarkdown from 'vue-markdown'
import navbar from './Navbar.vue'
import shareitem from './shareItem.vue'

export default {
  headful: {
    title: "",
    description: "",
    image: "",
    head: {
      'meta[charset]': { charset: 'utf-8' },
    }
  },
  name: 'single-article',
  components: {
    VueMarkdown,
    navbar,
    shareitem
  },
  data() {
    return {
      title: "",
      date: "",
      source: "",
      intro: "",
      share: "",
      image: "",
      description: ""
    }
  },
  created() {
    var slug = this.$route.params.slug

    // Fetches the markdown file
    var self = this
    var json_path = "./public/articles/" + slug + ".json"
    var is_prerendered = false
    if (window.location.pathname.slice(-1) == "/") {
      json_path = "../public/articles/" + slug + ".json"
      is_prerendered = true
    }
    json(json_path).then(function(data) {
      self.source = data.text
      if (is_prerendered) {
        function replaceAll(str, find, replace) {
            return str.replace(new RegExp(find, 'g'), replace);
        }
        self.source = replaceAll(self.source, "./public/images/", "../public/images/")
      }
      
      self.headful.image = "https://blog.nkb.fr/public/images/" + data.image
      self.title = data.title
      self.date = data.date
      self.intro = data.intro
      self.share = data.share
      self.description = data.description

      self.headful.title = data.title
      self.headful.description = data.description
    }).catch(function(error){
      console.log(error)
    });
  }

}
</script>

<style lang="sass">
h1
  font-weight: 200

.article-content
  font-size: 1.2rem
  line-height: 2rem
  font-family: Georgia

.byline
  font-variant: small-caps
  font-size: .8rem
  font-family: Georgia
</style>
