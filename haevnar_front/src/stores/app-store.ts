import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useThemeStore = defineStore('theme', () => {
  const theme = ref('dark')
  function onChangeThemeMode() {
    theme.value = theme.value == 'dark' ? 'light' : 'dark'
  }
  return { theme, onChangeThemeMode }
})
