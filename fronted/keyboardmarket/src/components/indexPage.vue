<template>
    <html lang="zh-Hant-TW">
        <link rel="icon" type="image/x-con" href="@/assets/favicon.ico" />
        <div id="app">
            <HeadLogoComponent></HeadLogoComponent>
            <div>
                <img src="@/assets/咖啡首頁.jpg" style="display:block; margin:auto;" /> 
                <img src="@/assets/咖啡首頁2.jpg" style="display:block; margin:auto;" /><br>
            </div>
            <b-container id="products" fluid="lg" class="container-fluid">
                <b-row>
                    <b-col v-for="product in products" :key="product.id">
                        <a :href="'/#/productDetail/' + product.id">
                            <img :src="'http://localhost:8000' + product.img" alt="" style="width: 200px; height: 200px" />
                        </a>
                        <h4 class="productTitle">{{ product.name }}</h4>
                        <h5 class="productPrice">$ {{ product.price }}</h5>
                        <div>
                            <b-button variant="info" @click="addCart(product.id)"> 加入購物車 </b-button>
                        </div>
                    </b-col>
                </b-row>
            </b-container>
        </div>
    </html>
</template>
<script>
import { getallproduct } from "@/apis/product"
import { STATUS_OK } from "@/apis/constant"
import { addCartData } from "@/apis/car"
export default {
    name: "indexPage",
    components: {
        HeadLogoComponent: () => import("@/components/HeadLogo.vue"),
    },
    data() {
        return {
            slide: 0,
            sliding: null,
            isLogin: false,
            products: [],
        }
    },
    created() {
        getallproduct().then((response) => {
            if (response.data.code == STATUS_OK) {
                this.products = response.data.data
            } else {
                this.$fire({ type: "error", text: response.data.data })
            }
        })
    },

    methods: {
        addCart(product_id) {
            var username = window.localStorage.getItem("username")
            var token = window.localStorage.getItem("token")
            if (username != null && token != null) {
                var data = {
                    pid: product_id,
                    amount: 1,
                    username: username,
                }
                addCartData(data, token).then((response) => {
                    if (response.data.code == STATUS_OK) {
                        console.log(response.data)
                        this.$fire({ type: "success", text: "加入購物車成功!" })
                    } else {
                        this.$fire({ type: "error", text: response.data.data })
                    }
                })
            } else {
                this.$fire({ type: "error", text: "請登入!" }).then(() => {
                    window.location.href = "/#/login"
                    window.location.reload()
                })
            }
        },
        onSlideStart() {
            this.sliding = true
        },
        onSlideEnd() {
            this.sliding = false
        },
    },
}
</script>
