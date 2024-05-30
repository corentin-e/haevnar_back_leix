<script setup>
    import CardList from '../generic/CardList.vue'

    defineProps({
        name: String,
        date: String,
    })
</script>

<template>
    <CardList 
        bg-card="haev_white"
        bgTagCard="haev_orange"
        :tags="name"
        card-image
    >
        <div class="flex justify-between h-24 items-center relative">
            <div class="flex bg-haev_black opacity-40 w-full absolute justify-between p-5 h-full items-end z-30">
                <div class="state-indicator"></div>
            </div>
            <span class="font-bold text-lg absolute right-5 bottom-5 transition-all duration-500 z-40 text-haev_white">{{date}} | 10:00</span>
        </div>
    </CardList>
</template>