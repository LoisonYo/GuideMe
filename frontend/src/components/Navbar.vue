<template>
  <v-app-bar
    app
    dark
  >
    <h2>
      <router-link class="white--text" style="text-decoration: none" :to="{ name: 'home' }">
        <v-icon>mdi-coffee</v-icon>
        Coffee Counter
      </router-link>
    </h2>

    <v-spacer></v-spacer>

    <div v-if="loggedIn">
      <NavButton :color="'green'" :link="'scoreboard'" :text="'Scoreboard'" :icon="'earth'"></NavButton>

      <NavButton :color="'blue'" :link="'counter'" :text="'Counter'" :icon="'coffee'" :subIcon="'unfold-more-horizontal'"></NavButton>
      
      <NavButton :color="'red'" :link="'logout'" :text="'Logout'" :icon="'logout'"></NavButton>
    </div>
    <div v-else>
      <NavButton :color="'grey'" :link="'register'" :text="'Register'" :icon="'account-plus'"></NavButton>

      <NavButton :color="'indigo'" :link="'login'" :text="'Login'" :icon="'login'"></NavButton>
    </div>
  </v-app-bar>
</template>

<script>
import NavButton from './NavButton.vue'

export default {
  components: {
    NavButton,
  },
  computed: {
    loggedIn() {
      return this.$store.getters.loggedIn
    }
  }
}
</script>

<style>

</style>