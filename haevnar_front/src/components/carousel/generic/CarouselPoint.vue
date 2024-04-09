<script setup lang="ts">

 defineProps({
    slides: Array,
  })

</script>

<template>
    <div
        class="flex w-full"
    >
        <div class="w-1/2 p-5">
            <div class="flex justify-between">
                <span class="font-bold">"Titre"</span>
                <span class="font-bold">03-03-24</span>
            </div>
            <span class="p-2">
                Test Text Pour Carousel
            </span>
        </div>
        <div class="w-1/2 h-56 bg-haev_white rounded-lg shadow-2xl">
        </div>
    </div>
</template>