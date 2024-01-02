<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';

const title = ref('');
const content = ref('');

onMounted(async () => {
  try {
    //load main page content
    const response = await axios.get(`${import.meta.env.VITE_APP_API_BASE_URL}/page/about/?format=json`);
    title.value = response.data.title;
    content.value = response.data.content;
  } catch (error) {
    console.error(error);
  }
});
</script>

<template>
  <div class="about page">
    <h1>{{ title }}</h1>
    <div class="content" v-html="content"></div>
  </div>
</template>

<style>
</style>
