<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';
import type { Project, ProjectNumberTags} from '@/types';
import { projectsNumberTagsToProjects } from '@/utils/projects';
import ProjectCard from '@/components/ProjectCard.vue';

const projects = ref(new Array<Project>());

onMounted(async () => {
  // Fetch data from API
  try {
    // First get the page of projects
    const projects_build: ProjectNumberTags[] = (await axios.get(`${import.meta.env.VITE_APP_API_BASE_URL}/projects/?format=json`)).data as ProjectNumberTags[];
    // Then get the tags data for each project efficiently (reducing the number of requests and theirs size)
    projects.value = await (projectsNumberTagsToProjects(projects_build) as Promise<Project[]>);
  } catch (error) {
    console.error(error);
  }
});
</script>

<template>
  <div class="projects">
    <div v-if="projects.length === 0">No projects</div>
    <ProjectCard v-for="project in projects" :key="project.handle" :project="project" class="project-card-container" />
  </div>
</template>

<style>
.projects {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.project-card-container {
  margin-bottom: 1em;
}
</style>
