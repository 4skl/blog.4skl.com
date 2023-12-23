<script setup lang="ts">
import type { Tag } from '@/types';
defineProps<{
  tag: Tag;
}>()
</script>

<template>
  <span class="tag" :title="tag.description" :style="{ borderColor: tag.color }">{{ tag.name }}</span>
</template>

<style scoped>
.tag {
  display: inline-block;
  padding: 0.2rem 0.5rem;
  border-radius: 0.5rem;
  border: 2px solid;
  font-size: 0.8rem;
  font-weight: 500;
  margin-right: 0.5rem;
  width: fit-content;
}
</style>