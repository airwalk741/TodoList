<template>
  <div>
    title : {{ todo.title }}
  </div>
</template>

<script>
export default {
  name: 'TodoItem',

  data: function () {
    return {
      title: '',
      content: ''
    }
  },

  props: {
    todo: {
      type: Object,
      required: true
    }
  },

}
</script>

