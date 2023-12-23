import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

/*
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
*/
// Based on this, build the store for projects
export const useProjectsStore = defineStore('projects', () => {
    const projects = ref([])
    const tags = ref([])
    const tags_id_set = new Set<number>()

    function loadProjects() {
        // Fetch data from API
        try {
            // First get the page of projects
            const projects_build = (await axios.get(`${import.meta.env.VITE_APP_API_BASE_URL}/projects/?format=json`)).data;
            asignTags();
            loadTags();
            mapTags();
            projects.value = projects_build;
        } catch (error) {
            console.error(error);
        }
    }

    function asignTags(){
        projects.value.forEach((project: Project) => {
            project.tags.forEach((tag_id: number) => {
              tags_id_set.add(tag_id);
            });
          });
    }

    function loadTags(){
        // Then get the set of tags id related to theses projects
        projects.value.forEach((project: Project) => {
            project.tags.forEach((tag_id: number) => {
              tags_id_set.add(tag_id);
            });
          });
    }

    function mapTags(){
        // Then get the set of tags related to theses projects
        const tags_id_list = Array.from(tags_id_set);
        if (tags_id_list.length !== 0) {
          const tags: Tag[] = (await axios.get(`${import.meta.env.VITE_APP_API_BASE_URL}/tags/?format=json&ids=${tags_id_list.join(',')}`)).data;
    
          // Map the tags to the projects
          projects.value.forEach((project: Project) => {
            project.tags = project.tags.map((tag_id: number) => {
              return tags.find((tag: Tag) => tag.id === tag_id);
            });
          });
        }
    }

    function loadProjectDetails(handle: string){
        // Fetch data from API
        try {
            // First get the page of projects
            const project = (await axios.get(`${import.meta.env.VITE_APP_API_BASE_URL}/projects/${handle}/?format=json`)).data;
            const f_project = projects.value.find((project: Project) => project.handle === handle);
            if(f_project){
                f_project.content = project.content;
            }else{
                projects.value.push(project);
            }
        } catch (error) {
            console.error(error);
        }
    }

    return { projects, tags, loadProjects, asignTags, loadTags, mapTags }
})