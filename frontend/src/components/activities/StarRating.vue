<template>
	<v-card @input="handleInput" class="d-flex justify-space-around transparent" elevation="0">
        <v-btn v-for="n in max" :key="n" @click="onClick(n)" @mouseover="onHover(n)" @mouseleave="onLeave" icon style="width:0">
            <v-icon v-if="isActive(n)" color="rgb(107,119,180)">{{ icon_unchecked }}</v-icon>
            <v-icon v-if="!isActive(n)" color="rgb(107,119,180)">{{ icon_checked }}</v-icon>
        </v-btn>
	</v-card>
</template>

<script>
export default {
	name: "ReviewEditor",
    props: ['value', 'max'],

    data()
    {
        return {
            icon_checked: 'mdi-star',
            icon_unchecked: 'mdi-star-outline',
            content: this.value,
            hovering: false,
            hover: 1,
        }
    },

    methods:
    {
        handleInput()
        {
            this.$emit('input', this.content)
        },

        onClick(n)
        {
            this.content = n;
            this.handleInput();
        },

        onHover(n)
        {
            this.hover = n;
            this.hovering = true;
        },

        onLeave()
        {
            this.hovering = false;
        },

        isActive(n)
        {
            return (this.hovering) ? n > this.hover : n > this.content;
        },
    },
}
</script>

<style>

</style>