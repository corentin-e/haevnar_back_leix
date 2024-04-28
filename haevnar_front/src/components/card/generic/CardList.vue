<script setup>
    import testImage1 from '@/assets/images/Star-Citizen-Alpha-3.3-2-672x372.jpg'
     defineProps({
        bgCard: String,
        bgTagCard: String,
        tags: [Array, String],
        cardImage: Boolean,
    })
</script>

<template>
    <div
        class="w-full rounded-md relative overflow-hidden"
        :class="`bg-${bgCard}`"
    >
        <div v-if="tags">
            <div 
                v-for="tag in tags"
                :key="`tag_${tag.name}`"
                class="w-fit pl-5 pr-5 rounded-br-md absolute font-semibold z-50"
                :class="`bg-${bgTagCard}`"
            >
            {{ tag.name }} 
            </div>
        </div>
            <slot/>
        <img 
            v-if="cardImage" 
            :src="testImage1" alt="" class="w-full absolute top-0 z-10"
        >
    </div>
</template>