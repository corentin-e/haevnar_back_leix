<script setup lang="ts">

import { ref } from 'vue'
import CarouselPoint from '../generic/CarouselPoint.vue';
import image1 from '@/assets/images/Star-Citizen-Alpha-3.3-2-672x372.jpg'
import image2 from '@/assets/images/store_slideshow_large.jpg'
import image3 from '@/assets/images/wallpaper_star_citizen_38_1920x1080.jpg'

const actualitiesData = ref([
    {
        id: 1,
        title: "Titre 1",
        date: "03603624",
        description: "Test 1 de description",
        image: image1,
    },
    {
        id: 2,
        title: "Titre 2",
        date: "13603624",
        description: "Test 2 de description",
        image: image2,
    },
    {
        id: 3,
        title: "Titre 3",
        date: "23603624",
        description: "Test 3 de description",
        image: image3,
    }
])

</script>

<template>
    <div
        class="flex justify-center mt-5 w-full "
    >
        <CarouselPoint> 
            <div 
                v-for="slide in actualitiesData"
                :key="slide.id"
                class="flex cursor-pointer justify-center relative"
            >
                <div class="w-1/2 p-5">
                    <div class="flex justify-between">
                        <span class="font-bold">{{slide.title}}</span>
                        <span class="font-bold">{{slide.date}}</span>
                    </div>
                    <span class="p-2">
                        {{slide.description}}
                    </span>
                </div>
                <div class="w-1/2 overflow-hidden rounded-lg shadow-2xl slide-image-size">
                    <img :src="slide.image" alt="" class="w-full h-full">
                </div>
            </div>
        </CarouselPoint>
    </div>
</template>

<style>
    .slide-image-size {
        height: 350px;
    }
</style>