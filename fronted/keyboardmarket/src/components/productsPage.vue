<template>
    <html lang="zh-Hant-TW">
        <link rel="icon" type="image/x-con" href="@/assets/favicon.ico" />
        <div id="app">
            <HeadLogoComponent></HeadLogoComponent>
            <b-container id="products" fluid="lg" class="container-fluid">
                <b-row>
                    <b-col v-for="product in products" :key="product.id">
                        <a :href="'/#/productDetail/' + product.id"
                            ><img :src="'http://localhost:8000' + product.img" alt="" style="width: 200px; height: 200px"
                        /></a>
                        <h4 class="productTitle">{{ product.name }}</h4>
                        <h5 class="productPrice">$ {{ product.price }}</h5>
                        <div>
                            <b-button variant="info" @click="addCart(product.id)"> 加入購物車 </b-button>
                        </div>
                    </b-col>
                </b-row>
            </b-container>
            <!-- <b-row align-h="center">
                <b-col cols="2">
                    <img src="https://i.imgur.com/8C0cKLC.png" alt="" />
                </b-col>
                <b-col cols="5">
                    <b-row>
                        <h2>3C - 藍芽耳機</h2>
                    </b-row>
                    <br />
                    <b-row align-h="right">
                        <div>
                            <ul>
                                <li><span>通話必備</span></li>
                                <li><span>就。很。無線</span></li>
                                <li><span>30小時續航</span></li>
                            </ul>
                        </div>
                    </b-row>
                    <br />
                    <b-row>
                        <h3>特價 $ 299</h3>
                    </b-row>
                    <br />
                    <b-row>
                        <b-col cols="3">
                            <b-form-spinbutton v-model="value" min="0" max="10" step="0.25"></b-form-spinbutton>
                        </b-col>
                    </b-row>
                    <br />
                    <b-row>
                        <b-col cols="3">
                            <b-button variant="info" @click="addCart(product.id)">加入購物車</b-button>
                        </b-col>
                    </b-row>
                </b-col>
            </b-row> -->
        </div>
    </html>
</template>
<script>
import { getcproduct } from "@/apis/product.js"
import { STATUS_OK } from "@/apis/constant.js"
import { addCartData } from "@/apis/car"
export default {
    name: "productsPage",
    components: {
        HeadLogoComponent: () => import("@/components/HeadLogo.vue"),
    },
    data() {
        return {
            isLogin: false,
            products: [],
        }
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
    },
    created() {
        var cid = this.$route.params.cid
        getcproduct(cid).then((response) => {
            if (response.data.code == STATUS_OK) {
                this.products = response.data.data
            } else {
                this.$fire({ type: "error", text: response.data.data })
            }
        })
    },
}
</script>
