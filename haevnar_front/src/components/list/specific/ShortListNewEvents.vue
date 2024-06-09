<script setup lang="ts">
    import { ref, onMounted } from 'vue'

    import ShortList from '@/components/list/generic/ShortList.vue';
    import CardListEvent from '@/components/card/specific/CardListEvent.vue';
    import axios from 'axios'

    interface Events {
        create_by: Number,
        date: Date,
        description: String,
        emplacement: String,
        id: Number,
        name: String,
    }

    const events= ref([] as Events[])

    const getEvents = () => {
        axios
        .get('http://localhost:8000/events/')
        .then((response) => {
            events.value.push(response.data[0])
        })
    }

    onMounted(async () => {
        await getEvents()
    })

</script>

<template>
    <ShortList
        title-list="Nouvelles Événements"
        w-list="1/2"
    >
        <div v-for="event in events" :key="event.id" >
            <CardListEvent  
                :name="event.name" 
                :date="event.date"
            />
        </div>

    </ShortList>
</template>