<template>
  <div id="app">
    <NavBar />
    <router-view/>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import axios from 'axios'
const url = process.env.VUE_APP_URL

export default {
  components: {
    NavBar
  },
  created: async function () {

    const res = await axios({
      url: `${url}/articles/`,
      method: 'GET',
    })

    this.$store.dispatch('todoList', res.data)
    
  },
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}


</style>
