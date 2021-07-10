<template>
  <nav id="nav" class="navbar navbar-expand-lg navbar-light bg-light" style="padding: 1rem">
    <div class="container-fluid">
      <router-link class="me-3" to="/" id="router" >Home</router-link>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <router-link to="/TodoList"  id="router">TodoList</router-link> 
        </ul>
        <form class="d-flex">
          <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
          <button class="btn btn-outline-success" type="submit">Search</button>
        </form>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavBar'
}
</script>

<style>

#nav a.router-link-exact-active {
  color: #42b983;
  
}

#router {
  text-decoration: none;
}


</style>