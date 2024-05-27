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
        :tags="tagsArray"
        card-item
    >
        <div class="flex p-5 justify-between h-24 items-center">
            <span class="text-nemesis-mode font-bold text-lg transition-all duration-500">03-04-24</span>
            <span class="text-nemesis-mode font-bold text-lg transition-all duration-500">OmniWorks</span>
            <img :src="OmniLogo" alt="" class="w-20">
        </div>
    </CardList>
</template>