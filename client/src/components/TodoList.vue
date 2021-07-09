<template>
  <div class="hello">



    <form>
      <input type="text" v-model="title" ><br>
      <textarea name="" id="" cols="30" rows="10" v-model="content"></textarea>
      <button @click="inputTodo">등록</button>
    </form>

    <div v-for="todo in todoList" :key="todo.id">
      <TodoItem :todo="todo" />
      <hr>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
import TodoItem from '@/components/TodoItem.vue'
const url = process.env.VUE_APP_URL

export default {
  name: 'TodoList',
  components: {
    TodoItem,
  },
  data: function () {
    return {
      title: '',
      content: '',
      todoList: [],
    }
  },
  props: {
  
  },

  created: function () {

    axios({
      url: `${url}/articles/`,
      method: 'GET',
      
    })
    .then(res => {
      const todos = res.data
      this.$store.dispatch('todoList', todos)
    })
    .catch(err => {
      console.log(err)
    })

    this.todoList = this.$store.state.todoList

  },

  methods: {
    inputTodo: function (event) {

      
      console.log(url)
      event.preventDefault()
      const title = this.title
      const content = this.content

      axios({
        url: `${url}/articles/`,
        method: 'POST',
        data: {
          title: title,
          content: content,
        },

      })
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.log(err, 'asdfasdf')
      })

    }
  }

}
</script>


