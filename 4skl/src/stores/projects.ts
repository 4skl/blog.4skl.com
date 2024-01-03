import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import type { Project,  ProjectNumberTags, Tag} from '@/types';
import { useTagsStore } from '@/stores/tags';
import slugify from 'slugify'
import axios from 'axios'

export const useProjectsStore = defineStore('projects', () => {
    const projects_handle = ref<Record<string, Project>>({}); // handle as key : project
    const projects_loaded = ref(false);
    
    function addProject(handle: string, project: Project) {
        projects_handle.value[handle] = project;
    }

    const projects = computed(() => {
        return Object.values(projects_handle.value);
    })

    const projects_featured = computed(() => {
        return Object.values(projects_handle.value).filter((project) => project.featured);
    })
    
    function searchProject(title: string) {
        const lowerCaseTitle = title.toLowerCase();
        return projects.value.filter(project =>
            slugify(project.title).toLowerCase().includes(lowerCaseTitle)
        );
    }

    function getProjectByHandle(handle: string) {
        return projects_handle.value[handle];
    }

    function filterProjectsByTags(tags: Tag[]) {
        // if no tags, return all projects
        if(tags.length === 0) return projects.value;
        return projects.value.filter(project => 
          tags.every(tag => project.tags.includes(tag))
        );
      }

    async function loadProjectContent(handle: string) {
        try {
            // Get tags store
            const tagsStore = useTagsStore();
            await tagsStore.loadTags();
            // Get the project
            const project_build: ProjectNumberTags = (await axios.get(`${import.meta.env.VITE_APP_API_BASE_URL}/projects/${handle}/?format=json`)).data as ProjectNumberTags;
            const project: Project = {
                handle: project_build.handle,
                title: project_build.title,
                description: project_build.description,
                content: project_build.content,
                image: project_build.image,
                url: project_build.url,
                git: project_build.git,
                tags: project_build.tags.map((tag_id) => tagsStore.getTagId(tag_id)),
                featured: project_build.featured,
                date_created: project_build.date_created,
                date_updated: project_build.date_updated,
              };
            addProject(project.handle, project);
        } catch (error) {
            console.error('Error:', error);
        }
    }

    async function loadProjects() {
        if(projects_loaded.value) return;
        try {
            // Get tags store
            const tagsStore = useTagsStore();
            await tagsStore.loadTags();
            // Get the list of projects
            const projects_build: ProjectNumberTags[] = (await axios.get(`${import.meta.env.VITE_APP_API_BASE_URL}/projects/?format=json`)).data as ProjectNumberTags[];
            for (const project_build of projects_build) {
                const project: Project = {
                    handle: project_build.handle,
                    title: project_build.title,
                    description: project_build.description,
                    content: project_build.content,
                    image: project_build.image,
                    url: project_build.url,
                    git: project_build.git,
                    tags: project_build.tags.map((tag_id) => tagsStore.getTagId(tag_id)),
                    featured: project_build.featured,
                    date_created: project_build.date_created,
                    date_updated: project_build.date_updated,
                  };
                addProject(project.handle, project);
            }
            projects_loaded.value = true;
        } catch (error) {
            console.error('Error:', error);
        }
    }

    return {projects, projects_featured, filterProjectsByTags, getProjectByHandle, loadProjects, loadProjectContent, searchProject}
})

