<script setup lang="ts">
import { defineProps } from 'vue'
import type { Project } from '@/types'
import TagItem from '@/components/TagItem.vue'
defineProps<{
  project: Project;
}>()
</script>

<template>
    <div class="project-card">
      <h2>{{ project.title }}</h2>
      <p>{{ project.description }}</p>
      <img :src="project.image" :alt="project.title" />
      <!-- Todo featured, ? date created, date updated, url, git ? -->
      <TagItem v-for="tag in project.tags" :key="tag.id" :tag="tag" />
    </div>
</template>

<style scoped>
</style>