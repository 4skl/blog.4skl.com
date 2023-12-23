<script setup lang="ts">
import { defineProps } from 'vue';
import type { Project } from '@/types';
import TagItem from '@/components/TagItem.vue';
defineProps<{
  project: Project;
}>()
</script>

<template>
  <div class="project-card">
        <img :src="project.image" :alt="project.title" />
        <h2>{{ project.title }}</h2>
        <p>{{ project.description }}</p>
        <!-- Todo featured, ? date created, date updated, url, git ? -->
        <TagItem v-for="tag in project.tags" :key="tag.id" :tag="tag" />
        <p>hellp</p>
  </div>
</template>

<style scoped>
.project-card {
  display: grid;
  grid-template-columns: 1fr;
}

.project-card > img {
  
}

</style>