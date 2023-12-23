<script setup lang="ts">
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import type { Project, Tag } from '@/types';
import TagItem from '@/components/TagItem.vue';
import { formatDate } from '@/utils/helpers';

const project = ref();
const route = useRoute();

onMounted(async () => {
  const project_build = (await axios.get(`${import.meta.env.VITE_APP_API_BASE_URL}/projects/${route.params.handle}/?format=json`)).data;
  const tags_id_list = project_build.tags;
  const tags: Tag[] = (await axios.get(`${import.meta.env.VITE_APP_API_BASE_URL}/tags/?format=json&ids=${tags_id_list.join(',')}`)).data;
  project_build.tags = project_build.tags.map((tag_id: number) => {
    return tags.find((tag: Tag) => tag.id === tag_id);
  });
  project.value = project_build;
});
</script>

<template>
    <div class="project-page">
      <div v-if="project">
      <h1 class="project-title">{{ project.title }}</h1>
      <p class="project-description">{{ project.description }}</p>
      <div class="center-content">
        <div class="tags"><TagItem v-for="tag in project.tags" :key="tag.id" :tag="tag" /></div>
        <div><span class="date-created">{{ formatDate(project.date_created) }}</span> - <span class="date-updated">{{ formatDate(project.date_updated) }}</span></div>
      <img class="project-image" v-if="project.image" :src="project.image" :alt="project.title" />
      </div>
      <!-- Todo featured, ? date created, date updated, url, git ? -->
      <div class="project-content" v-html="project.content"></div>
      </div>
    </div>
</template>

<style scoped>

.project-page {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.project-title {
  font-size: 2em;
  font-weight: bold;
  text-align: center;
}

.project-description {
  font-size: 1.5em;
  font-style: italic;
  text-align: center;
  margin-bottom: .5em;
}

.tags {
  margin: .5em;
}

.project-image {
  margin-top: 1em;
  width: 100%;
  height: 50vh;
  object-fit: cover;
}

.center-content {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
</style>