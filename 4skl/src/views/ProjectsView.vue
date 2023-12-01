<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';

const title = ref('');
const content = ref('');

onMounted(async () => {
  try {
    const response = await axios.get(`${import.meta.env.VITE_APP_API_BASE_URL}/page/home/?format=json`);
    title.value = response.data.title;
    content.value = response.data.content;
  } catch (error) {
    console.error(error);
  }
});
</script>

<template>
  <div class="projects">
    <h1>Here are my projects</h1>
  </div>
</template>

<style>
.projects {
  min-height: 100vh;
  display: flex;
  align-items: center;
}
</style>
