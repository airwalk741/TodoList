<template>
  <div class="hello">

    
    <h1>TodoList</h1>
    <div class="d-flex">
      <TodoCreate />
    </div>
   
    <div class="container">
      <div class="d-flex row">
        <div v-for="todo in todoList" :key="todo.id" class="col-3">
          <TodoItem :todo="todo" />
          <hr>
        </div>
      </div>
    </div>

  </div>
</template>

<script>

import TodoItem from '@/components/Todo/TodoItem.vue'
import TodoCreate from '@/components/Todo/TodoCreate.vue'


export default {
  name: 'TodoList',
  components: {
    TodoItem,
    TodoCreate,
  },
  data: function () {
    return {
      title: '',
      content: '',
      todoList: []
    }
  },
  props: {
  
  },

  created: async function () {
    this.todoList = this.$store.state.todoList
  },

  methods: {
    
  }

}
</script>

<style>

h1 {
  margin: 4rem 0rem 3rem 0rem;
}

#insert {
  margin-left: auto;
  margin-right: 5rem;
  margin-bottom: 2.5rem;
}


</style>

