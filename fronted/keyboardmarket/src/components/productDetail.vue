<template>
    <html lang="zh-Hant-TW">
        <link rel="icon" type="image/x-con" href="@/assets/favicon.ico" />
        <div id="app">
            <HeadLogoComponent></HeadLogoComponent>
            <b-container>
                <b-row align-h="center">
                    <b-col cols="5">
                        <img :src="'http://localhost:8000' + item.img" alt="" style="width: 200px; height: 200px" />
                    </b-col>
                    <b-row>
                      <h2>{{ item.name }}</h2>
                      <h4>{{ item.info}}</h4>
                    </b-row>
                </b-row>
                <br />
                <b-row>
                  <b-col cols="3">
                        <ShareNetwork
                        network="facebook"
                        :url="'http://127.0.0.1:8080/#/productDetail/' + item.id"
                        :quote="'幸運咖啡館 ' + item.name "
                        :hashtags="'來杯美味咖啡吧' + item.name"
                        >
                          <img src="@/assets/fb分享.jpg" style="width:60px;height: 35px;" alt="">
                        </ShareNetwork>
                  </b-col>
                  <b-col cols="3">
                    <ShareNetwork
                    network="Line"
                    :url="'http://127.0.0.1:8080/#/productDetail/' + item.id"
                    :title="'幸運咖啡館'+ item.name"
                    :description="'來杯美味咖啡吧'+item.name "
                    >
                      <img src="@/assets/line分享.jpg" alt="" style="width: 60px;height: 35px;">
                    </ShareNetwork>
                  </b-col>
                </b-row> 
                <br/>       
                <b-row>
                    <h3>${{ item.price }}</h3>
                </b-row>
                <b-row>
                    <b-col cols="5">
                        <b-form-spinbutton v-model="amount" min="1" :max="item.stored_amount"></b-form-spinbutton>
                    </b-col>
                    <b-col cols="3">
                        <span style="color: red">剩餘數量: {{ item.stored_amount }}</span>
                    </b-col>
                </b-row>
                <br />
                <b-row>
                    <b-col cols="3">
                        <b-button variant="info" @click="addCart">加入購物車</b-button>
                    </b-col>
                    <b-col cols="3">
                        <b-button variant="info" @click="addToFavorite">
                          {{ favoriteText }}
                        </b-button>
                    </b-col>
                </b-row>
            </b-container>
        </div>
    </html>
</template>
<script>
import { getDetail } from "@/apis/product"
import { getProductFavorite,addFavorite } from '@/apis/favorite.js'
import { STATUS_OK } from "@/apis/constant"
import { addCartData } from "@/apis/car"
export default {
    name: "productDetail",
    components: {
        HeadLogoComponent: () => import("@/components/HeadLogo.vue"),
    },
    data() {
        return {
            isLogin: false,
            amount: 1,
            item: {},
            favoriteText:""
        }
    },
    methods:{
      addToFavorite(){
        var pid = this.$route.params.pid
        var username = window.localStorage.getItem("username")
        var token = window.localStorage.getItem("token")
        if(username == null || token == null){
          this.$fire({type:"error",text:"請登入!"}).then(() => {
            location.href = "/#/login"
          })
        }else{
          addFavorite(pid,token,username).then((response) => {
            if(response.data.code == STATUS_OK){
              this.favoriteText = response.data.data.status == 0 ? "按讚" : "已按讚"
            }
          })
        }
      },
      addCart(){
        var username = window.localStorage.getItem("username")
        var token = window.localStorage.getItem("token")
        if(username != null && token != null){
          var data = {
            "pid":this.item.id,
            "amount":this.amount,
            "username":username
          }
          addCartData(data,token).then((response) => {
            if(response.data.code == STATUS_OK){
              this.$fire({type:"success","text":"加入購物車成功!"})
            }else{
              this.$fire({type:"error","text":response.data.data})
            }
          })
        }else{
          this.$fire({type:"error",text:"請登入!"}).then(() => {
            window.location.href = "/#/login"
            window.location.reload()
          })
        }
      }
    },
    created(){
      var pid = this.$route.params.pid
      getDetail(pid).then((response) => {
        if(response.data.code == STATUS_OK){
          this.item = response.data.data
          var token = window.localStorage.getItem("token")
          var username = window.localStorage.getItem("username")
          if(token == null || username == null){
            this.favoriteText = "登入以按讚"
          }else{
            getProductFavorite(pid,token,username).then((response) => {
              if(response.data.code == STATUS_OK){
                var status = response.data.data.status
                this.favoriteText = status == 0 ? "按讚" : "已按讚" 
              }
            })
          }
        }
        else{
          this.$fire({type:'error',text:response.data.data}).then(() => {
            window.location.href = "/#/"
            window.location.reload
          })
        }
      })
    }
  }
</script>
