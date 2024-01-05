<script setup lang="ts">
import { withDefaults } from 'vue';
import type { Tag } from '@/types';
const props = withDefaults(defineProps<{
  tag: Tag;
  selected?: boolean;
}>(), {
  selected: false
});


const emit = defineEmits(['toggle-tag']);

const toggleTag = () => {
  emit('toggle-tag', props.tag);
};
</script>

<template>
  <span class="tag" :class="{ 'selected': props.selected }" :title="tag.description" :style="{ borderColor: tag.color }" @click="toggleTag">{{ tag.name }}</span>
</template>

<style scoped>
.tag {
  display: inline-block;
  padding: 0.15rem 0.4rem;
  border-radius: 0.5rem;
  border: 2px solid;
  font-size: 0.8rem;
  font-weight: 500;
  margin-right: 0.5rem;
  width: fit-content;
}

.tag.selected {
  background-color: var(--color-border);
}
</style>