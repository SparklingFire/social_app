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
        <ul class="comments-list">
            <li v-for="item in post.comments">
                {{item.parent}}
                {{item.text}}
            </li>
        </ul>
    </div>
</template>

<script>
    export default{
        data(){
            return{
                loading:false,
                post:[],
            }
        },
        created(){
            this.fetchData();
        },
        methods:{
            fetchData(){
                let curr_url = 'http://127.0.0.1:8000' + window.location.pathname;
                this.$http.get(curr_url).then(response => this.post = response.body);
            }
        }
    }
</script>
