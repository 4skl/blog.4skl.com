<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';
import type { Tag, Project } from '@/types';
import ProjectCard from '@/components/ProjectCard.vue';

const projects = ref(new Array<Project>());

onMounted(async () => {
  // Fetch data from API
  try {
    // First get the page of projects
    const projects_build = (await axios.get(`${import.meta.env.VITE_APP_API_BASE_URL}/projects/?format=json`)).data;
    const tags_id_set = ref(new Set<number>());

    // Then get the set of tags id related to theses projects
    projects_build.forEach((project: Project) => {
      project.tags.forEach((tag_id: number) => {
        tags_id_set.value.add(tag_id);
      });
    });

    // Then get the set of tags related to theses projects
    const tags_id_list = Array.from(tags_id_set.value);
    if (tags_id_list.length !== 0) {
      const tags: Tag[] = (await axios.get(`${import.meta.env.VITE_APP_API_BASE_URL}/tags/?format=json&ids=${tags_id_list.join(',')}`)).data;

      // Map the tags to the projects
      projects_build.forEach((project: Project) => {
        project.tags = project.tags.map((tag_id: number) => {
          return tags.find((tag: Tag) => tag.id === tag_id);
        });
      });
    }

    // Finally set the projects
    projects.value = projects_build;
    
    console.log(projects.value);
  } catch (error) {
    console.error(error);
  }
});
</script>

<template>
  <div class="projects">
    <div v-if="projects.length === 0">No projects</div>
    <ProjectCard v-for="project in projects" :key="project.handle" :project="project" />
  </div>
</template>

<style>
.projects {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
