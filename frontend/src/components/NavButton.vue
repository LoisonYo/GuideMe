<template>
    <v-btn :class="color" class="darken-3 mr-3" :to="{ name: link }">
        <span class="mr-2">{{text}}</span>
        <v-icon>mdi-{{icon}}</v-icon>
        <v-icon>mdi-{{subIcon}}</v-icon>
    </v-btn>
</template>

<script>
export default {
  props: {
    color: {
      type: String,
      required: true
    },
    icon: {
      type: String,
      required: true
    },
    subIcon: {
      type: String,
      required: false
    },
    link: {
      type: String,
      required: true
    },
    text: {
      type: String,
      required: true
    },
  }
}
</script>

<style>

</style>
