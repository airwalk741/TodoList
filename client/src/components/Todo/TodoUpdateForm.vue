<template>
  <form >
    <input type="text" v-model="title">
    <textarea name="" id="" cols="30" rows="10" v-model="content"></textarea>
    <button @click="update">수정</button>
    <button @click="updataCancel">취소</button>
  </form>
</template>

<script>
import axios from 'axios'
const url = process.env.VUE_APP_URL

export default {
  name: 'TodoUpdateForm',
  data: function () {
    return {
      title: this.todo.title,
      content: this.todo.content,
    }
  },
  props: {
    todo: {
      type: Object,
      require: true
    }
  },

  methods: {
    updataCancel: function (event) {
      event.preventDefault()
      this.todo.is_update_form = !this.todo.is_update_form
    },
    update: function (event) {
      event.preventDefault()

      axios({
        url: url + `/articles/${this.todo.id}/`,
        method: 'PUT',
        data: {
          title: this.title,
          content: this.content
        }
      })
      .then(res => {
        console.log(res)
        this.todo.is_update_form = !this.todo.is_update_form
      })
      .catch(err => {
        console.log(err)
      })

    }
  }
}
</script>

<style>

</style>