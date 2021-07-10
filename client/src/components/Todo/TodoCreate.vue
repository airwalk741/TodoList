<template>
  <div  id="insert">
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
      추가하기
    </button>

    <!-- Modal -->
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
          <div class="modal-content">
            <div class="modal-header">
              <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
              <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form>
                  <input type="text" v-model="title" ><br>
                  <textarea name="" id="" cols="30" rows="10" v-model="content"></textarea>
                </form>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              <button type="button" class="btn btn-primary"  @click="inputTodo">등록</button>
            </div>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
const url = process.env.VUE_APP_URL


export default {

  name: 'TodoCreate',

  data: function () {
    return {
      title: '',
      content: '',
      modal: ''
    }
  },

  methods: {
    inputTodo: async function (event) {
      console.log(url)
      event.preventDefault()
      const title = this.title
      const content = this.content

      const response = await axios({
        url: `${url}/articles/`,
        method: 'POST',
        data: {
          title: title,
          content: content,
        },
      })

      this.$store.dispatch('todoCreate', response)
      
    }
  }
}
</script>

<style>

</style>