<script setup lang="ts">

  import { RouterLink } from 'vue-router'

  import WelcomePresentation from './part/presentation/WelcomePresentation.vue';
  import WelcomeActualities from './part/actualities/WelcomeActualities.vue';

  import { useThemeStore } from '@/stores/app-store'

  defineProps({
    darkModeActive: Boolean,
  })

  const theme = useThemeStore()

  theme.theme
</script>

<template>
  <div class="w-full justify-center flex flex-col pt-5 theme-mode transition-all duration-500">
    <WelcomePresentation/>
    <!-- Button - Banneer - Components -->
    <div class="bg-haev_orange p-5 flex justify-center">
      <RouterLink to="/registration">
        <button type="button" class="rounded-full border border-haev_dark bg-transparent text-haev_dark px-5 py-2 hover:bg-haev_dark hover:text-haev_orange transition-all duration-300">Rejoindre l'Alliance</button>
      </RouterLink>
    </div>
      <!-- News - Components -->
    <WelcomeActualities/>
  </div>
</template>

<style>
.text-first-custom::first-letter {
  font-family: "Slackside One", cursive;
  font-size: 64px;
}

.text-custom {
  font-size: 22px;
}

.title-news-custom::first-letter {
  font-family: "Slackside One", cursive;
  font-size: 94px;
}

.title-news-custom {
  font-size: 40px;
}

.title-sub-new-custom {
  font-family: "Slackside One", cursive;
  font-size: 33px;
  color: var(--haev_orange)
}
</style>
