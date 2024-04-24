<script setup lang="ts">

 defineProps({
    slides: Array,
  })

</script>

<template>
    <div class="flex carousel overflow-hidden absolute">
        <div class="flex relative carousel-slides" >
            <slot/>
        </div>
    </div>
</template>

<style>
    .carousel {
        height: 350px;
    }

    .carousel-slides {
        width: 600px;
    }
</style>