<script setup>
    import ShortList from '@/components/list/generic/ShortList.vue';
    import CardListClan from '@/components/card/specific/CardListClan.vue';
</script>

<template>
    <ShortList 
        title-list="Nouveaux Clans"
        w-list="1/2"
    >
        <CardListClan/>
    </ShortList>
</template>