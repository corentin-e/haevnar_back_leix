<script setup>
    import {ref} from 'vue'
    import 'vue3-carousel/dist/carousel.css'
    import { Slide } from 'vue3-carousel'
    import CarouselHaev from '@/components/carousel/generic/CarouselHaev.vue'
    import image1 from '@/assets/images/Star-Citizen-Alpha-3.3-2-672x372.jpg'
    import image2 from '@/assets/images/store_slideshow_large.jpg'
    import image3 from '@/assets/images/wallpaper_star_citizen_38_1920x1080.jpg'

    const actualitiesData = ref([
        {
            id: 1,
            title: "Titre 1",
            date: "03-03-24",
            description: "Test 1 de description",
            autor: "Etharion",
            image: image1,
        },
        {
            id: 2,
            title: "Titre 2",
            date: "13-03-24",
            description: "Test 2 de description",
            autor: "Etharion",
            image: image2,
        },
        {
            id: 3,
            title: "Titre 3",
            date: "23-03-24",
            description: "Test 3 de description",
            autor: "Etharion",
            image: image3,
        }
    ])
</script>

<template>
    <CarouselHaev
        pagination
    >
        <Slide
            class="haev_carousel_slide"
            v-for="slide in actualitiesData" 
            :key="slide"
        >
            <div class="flex justify-center w-full p-32">
                <div class="w-1/2 p-5">
                    <div class="flex justify-between">
                        <span class="font-bold">"{{slide.title}}"</span>
                        <span class="font-bold">{{slide.date}}</span>
                    </div>
                    <span class="flex mt-5 text-left">
                        {{slide.description}}
                    </span>
                    <span class="flex mt-5 text-left italic font-bold text-haev_orange">
                        {{ slide.autor }}
                    </span>
                </div>
                <div class="w-1/2 overflow-hidden rounded-lg haev_slide-image-size">
                    <img :src="slide.image" alt="" class="w-full h-full">
                </div>
            </div>
            
        </Slide>
    </CarouselHaev>
</template>

<style>
 .haev_carousel {
    height: 400px;
 }

 .haev_carousel_slide {
    height: 400px;
 }

 .haev_slide-image-size {
    height: 350px;
 }

</style>
