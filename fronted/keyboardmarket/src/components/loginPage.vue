<template>
    <html lang="zh-Hant-TW">
        <link rel="icon" type="image/x-con" href="@/assets/favicon.ico" />
        <div id="app">
            <HeadLogoComponent></HeadLogoComponent>
            <div
                id="loginHeader"
                style="
                    width: 100%;
                    height: 100px;
                    background-image: linear-gradient(to right, #c9c9c9, #f2ffff, #00e6e6);
                    padding-top: 40px;
                "
            >
                <h3>登入</h3>
            </div>
            <div id="loginForm" style="width: 50%; height: 500px">
                <b-form @submit="onSubmit" @reset="onReset" style="width: 100%">
                    <b-form-group id="username_group" label="用戶名:" label-for="username" style="margin: 10px">
                        <b-form-input id="username" placeholder="請輸入用戶名" v-model="username" required> </b-form-input>
                    </b-form-group>
                    <b-form-group id="password_group" label="密碼:" label-for="password" style="margin: 10px">
                        <b-form-input id="password" placeholder="請輸入密碼" type="password" v-model="password" required> </b-form-input>
                    </b-form-group>
                    <b-button type="submit" variant="info" style="width: 80px; margin: 10px">登入</b-button>
                    <b-button type="reset" variant="danger" style="width: 80px; margin: 10px">清空</b-button>
                    <a href="/#/createreset">忘記密碼?</a>
                </b-form>
            </div>
        </div>
    </html>
</template>
<script>
import { login } from "@/apis/users"
import { STATUS_OK } from "@/apis/constant"
export default {
    name: "loginPage",
    components: {
        HeadLogoComponent: () => import("@/components/HeadLogo.vue"),
    },
    data() {
        return {
            isLogin: false,
            username: "",
            password: "",
        }
    },
    methods: {
        onSubmit(e) {
            e.preventDefault()
            var data = {
                username: this.username,
                password: this.password,
            }
            login(data).then((response) => {
                if (response.data.code == STATUS_OK) {
                    window.localStorage.setItem("username", this.username)
                    window.localStorage.setItem("token", response.data.data.token)
                    this.$alert("登入成功").then(() => {
                        window.location.href = "/#/"
                        window.location.reload()
                    })
                } else {
                    this.$fire({ type: "error", text: response.data.data })
                }
            })
        },
        onReset() {
            this.username = this.password = ""
        },
    },
}
</script>
