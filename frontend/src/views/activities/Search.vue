<template>
	<div style="width:100%;">

		<OptionsSearch v-on:value="radius = Number($event)" :center="center.wrap()" />

		<l-map :zoom="zoom" :center="origin" ref="map" :worldCopyJump="true" 
			style="height: 100vh; width:100%; position: fixed; top:0;"
			@click="setPosition"
			@update:center="centerUpdate"
			@update:zoom="zoomUpdate">

			<l-tile-layer :url="url" :attribution="attribution"/>

			<l-circle
				:lat-lng="center"
				:radius="radius"
				color="#7B87D1"
			/>

			<l-marker
				:lat-lng.sync="center"
				:icon="icon"
			/>
		</l-map>
	</div>
</template>

<script>
import { latLng, icon } from "leaflet";
import { LMap, LTileLayer, LMarker, LCircle } from 'vue2-leaflet';
import marker from "@/assets/marker.svg";
import OptionsSearch from '@/components/activities/OptionsSearch.vue';

export default {
	name: 'Search',
	components: {
		LMap,
		LTileLayer,
		LMarker,
		LCircle,
		OptionsSearch,
	},
	data() {
		return {
			radius: 1000,
			maxBounds: [[-90,-180], [90,180]],
			zoom: 13,
			url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
			attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
			center: latLng(47.053011, 7.067925),
			origin: latLng(47.053011, 7.067925),
			icon: icon({
				iconUrl: marker,
				iconSize: [50, 50],
				iconAnchor: [25, 50],
			}),
		}
	},

	mounted()
	{
		this.$nextTick(() => {
			this.map = this.$refs.map.mapObject // work as expected
			this.map.zoomControl.remove()
		});
	},

	methods: {
		setPosition(event) {
			this.center = event.latlng;
		},
		zoomUpdate(zoom) {
			this.currentZoom = zoom;
		},
		centerUpdate(center) {
			this.currentCenter = center;
		},
	},
}
</script>

<style>
</style>