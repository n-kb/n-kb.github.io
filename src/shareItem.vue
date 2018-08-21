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
          <div>
            <a href="https://twitter.com/nicolaskb" target="_blank">
              <span class="icon">
                <i class="fab fa-twitter"></i>
              </span>
              <span class="is-size-7">
                Tweet
              </span> 
            </a>
          </div>
          <div>
            <a href="https://www.facebook.com/nicolas.kayserbril/" target="_blank">
              <span class="icon">
                <i class="fab fa-facebook"></i>
              </span>
              <span class="is-size-7">
                Share
              </span>
            </a>
          </div>
          <hr>
          <div>
            <span class="is-size-7">
              Permalink
            </span>
            <input class="input is-small" readonly value="http://">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'shareitem',
  data(){
    return {
      showShare: false
    }
  },
  props: {
    title: {
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
</style>
