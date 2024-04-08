<script setup lang="ts">

import LogoShipHaevnarWhite from '@/assets/logos/logo_ship_haevnar_white.png'
import WelcomeImg from '@/assets/images/welcome-image.png'

</script>

<template>
    <div class="overflow-hidden img-frame-custom">
      <div class="relative text-haev_white z-20 w-full h-full p-24 text-custom">
        <div class="flex items-start h-full">
          <div class="w-4/5">
            <p class="text-first-custom text-custom">
              Bienvenue sur le site de l'Alliance d'Hævnär,
            </p>
            <p class="pt-2">
              Un réseau interstellaire de corporations unifiées et de citoyens visionnaires dans l'univers de Star Citizen.
            </p>
            <p class="pt-2">
              Une alliance dynamique et diversifié de corporations spécialisées, s'étendant des activités d'exploration et de mercenariat, à la logistique et au sport compétitif.
            </p>
            <p  class="pt-2">
              Nous sommes une communauté soudée de pionniers, d'explorateurs, de commerçants, et de guerriers, œuvrant ensemble pour forger un avenir meilleur dans les vastes étendues de l'espace.
            </p>
            <p  class="pt-2">
              Chez nous, vous trouverez une place pour vous et les votres, que vous soyez un vétéran de l'espace ou un nouveau venu dans l'univers de Star Citizen.
            </p>
          </div>
          <img :src="LogoShipHaevnarWhite" alt="welcome image" class="w-1/5">
        </div>
      </div>
      <img :src="WelcomeImg" alt="welcome image" class="w-full img-size-custom">
    </div>
</template>