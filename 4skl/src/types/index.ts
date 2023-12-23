export interface Tag {
    id: number;
    name: string;
    description: string;
    color: string;
}

export interface Project {
    handle: string;
    title: string;
    description: string;
    content?: string;
    image: string;
    url: string;
    git: string;
    tags: Tag[] | number[];
    featured: boolean;
    date_created: Date;
    date_updated: Date;
  }