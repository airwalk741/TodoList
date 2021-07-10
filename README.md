# TodoList

> TodoLis 연습





## ✍ 새로고침 이슈



#### 😢 새로고침 하면 자꾸 TodoList의 값이 사라지는 이슈가 발생

- 새로고침하면 `vuex store`에 저장된 TodoList를 잘 받아오지 못한다.
- 알고보니 새로고침 하면 `store`에 있는 데이터가 사라진다했다.



```bash
npm install vuex-persistedstate
```

- `vuex-persistedstate` 는 `vuex`에 저장되는 값들을 웹브라우저 `localstorage`에 저장하는 것!
- 그럼 새로고침 했을 때 `localstorage`의 값을 가져와 사용한다!

- 사용하기 위해서는 사용하는 `store`의 `index.js`에  플러그인 `vuex-persistedstate` 추가하기



  ```js
  ...
  import createPersistedState from 'vuex-persistedstate'
  
  Vue.use(Vuex)
  
  export default new Vuex.Store({
    state: {
      todoList: []
    },
    ...,
    plugins: [
      createPersistedState()
    ],
  })
  ```



#### 단점

- `localstorage`에 저장하는 값이 많아지면 웹의 속도가 느려진다. ( 회사의 경우 )
- 따라서 그떄는 원하는 값만 `store`에 저장해야한다.



#### 참고 자료

- [새로고침 문제](http://blog.knowgari.com/state%EC%B4%88%EA%B8%B0%ED%99%94%EB%A7%89%EA%B8%B0/)





## 해야 할 것

- [ ]  article 추가할 시 모달이 사라지지 않음.
- [ ]  추가하고 새로고침을 해야 생성한 Todo가 보인다.
- [ ]  삭제 버튼 클릭시 Todo 삭제하기

