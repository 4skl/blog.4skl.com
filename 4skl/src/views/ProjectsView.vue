<script setup lang="ts">
import { ref, onMounted, computed } from 'vue';
import type { Project, Tag } from '@/types';
import { useProjectsStore } from '@/stores/projects';
import { useTagsStore } from '@/stores/tags';
import ProjectCard from '@/components/ProjectCard.vue';
import TagItem from '@/components/TagItem.vue';

const projects = ref([] as Project[]);
const tags = ref([] as Tag[]);
const tagsFilter = ref([] as Tag[]);
const searchName = ref('');

const tagStore = useTagsStore();
const projectStore = useProjectsStore();

const toggleTagFilter = (tag: Tag) => {
  const index = tagsFilter.value.findIndex(t => t.id === tag.id);
  if (index > -1) {
    tagsFilter.value.splice(index, 1);
  } else {
    tagsFilter.value.push(tag);
  }
};

const isTagSelected = (tag: Tag) => {
  return tagsFilter.value.some(filterTag => filterTag.id === tag.id);
};

const filteredProjects = computed(() => {
  let result = projects.value;

  // Filter by tags
  if (tagsFilter.value.length > 0) {
    result = projectStore.filterProjectsByTags(tagsFilter.value);
  }

  // *AND* Filter by project name
  if (searchName.value.length > 0) {
    result = result.filter(project => projectStore.searchProject(searchName.value).includes(project));
  }

  return result;
});

onMounted(async () => {
  // Fetch data from API
  await tagStore.loadTags();
  tags.value = tagStore.tags;
  await projectStore.loadProjects();
  projects.value = projectStore.projects;
});

</script>

<template>
  <div class="projects-filter">
    <div class="tag-filter">
      <h3>Filter by tags : </h3>
      <div v-if="tags.length === 0">No tags</div>
      <!-- List of tags -->
      <div v-else class="tags">
        <span v-for="tag in tags" :key="tag.id">
          <TagItem :tag="tag" :selected="isTagSelected(tag)" @toggle-tag="toggleTagFilter" />
        </span>
      </div>
    </div>
    <!-- Searchbar for projects -->
    <input type="text" v-model="searchName" placeholder="Search projects" class="search-bar"/>
  </div>
  <div class="projects">
    <div v-if="filteredProjects.length === 0">No projects</div>
    <ProjectCard v-for="project in filteredProjects" :key="project.handle" :project="project" />
  </div>
</template>

<style>

.projects-filter {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: auto;
  margin-bottom: 1em;
  max-width: 800px;
}

.tag-filter {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 1em;
}

.tags {
  margin-left: 1em;
}

.tags > * {
  cursor: pointer;
}

.search-bar {
  margin-bottom: 1em;
}
</style>
