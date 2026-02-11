<template>
  <div v-html="renderedHtml"></div>
</template>

<script>
import MarkdownIt from 'markdown-it';

export default {
  props: ['markdownText'],
  data() {
    return {
      renderedHtml: ''
    };
  },
  watch: {
    markdownText: {
      immediate: true,
      handler(newMarkdown) {
        this.renderMarkdown(newMarkdown);
      }
    }
  },
  methods: {
    renderMarkdown(markdown) {
      const md = new MarkdownIt();
      this.renderedHtml = md.render(markdown);
    }
  }
}
</script>
