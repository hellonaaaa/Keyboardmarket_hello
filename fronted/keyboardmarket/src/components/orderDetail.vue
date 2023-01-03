<template>
    <html lang="zh-Hant-TW">
        <link rel="icon" type="image/x-con" href="@/assets/favicon.ico" />
        <div id="app">
            <HeadLogoComponent></HeadLogoComponent>
            <div
                id="orderHeader"
                style="
                    width: 100%;
                    height: 100px;
                    background-image: linear-gradient(to right, #c9c9c9, #f2ffff, #00e6e6);
                    padding-top: 40px;
                "
            >
                <h3>訂單詳情</h3>
            </div>
            <b-row align-h="center">
                <b-col cols="5">
                    <span>訂單編號:</span>
                    <b-form-input readonly v-model="orderno"></b-form-input>
                </b-col>
                <b-col cols="5">
                    <span>總金額:</span>
                    <b-form-input readonly v-model="orderPrice"></b-form-input>
                </b-col>
            </b-row>
            <b-row align-h="center">
                <b-col cols="8">
                    <span>收貨地址:</span>
                    <b-form-input readonly v-model="orderAddress"></b-form-input>
                </b-col>
                <b-col cols="2">
                    <span>狀態:</span>
                    <b-form-input readonly v-model="orderStatus"></b-form-input>
                </b-col>
            </b-row>
            <b-row align-h="center">
                <b-col cols="5">
                    <span>聯絡電話:</span>
                    <b-form-input readonly v-model="phone"></b-form-input>
                </b-col>
            </b-row>
            <b-table striped hover :items="products" :fields="fields"></b-table>
        </div>
    </html>
</template>
<script>
import { getDetailOrderData } from "@/apis/order.js"
import { STATUS_OK } from "@/apis/constant.js"
export default {
    name: "orderDetail",
    components: {
        HeadLogoComponent: () => import("@/components/HeadLogo.vue"),
    },
    data() {
        return {
            orderno: "0a000c",
            orderPrice: "$4,491",
            orderAddress: "新北市蘆洲區民族路448號",
            orderStatus: "未出貨",
            phone: "0977777777",
            isLogin: false,
            products: [
                {
                    name: "耳機",
                    price: 399,
                    amount: 3,
                    subtotal: 1197,
                },
                {
                    name: "鍵盤",
                    price: 499,
                    amount: 3,
                    subtotal: 1497,
                },
                {
                    name: "滑鼠",
                    price: 599,
                    amount: 3,
                    subtotal: 1797,
                },
            ],
            fields: [
                { key: "name", label: "商品名稱" },
                { key: "price", label: "價格" },
                { key: "amount", label: "數量" },
                { key: "subtotal", label: "小計" },
            ],
        }
    },
    created(){
      var username = window.localStorage.getItem("username")
      var token = window.localStorage.getItem("token")
      if(username != null && token != null){
        getDetailOrderData(username,token,this.$route.params.oid).then((response) => {
          if(response.data.code == STATUS_OK){
            this.orderno = this.$route.params.oid
            this.orderPrice = response.data.data.products.map((x) => x.subtotal).reduce((a,b) => a + b).toString()
            this.orderAddress = response.data.data.address
            this.orderStatus = response.data.data.orderStatus
            this.phone = response.data.data.phone
            this.products = response.data.data.products
          }
        })
      }
    }
  }
</script>
