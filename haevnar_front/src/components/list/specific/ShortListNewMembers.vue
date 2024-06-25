<script setup>
    import ShortList from '@/components/list/generic/ShortList.vue';
    import CardListMember from '@/components/card/specific/CardListMember.vue';
</script>

<template>
    <ShortList 
        title-list="Nouveaux Membres"
    >
        <CardListMember/>
    </ShortList>
</template>