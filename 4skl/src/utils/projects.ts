import axios from 'axios';
import type { Project, ProjectNumberTags, Tag} from '@/types';

export async function projectsNumberTagsToProjects(projects_number_tags: ProjectNumberTags[]): Promise<Project[]> {
    const projects: Project[] = [];
    let tags: Tag[] = [];
    const tags_id_set = new Set<number>();
    projects_number_tags.forEach((project_number_tags) => {
      project_number_tags.tags.forEach((tag_id) => {
        tags_id_set.add(tag_id);
      });
    });
    const tags_id_list = Array.from(tags_id_set);
    if (tags_id_list.length !== 0) {
      const tags_id_string = tags_id_list.join(',');
      tags = (await axios.get(`${import.meta.env.VITE_APP_API_BASE_URL}/tags/?format=json&ids=${tags_id_string}`)).data as Tag[];
    }
  
    projects_number_tags.forEach((project_number_tags) => {
      const project: Project = {
        handle: project_number_tags.handle,
        title: project_number_tags.title,
        description: project_number_tags.description,
        content: project_number_tags.content,
        image: project_number_tags.image,
        url: project_number_tags.url,
        git: project_number_tags.git,
        tags: tags.filter((tag) => project_number_tags.tags.includes(tag.id)),
        featured: project_number_tags.featured,
        date_created: project_number_tags.date_created,
        date_updated: project_number_tags.date_updated,
      };
      projects.push(project);
    });
  
    return projects;
  }