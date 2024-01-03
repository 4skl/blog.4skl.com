import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import type { Tag } from '@/types';
import slugify from 'slugify'

export const useTagsStore = defineStore('tags', () => {
    const tags_id = ref<Record<number, Tag>>({}); // tag id : tag
    const tags_loaded = ref(false);

    function addTagId(id: number, tag: Tag) {
        tags_id.value[id] = tag;
    }

    const tags = computed(() => {
        return Object.values(tags_id.value);
    })

    function searchTag(name: string) {
        const lowerCaseName = name.toLowerCase();
        return tags.value.filter(tag =>
            slugify(tag.name).toLowerCase().includes(lowerCaseName)
        );
    }

    function getTagId(id: number) {
        return tags_id.value[id];
    }

    async function loadTags() {
        if(tags_loaded.value) return;
        try {
            const tags_temp = (await axios.get(`${import.meta.env.VITE_APP_API_BASE_URL}/tags/?format=json`)).data as Tag[];
            for (const tag of tags_temp) {
                addTagId(tag.id, tag);
            }
            tags_loaded.value = true;
        } catch (error) {
            console.error('Error:', error);
        }
    }

    return {tags, loadTags, searchTag, getTagId}
})

