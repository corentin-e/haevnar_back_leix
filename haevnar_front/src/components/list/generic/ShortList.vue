<script setup>
    defineProps({
        titleList: String,
        wList: String,
    })
</script>

<template>
    <div 
        class="flex flex-col"
        :class="`w-${wList}`"
    >
        <span class="title-sub-new-custom mb-5">{{ titleList }}</span>
        <div class="flex-col">
            <slot />
        </div>
    </div>
</template>