<template>
  <div id="App">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'layout'
}
</script>

<style lang="sass">
  @import "colors.sass"
  $family-primary: "Arial"
  $title-size: 2.5em
  $weight-semibold: 200
  $body-family: "Arial"
  $primary: $nkb-purple
  $info: $nkb-lightblue
  $link: $nkb-darkblue

  @import "~bulma/bulma"
</style>
