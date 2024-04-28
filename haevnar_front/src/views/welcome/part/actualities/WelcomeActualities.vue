<script setup lang="ts">
  import CarouselAllianceActuality from '@/components/carousel/specific/CarouselAllianceActuality.vue'
  import CarouselScActuality from '@/components/carousel/specific/CarouselScActuality.vue'
  import ShortListNewClan from '@/components/list/specific/ShortListNewClan.vue';
  import ShortListNewMembers from '@/components/list/specific/ShortListNewMembers.vue';
  import ShortListNewEvents from '@/components/list/specific/ShortListNewEvents.vue';

</script>

<template>
    <span class="title-news-custom w-full text-center">
      Journal de l'Alliance
    </span>
    <div class="flex flex-col px-10">
      <span class="title-sub-new-custom">
        Vie de l'alliance
      </span>
      <CarouselAllianceActuality/>
      <div class="flex w-full mt-16 justify-between">
        <ShortListNewMembers class="mr-16"/>
        <ShortListNewClan class="mr-16"/>
        <ShortListNewEvents/>
      </div>
      <CarouselScActuality class="mt-16"/>
    </div>
</template>