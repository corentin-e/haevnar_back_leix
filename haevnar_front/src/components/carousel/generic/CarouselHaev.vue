<script setup>
    // If you are using PurgeCSS, make sure to whitelist the carousel CSS classes
   import 'vue3-carousel/dist/carousel.css'
   import { Carousel, Pagination, Navigation } from 'vue3-carousel'
   defineProps({
      pagination: Boolean,
   })
</script>

<template>
    <Carousel 
        class="haev_carousel" 
        :wrap-around="true"
    >
        <slot/>
            
        <template #addons>
            <Navigation/>
            <Pagination 
               v-if="pagination" 
               class="carousel-pagination-custom"
            />
        </template>
    </Carousel>
</template>

<style>
 .haev_carousel {
    height: 400px;
 }

 .carousel__prev {
    height: 60px;
    width: 60px;
    color: #000000;
 }
 .carousel__prev:hover {
    color: var(--haev_orange)!important;
 }
 .carousel__next {
    height: 60px;
    width: 60px;
    color: #000000;
 }
 .carousel__next:hover {
    color: var(--haev_orange)!important;
 }
 .carousel__icon {
    height: 60px;
    width: 60px;
 }
 .carousel__pagination-button::after {
    border-radius: 100%;
    height: 15px;
    width: 15px;
    background-color: #000000;
 }
 .carousel__pagination-button--active::after {
    background-color: var(--haev_orange);
 }
 .carousel__pagination-button::after:hover {
    background-color: var(--haev_orange);
 }
 .carousel-pagination-custom {
   position: static!important;
 }
</style>
