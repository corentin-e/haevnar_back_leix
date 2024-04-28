<script setup>
    import { ref } from 'vue'
    import CardList from '../generic/CardList.vue'
    import OmniLogo from '@/assets/logo-omniworks/OMNIWORKS-Logo-1.png'

    const tagsArray = ref([
        {
            name: "Omniworks",
        },
    ])
</script>

<template>
    <CardList 
        bg-card="haev_white"
        bgTagCard="haev_orange"
        :tags="tagsArray"
        card-image
    >
        <div class="flex justify-between h-24 items-center relative">
            <div class="flex bg-haev_black opacity-40 w-full absolute justify-between p-5 h-full items-end">
                <div class="state-indicator"></div>
            </div>
            <span class="font-bold text-lg absolute right-5 bottom-5">03-03-24 | 10:00</span>
        </div>
    </CardList>
</template>

<style>
    .state-indicator {
        
    }
</style>