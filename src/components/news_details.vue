<template>
    <div class="news_details">
        <div class="panel panel-default">
            <div class="panel-heading">
                {{post.title}}
            </div>
            <div class="panel-body">
                {{post.text}}
            </div>
            <div class="panel-footer"></div>
        </div>
        <div v-if="loading">loading</div>
        <ul class="comments-list">
            <li v-for="item in post.comments_data">
                <p>{{item.author}}</p>
                <p>{{item.text}}</p>
            </li>
        </ul>
        <form @submit.prevent="leaveComment" method="POST">
          <input v-model="comment">
           <button type="submit" class="btn btn-primary">Оставить комментарий</button>
        </form>
    </div>
</template>

<script>
    export default{
        data(){
            return{
                loading: false,
                post:[],
                curr_url: 'http://127.0.0.1:8000' + window.location.pathname + '/',
                comment: '',
            }
        },
        created(){
            this.fetchData();
        },
        watch: {
            '$route': 'fetchData'
        },

        beforeRouteEnter (to, from, next) {
            next(vm => {vm.fetchData()})
        },
        methods:{
            fetchData(){
                this.loading = true;
                this.$http.get(this.curr_url).then(response => {this.post = response.body;});
                this.loading = false;
            },
            leaveComment(){
                this.loading = true;
                this.$http.post(this.curr_url, this.comment).then(
                    refresh => {this.fetchData();
                                this.comment=''}, error => {});
                this.loading = false;
            },
        }
    }
</script>

<style>

</style>
