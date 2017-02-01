import Vue from 'vue'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'
import news_list from './components/news_list.vue'
import news_details from './components/news_details.vue'
Vue.use(VueResource);
Vue.use(VueRouter);


const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes:[
    {path: '/', component: news_list},
    {path: '/news/:id', component: news_details}
  ]
});


new Vue({ router,
  el: '#app',
  template: '<div class="row"><div class="col-sm-6 col-sm-offset-3 main-column"><router-view></router-view></div></div></div>'
});
