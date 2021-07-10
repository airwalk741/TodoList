<template>
  <div>
    <div v-if="!todo.is_update_form"> 
      <div>
        title : {{ todo.title }}
      </div>
      <button>상세보기</button>
      <button @click="articleUpdate(todo)">수정</button>
      <button @click="articleDelete">삭제</button>
    </div>
    <TodoUpdateForm v-if="todo.is_update_form" :todo="todo"/>
  </div>
</template>

<script>
import TodoUpdateForm from '@/components/TodoUpdateForm.vue'
import axios from 'axios'
const url = process.env.VUE_APP_URL

export default {
  name: 'TodoItem',
  components: {
    TodoUpdateForm
  },
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
  methods: {
    articleUpdate: function (todo) {
      todo.is_update_form = !todo.is_update_form
    },
    articleDelete: function () {
      axios({
        url: url + `/articles/${this.todo.id}/`,
        method: 'DELETE'
      })
      .then(res => {
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
    }

  }

}
</script>

