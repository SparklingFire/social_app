<template>
    <form @submit.prevent="Login" method="POST">
        <input v-model="login">
        <input v-model="password">
           <button type="submit" class="btn btn-primary">Войти</button>
        </form>
</template>

<script>
    export default{
        data(){return{login: '',
                      password: ''}
        },
        methods:{
            Login(){
                this.$http.post('http://127.0.0.1:8000/login/', {'login': this.login, 'password': this.password})
            }
        }
    }
</script>
