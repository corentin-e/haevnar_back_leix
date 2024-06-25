<script setup lang="ts">
    import ShortList from '@/components/list/generic/ShortList.vue';
    import CardListEvent from '@/components/card/specific/CardListEvent.vue';

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