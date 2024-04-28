<script setup>
    import { ref } from 'vue'
    import CardList from '../generic/CardList.vue'
    const tagsArray = ref([
        {
            name: "Omniworks",
        },
    ])
</script>

<template>
    <CardList 
        bg-card="haev_white"
        bgTagCard="haev_dark"
        :tags="tagsArray"
    >
        <div class="flex p-5 justify-between h-24 items-center">
            <span class="text-nemesis-mode font-bold text-lg">03-04-24</span>
            <span class="text-nemesis-mode w-1/2 font-bold text-lg">[OMNI] Nicklas</span>
        </div>
    </CardList>
</template>