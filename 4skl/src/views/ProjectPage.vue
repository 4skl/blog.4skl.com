<script setup lang="ts">
import { ref, onMounted, nextTick } from 'vue';
import { useRoute } from 'vue-router';
import type { Project } from '@/types';
import TagItem from '@/components/TagItem.vue';
import { formatDate } from '@/utils/helpers';
import { useProjectsStore } from '@/stores/projects';
import hljs from 'highlight.js';

const project = ref<Project>();

onMounted(async () => {
  const route = useRoute();
  const handle = route.params.handle as string;
  const projectsStore = useProjectsStore();
  await projectsStore.loadProjectContent(handle);
  project.value = projectsStore.getProjectByHandle(handle);

  // Highlight code blocks
  nextTick(async () => {
    // Check if dark mode is enabled
    const isDarkMode = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;

    // Import the appropriate highlight.js style
    if (isDarkMode) {
      await import('highlight.js/styles/dark.css');
    } else {
      await import('highlight.js/styles/github.css');
    }

    document.querySelectorAll('pre code').forEach((block) => {
      hljs.highlightElement(block as HTMLElement);
    });
  });

  // CKEditor img styling
  // Parse the HTML string into a Document object
  const parser = new DOMParser();
  const doc = parser.parseFromString(project.value.content as string, 'text/html');

  // Select all images and apply styles only if they don't have inline styles
  doc.querySelectorAll('img').forEach((img) => {
    if (!img.hasAttribute('style')) {
      img.style.maxWidth = '90%';
      img.style.height = 'auto';
      img.style.display = 'block';
      img.style.margin = 'auto';
      img.style.objectFit = 'cover';
    }
  });

  // Serialize the Document object back into an HTML string
  project.value.content = new XMLSerializer().serializeToString(doc);

});
</script>

<template>
    <div class="project-page">
      <div v-if="project">
      <div class="project-header">
        <h1 class="project-title">{{ project.title }}</h1>
        <p class="project-description">{{ project.description }}</p>
        <div class="tags"><TagItem v-for="tag in project.tags" :key="tag.id" :tag="tag" /></div>
        <div><span class="date-created">{{ formatDate(project.date_created) }}</span> - <span class="date-updated">{{ formatDate(project.date_updated) }}</span></div>
      </div>
      <img class="project-image" v-if="project.image" :src="project.image" :alt="project.title" loading="lazy"/>
      <!-- Todo featured, ? date created, date updated, url, git -->
      <div class="project-content" v-html="project.content"></div>
      </div>
    </div>
</template>

<style scoped>

.project-page {
  width: 100%;
}
.project-header {
  margin-top: 2em;
  margin-bottom: .5em;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
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
  overflow-wrap: break-word;
  max-width: 90vw;
  margin: auto;
  margin-bottom: 1em;
}

.tags {
  margin: .5em;
}

.project-image {
  margin-top: 1em;
  width: calc(100% + 4rem); /* Set the width to 100% plus the padding */
  margin-left: -2rem; /* Center the image */
  object-fit: cover;
  max-height: 50vh;
  object-position: center;
  overflow: hidden;
}
.project-content {
  margin: auto;
  margin-top: 2em;
  width: 90%;
  max-width: 800px; /* Added a max-width to prevent the content from becoming too wide on large screens */
  overflow-wrap: break-word;
}

</style>