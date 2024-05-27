<script setup>
    import testImage1 from '@/assets/images/Star-Citizen-Alpha-3.3-2-672x372.jpg'
     defineProps({
        bgCard: String,
        bgTagCard: String,
        tags: [Array, String],
        cardImage: Boolean,
        cardItem: Boolean,
    })
</script>

<template>
    <div>
        <div
            v-if="cardItem"
            class="w-full rounded-br-md rounded-tr-md rounded-bl-md relative overflow-hidden"
            :class="bgCard ? `bg-${bgCard}` : 'bg-nemesis-mode'"
        >
            <div v-if="tags">
                <div 
                    v-for="tag in tags"
                    :key="`tag_${tag.name}`"
                    class="w-fit pl-5 pr-5 rounded-br-md absolute font-semibold z-40 delay-0"
                    :class="bgTagCard ? `bg-${bgTagCard}` : 'bg-tag-nemesis-mode'"
                >
                    {{ tag.name }} 
                </div>
            </div>
            <slot/>
        </div>
        <div
            v-if="cardImage"
            class="w-full rounded-br-md rounded-tr-md rounded-bl-md relative overflow-hidden"
        >
            <div v-if="tags">
                <div 
                    v-for="tag in tags"
                    :key="`tag_${tag.name}`"
                    class="w-fit pl-5 pr-5 rounded-br-md absolute font-semibold z-40 delay-0"
                    :class="bgTagCard ? `bg-${bgTagCard}` : 'bg-tag-nemesis-mode'"
                >
                    {{ tag.name }} 
                </div>
            </div>
                <slot/>
            <img 
                :src="testImage1" alt="" class="w-full absolute top-0 z-10"
            >
        </div>
    </div>
    
</template>