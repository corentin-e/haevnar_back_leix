<script setup>
    import { onMounted } from 'vue'

    import ShortList from '@/components/list/generic/ShortList.vue';
    import CardListEvent from '@/components/card/specific/CardListEvent.vue';
    import axios from 'axios'

    onMounted(() => {
        const eventsArray = axios.get('http://localhost:8000/events/')
    })
</script>

<template>
    <ShortList
        title-list="Nouvelles Événements"
        w-list="1/2"
    >
        <div v-for="event in eventsArray" :key="event.id" >
            <CardListEvent  
                :name="event.name" 
                :date="event.date"
            />
        </div>

    </ShortList>
</template>