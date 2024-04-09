<script setup lang="ts">

import { ref } from 'vue'
import CarouselPoint from '../generic/CarouselPoint.vue';

const actualitiesData = ref([])

</script>

<template>
    <div
        class="flex w-full mt-5"
    >
        <CarouselPoint :slides="actualitiesData"/>
    </div>
</template>