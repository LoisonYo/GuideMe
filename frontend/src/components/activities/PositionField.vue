<template>
	<v-card @input="handleInput" style="background-color: transparent; box-shadow: none">
        <LMap @click="setPosition" :zoom="zoom" :center="origin" style="height: 300px; width: 100%;">
            <LTileLayer :url="url" :attribution="attribution"/>
            <LMarker :lat-lng.sync="center" :icon="icon" />
        </LMap>
	</v-card>
</template>

<script>
import { latLng, icon } from "leaflet";
import { LMap, LTileLayer, LMarker } from 'vue2-leaflet';
import marker from "@/assets/marker.svg";

export default {
    components:
    {
        LMap,
        LTileLayer,
        LMarker,
    },

	name: "PositionField",
    props: ['value'],

    data()
    {
        return {
            content: this.value,
            url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            origin: undefined,
            center: undefined,
            zoom: 0,
            icon: icon({
				iconUrl: marker,
				iconSize: [50, 50],
				iconAnchor: [25, 50],
			}),
        }
    },

    mounted()
    {
        this.origin = latLng(0, 0);
        this.center = this.origin;
    },

    methods:
    {
        handleInput()
        {
            this.$emit('input', this.content)
        },

        setPosition(event)
        {
			this.center = event.latlng;
            this.content.latitude = this.center.lat.toFixed(5);
            this.content.longitude = this.center.lng.toFixed(5);
		},
    },

    watch:
    {
        value:
        {
            handler(n)
            {
                this.content = n;
                this.origin = latLng(n.latitude, n.longitude);
                this.center = this.origin;
            },
            deep: true,
        }
    }
}
</script>

<style>

</style>