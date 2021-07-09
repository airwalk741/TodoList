import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todoList: []

  },
  mutations: {
    TODOLIST: function (state, todos) {
      state.todoList = todos
    }
  },
  actions: {
    todoList: function ({ commit }, todos) {
      commit('TODOLIST', todos)
    }
  },

})
