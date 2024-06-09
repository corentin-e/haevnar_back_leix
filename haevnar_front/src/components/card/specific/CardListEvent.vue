<script setup>
    import CardList from '../generic/CardList.vue'

    defineProps({
        name: String ,
        date: String,
    })

    const formatDate = (valueDate) => {
        let dateFormat = new Date (valueDate)
        let dd = dateFormat.getDate()
        let mm = dateFormat.getMonth() + 1
        let yyyy = dateFormat.getFullYear()
        if (dd < 10) {
            dd = '0' + dd;
        }
        if (mm < 10) {
            mm = '0' + mm;
        }
        return dateFormat = dd + '-' + mm + '-' + yyyy
    }
</script>

<template>
    <CardList 
        bg-card="haev_white"
        bgTagCard="haev_orange"
        :tags="name"
        card-image
    >
        <div class="flex justify-between h-24 items-center relative">
            <div class="flex bg-haev_black opacity-40 w-full absolute justify-between p-5 h-full items-end z-30"></div>
            <div class="absolute bg-haev_orange h-4 w-4 rounded-full z-40 bottom-3 left-3 shadow-haev-indicator shadow-haev_orange"></div>
            <span class="font-bold text-lg absolute right-5 bottom-5 transition-all duration-500 z-40 text-haev_white">{{ formatDate(date) }} | 10:00</span>
        </div>
    </CardList>
</template>

<style>
    .shadow-haev-indicator {
        box-shadow: 0 0 3px 1px var(--haev_orange);
        animation: shadowmove 1.5s infinite;
    }
    @keyframes shadowmove {
        100% {box-shadow: 0 0 9px 2px var(--haev_orange);}
    }
</style>