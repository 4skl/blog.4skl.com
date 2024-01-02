<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';
import type { Project, ProjectNumberTags} from '@/types';
import { projectsNumberTagsToProjects } from '@/utils/projects';
import ProjectCard from '@/components/ProjectCard.vue';

const title = ref('');
const content = ref('');
const projects = ref(new Array<Project>());

onMounted(async () => {
  try {
    //load main page content
    const response = await axios.get(`${import.meta.env.VITE_APP_API_BASE_URL}/page/home/?format=json`);
    title.value = response.data.title;
    content.value = response.data.content;

    //load featured projects
    const projects_build: ProjectNumberTags[] = (await axios.get(`${import.meta.env.VITE_APP_API_BASE_URL}/projects/featured/?format=json`)).data as ProjectNumberTags[];;
    // Then get the tags data for each project efficiently (reducing the number of requests and theirs size)
    projects.value = await (projectsNumberTagsToProjects(projects_build) as Promise<Project[]>);
  } catch (error) {
    console.error(error);
  }
});
</script>

<template>
  <div class="home page">
    <h1>{{ title }}</h1>
    <div class="content" v-html="content"></div>
      <h2 v-if="projects.length === 1" class="featured-project-title">Featured project</h2>
      <h2 v-else class="featured-project-title">Featured projects</h2>
      <div class="projects">
        <div v-if="projects.length === 0">No featured projects</div>
        <ProjectCard v-for="project in projects" :key="project.handle" :project="project" />
      </div>
  </div>
</template>

<style>
.featured-project-title {
  text-align: center;
  margin-bottom: 1em;
  margin-top: 2em;
}

</style>
