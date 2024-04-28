<script setup>
    import {ref} from 'vue'
    import 'vue3-carousel/dist/carousel.css'
    import { Slide } from 'vue3-carousel'
    import CarouselHaev from '@/components/carousel/generic/CarouselHaev.vue'
    import image1 from '@/assets/images/Star-Citizen-Alpha-3.3-2-672x372.jpg'
    import image2 from '@/assets/images/store_slideshow_large.jpg'
    import image3 from '@/assets/images/wallpaper_star_citizen_38_1920x1080.jpg'

    const actualitiesScData = ref([
        {
            id: 1,
            image: image1,
        },
        {
            id: 2,
            image: image2,
        },
        {
            id: 3,
            image: image3,
        }
    ])
</script>

<template>
    <CarouselHaev>
        <Slide
            class="haev_carousel_slide"
            v-for="slide in actualitiesScData" 
            :key="slide.id"
        >
            <div class="flex justify-center w-full p-32">
                <div class="w-full overflow-hidden rounded-lg haev_slide-image-size">
                    <img :src="slide.image" alt="" class="w-full">
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
