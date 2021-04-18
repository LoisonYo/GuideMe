<template>
    <LMap ref="map" @input="handleInput" @click="setPosition" 
        :zoom="zoom" :center="origin" 
        style="height: 300px; width: 100%; position:relative; z-index: 0;">
        <LTileLayer :url="url" :attribution="attribution"/>
        <LMarker :lat-lng.sync="center" :icon="icon" />
    </LMap>
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
    props: {
        value: {
            type: Object,
            required: true,
        },
        setPositionEnable: {
            type: Boolean,
            default: true,
        }
    },
    
    data()
    {
        return {
            content: this.value,
            url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            origin: undefined,
            center: undefined,
            zoom: 10,
            icon: icon({
				iconUrl: marker,
				iconSize: [50, 50],
				iconAnchor: [25, 50],
			}),
        }
    },
    mounted() {
        this.$nextTick(() => {
			this.map = this.$refs.map.mapObject // work as expected
			this.map.zoomControl.remove()
		});

        this.origin = latLng(47, 6.9);
        this.center = this.origin;
    },
    methods: {
        handleInput() {
            this.$emit('input', this.content)
        },
        setPosition(event) {
            if (this.setPositionEnable) {
                this.center = event.latlng;
                this.content.latitude = this.center.lat.toFixed(5);
                this.content.longitude = this.center.lng.toFixed(5);
            }
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