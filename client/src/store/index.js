import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todoList: []

  },
  mutations: {
    TODOLIST: function (state, todos) {
      state.todoList = todos
    },
    TODOCREATE: function (state, todo) {
      state.todoList += [todo]
      console.log(state.todoList)
    }
  },
  actions: {
    todoList: function ({ commit }, todos) {
      commit('TODOLIST', todos)
    },
    todoCreate: function ({ commit }, todo) {
      commit('TODOCREATE', todo)
    }
  },
  plugins: [
    createPersistedState()
  ],

})
