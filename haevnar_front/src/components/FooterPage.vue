<script setup lang="ts">
    import { useThemeStore } from '@/stores/app-store'

    import LogoTitleHaevnarBlack from '../assets/logos/logo_haevnar_black_title.png'
    import LogoTitleHaevnarWhite from '../assets/logos/logo_haevnar_white_title.png'

    const theme = useThemeStore()

    theme.theme

</script>

<template>
    <div 
        class="flex items-center justify-center px-5 pb-4 text-mode bg-mode w-full bottom-0 fixed"
    >
        <RouterLink to="/">
            <img 
                :src="theme.theme == 'dark' ? LogoTitleHaevnarWhite : LogoTitleHaevnarBlack"
                width="230"
                alt="logo title Haevnär"
            >
        </RouterLink>
    </div>
</template>

<style>
    .nav-link-custom {
        color: var(--text_app);
        border-bottom: 1px solid var(--text_app);
        transition: all 0.5s;
    }
    .nav-link-custom:hover {
        color: #F77C04;
        border-bottom: 1px solid #F77C04;
    }
</style>