<template>
    <div class="row">
        <div v-if="loading">loading</div>
        <ul id="news">
            <li v-for="item in news_list">
                <div class="panel panel-default">
                    <div class="panel-heading">{{ item.title}}</div>
                    <div class="panel-body">{{item.text}}</div>
                    <div class="panel-footer">
                        <router-link v-bind:to="'/news/' + item.primary_key">Comments: {{item.comments_data.length}}
                        </router-link>
                    </div>
                </div>
            </li>
        </ul>
    </div>
</template>


<script>
  export default{
      data(){
          return {
              loading: false,
              news_list: []
              }
      },
      beforeRouteEnter (to, from, next) {
          next(vm => {
              vm.loading = true;
              vm.$http.get('http://127.0.0.1:8000/news/').then(response => vm.news_list = response.data);
              vm.loading = false;})
      },
  }
</script>

<style>
    ul{
        padding: 0;
        list-style-type: none;
    }
</style>
