<script setup>
    import ShortList from '@/components/list/generic/ShortList.vue';
    import CardListEvent from '@/components/card/specific/CardListEvent.vue';
</script>

<template>
    <ShortList 
        title-list="Nouvelles Événements"
        w-list="1/2"
    >
        <CardListEvent/>
    </ShortList>
</template>