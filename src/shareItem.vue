<template>
  <div>
    <div class="has-text-right">
      <span class="icon">
        <i class="fas fa-share"></i>
      </span>
      <span class="is-size-7 is-uppercase">
        <a @click="showShare=true">
          {{ shareText }}
        </a>
      </span>
    </div>
    <div class="card share-card" v-if="showShare">
      <div class="card-content">
        <div class="content">
          <div class="columns zero-space">
            <div class="column is-offset-10 zero-space">
              <a class="card-header-icon zero-space close-button" @click="showShare=false">
                <span class="icon">
                  <i class="fas fa-window-close"></i>
                </span>
              </a>
            </div>
          </div>
          <social-sharing :url="url"
                      :title="title"
                      :description="description"
                      :quote="quote"
                      twitter-user="nicolaskb"
                      inline-template>
            <div>
              <div class="columns">
                <div class="column is-half no-padding">
                  <a>
                    <network network="email">
                        <i class="fa fa-envelope"></i> <span class="is-size-7">Email</span>
                    </network>
                  </a>
                </div>
                <div class="column is-half no-padding">
                  <a>
                    <network network="facebook">
                        <i class="fab fa-facebook"></i> <span class="is-size-7">Share</span>
                    </network>
                  </a>
                </div>
              </div>
              <div class="columns">
                <div class="column is-half no-padding">
                  <a>
                    <network network="twitter">
                        <i class="fab fa-twitter"></i> <span class="is-size-7">Tweet</span>
                    </network>
                  </a>
                </div>
                <div class="column is-half no-padding">
                  <a>
                    <network network="linkedin">
                        <i class="fab fa-linkedin"></i> <span class="is-size-7">Linkedin</span>
                    </network>
                  </a>
                </div>
              </div>
              <div class="columns">
                <div class="column is-half no-padding">
                  <a>
                    <network network="reddit">
                        <i class="fab fa-reddit"></i> <span class="is-size-7">Reddit</span>
                    </network>
                  </a>
                </div>
              </div>
            </div>
          </social-sharing>
          <hr>
          <div>
            <span class="is-size-7">
              Permalink
            </span>
            <input class="input is-small" readonly :value="url">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

var SocialSharing = require('vue-social-sharing');

export default {
  name: 'shareitem',
  data(){
    return {
      showShare: false,
      url: window.location
    }
  },
  components: {
    SocialSharing
  },
  props: {
    title: {
      default: "",
      type: String
    },
    description: {
      default: "",
      type: String
    },
    quote: {
      default: "",
      type: String
    },
    shareText: {
      default: "",
      type: String
    }
  }

}
</script>

<style lang="sass">
.zero-space
  margin: 0
  padding: 0
  margin-bottom: -.2rem;

.close-button
  justify-content: end;

.share-card
  position: absolute
  z-index: 3

.no-padding
  padding: 0
</style>
