<script setup lang="ts">
import { defineProps } from 'vue';
import type { Project } from '@/types';
import TagItem from '@/components/TagItem.vue';
import { formatDate } from '@/utils/helpers';
defineProps<{
  project: Project;
}>()
</script>

<template>
  <router-link :to="{ name: 'project', params: { handle: project.handle }}" class="project-card-container">
    <div class="project-card">
          <img v-if="project.image" :src="project.image" :alt="project.title" />
          <img v-else src="@/assets/no-image.svg" :alt="project.title" />
          <div class="project-info">
            <h2>{{ project.title }}</h2>
            <p>{{ project.description }}</p>
            <!-- Todo featured, ? date created, date updated, url, git ? -->
            <div class="lower-info">
              <span class="tags">
                <TagItem v-for="tag in project.tags" :key="tag.id" :tag="tag" />
              </span>
              <span class="date-created">{{ formatDate(project.date_created) }}</span>
            </div>
          </div>
    </div>
  </router-link>
</template>

<style scoped>
.project-card {
  display: flex;
  align-items: center;
  background-color: var(--color-border);
  padding: .5em;
  border-radius: .5em;
  color: var(--color-text);
  height: 10em;
  overflow: hidden;
  width: 90vw;
  max-width: 800px;
}

.project-card > img {
  margin-right: 1em;
  width: 20%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  border-radius: .5em;
  align-self: stretch;
}

.project-info {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  flex-grow: 1;
  align-self: stretch;
}

.lower-info {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: auto;
}
</style>