<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';

const title = ref('');
const content = ref('');
const featuredProjects = ref([]);

onMounted(async () => {
  try {
    //load main page content
    const response = await axios.get(`${import.meta.env.VITE_APP_API_BASE_URL}/page/home/?format=json`);
    title.value = response.data.title;
    content.value = response.data.content;

    //load featured projects
    await axios.get(`${import.meta.env.VITE_APP_API_BASE_URL}/projects/featured/?format=json`);
    featuredProjects.value = response.data.featured_projects;
  } catch (error) {
    console.error(error);
  }
});
</script>

<template>
  <div class="home page">
    <h1>{{ title }}</h1>
    <div class="content" v-html="content"></div>

  </div>
</template>

<style>
</style>
