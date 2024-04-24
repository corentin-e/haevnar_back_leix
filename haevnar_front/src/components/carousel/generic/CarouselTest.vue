<script setup>
import {ref} from 'vue'
    // If you are using PurgeCSS, make sure to whitelist the carousel CSS classes
    import 'vue3-carousel/dist/carousel.css'
    import { Carousel, Slide, Pagination } from 'vue3-carousel'
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
    <Carousel class="mt-5">
        <Slide 
            v-for="slide in actualitiesData" 
            :key="slide"
        >
            <div class="flex justify-center">
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
            
        </Slide>

        <template #addons>
        <Pagination />
        </template>
    </Carousel>
</template>

<style>
    .carousel__item {
        min-height: 300px;
        width: 100%;
        background-color: var(--vc-clr-primary);
        color: var(--vc-clr-white);
        font-size: 20px;
        border-radius: 8px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .carousel__slide {
        padding: 10px;
    }

    .carousel__prev,
    .carousel__next {
        box-sizing: content-box;
        border: 5px solid white;
    }
</style>
