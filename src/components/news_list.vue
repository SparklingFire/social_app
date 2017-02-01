<template>
    <ul id="news">
        <li v-for="item in news_list">
            <div class="panel panel-default">
                <div class="panel-heading">{{ item.title}}</div>
                <div class="panel-body">{{item.text}}</div>
                <div class="panel-footer">
                    <router-link v-bind:to="'/news/' + item.primary_key">Comments:{{item.comments.length}}</router-link>
                </div>
            </div>
        </li>
    </ul>
</template>


<script>
  export default{
      data(){
          return {
              loading: false,
              news_list: [],
              }
      },
      created(){
          this.fetchData()
      },
      methods:{
          fetchData(){
              this.loading = true;
              this.$http.get('http://127.0.0.1:8000/news/').then(response => this.news_list = response.data);
              this.loading = false;
          }
      }
  }
</script>

<style>
    ul{
        list-style-type: none;
    }
</style>
