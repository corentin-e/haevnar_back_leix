<script setup lang="ts">
import { ref, computed, watch } from 'vue'

import { useThemeStore } from '@/stores/app-store'

import WelcomeLoader from '@/components/loading/specific/welcome/WelcomeLoader.vue'
import HeaderPage from '@/components/HeaderPage.vue'
import FooterPage from '@/components/FooterPage.vue'

//import axios from 'axios'

const theme = useThemeStore()

theme.theme

const loaderActive = ref(true)

const themeMode = computed(() => {
  return theme.theme
})

const themeModeNemesis = computed(() => {
  return theme.theme
})

watch(themeMode, (newTheme) => {
  if(newTheme == 'dark') {
    document.documentElement.style.setProperty('--bg_app', 'var(--haev_bg_mode_dark)');
    document.documentElement.style.setProperty('--text_app', 'var(--haev_text_mode_dark)');
  } else {
    document.documentElement.style.setProperty('--bg_app', 'var(--haev_bg_mode_light)');
    document.documentElement.style.setProperty('--text_app', 'var(--haev_text_mode_light)');
  }
})
watch(themeModeNemesis, (newTheme) => {
  if(newTheme == 'dark') {
    document.documentElement.style.setProperty('--bg_app_nemesis', 'var(--haev_bg_mode_nemesis_dark)');
    document.documentElement.style.setProperty('--bg_tag_nemesis', 'var(--haev_bg_tag_mode_nemesis_dark)');
    document.documentElement.style.setProperty('--text_app_nemesis', 'var(--haev_text_mode_nemesis_dark)');
  } else {
    document.documentElement.style.setProperty('--bg_app_nemesis', 'var(--haev_bg_mode_nemesis_light)');
    document.documentElement.style.setProperty('--bg_tag_nemesis', 'var(--haev_bg_tag_mode_nemesis_light)');
    document.documentElement.style.setProperty('--text_app_nemesis', 'var(--haev_text_mode_nemesis_light)');
  }
})


//  TODO
interface Events {
    create_by: Number,
    date: Date,
    description: String,
    emplacement: String,
    id: Number,
    name: String,
}

const events= ref([] as Events[])
//  end TODO


const loadApplication = async () => {
  await getEvents()

  const loader = document.getElementById('loader')
  loader?.classList.add("hidden-loader")
}


const getEvents = async () => {

  // const response: any = await axios.get('http://localhost:8000/events/')
  // MOCK
  const response: any = await new Promise ((resolve) => {
      setTimeout(() => {
          resolve({
              data: [
                  {
                      name: 'test',
                      date: '01-02-03',
                  }
              ]
          })
      }, 2000);
  })

  events.value.push(response.data[0])
}

</script>

<template >
  <div
    class="w-100 transition-all duration-500 theme-mode h-screen"
  >
    <WelcomeLoader
      id="loader"
      class="loader w-full h-full"
      @load="loadApplication"
    />
    <template v-if="events.length !== 0">
      <HeaderPage/>
      <router-view></router-view>
    </template>
  </div>

</template>

<style scoped>

.loader {
  transition: all .8s;
}
.hidden-loader {
  width: 0%;
  overflow: hidden;
  opacity: 0;
}
</style>
