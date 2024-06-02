<script setup>
    import { reactive } from 'vue'

    import ShortList from '@/components/list/generic/ShortList.vue';
    import CardListEvent from '@/components/card/specific/CardListEvent.vue';
    import axios from 'axios'

    const state = reactive({
      events: [],
    });

    const getEvents = () => {
        axios
        .get('http://localhost:8000/events/')
        .then((response) => {
            state.events = response.data.results;
        })
        console.log('events', state.events)
    }

    console.log('events', getEvents)

</script>

<template>
    <ShortList
        title-list="Nouvelles Événements"
        w-list="1/2"
    >
        <div>
            {{ events }}
        </div>
        <div v-for="event in events" :key="event.id" >
            <CardListEvent  
                :name="event.name" 
                :date="event.date"
            />
        </div>

    </ShortList>
</template>