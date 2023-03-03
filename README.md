這是一個簡單的作品集-購物車系統
## 1.環境依賴及目錄
```
│  manage.py
│  README.md
│  requirements.txt
│      
├─backed
│  └─keyboardmarket
│      ├─keyboardmarket
│      ├─login                      	#登入功能
│      ├─media                      	#django後台圖片、個人資料圖片
│      ├─paypalTools  		   	        #結帳功能
│      ├─product                    	#產品功能
│      ├─resetPWD                   	#重設密碼功能
│      ├─templates                  	#模板
│      │  ├─orders
│      │  │      createorder.html  	    #訂單成立郵件模板
│      │  │      
│      │  └─reset
│      │          resetpassword.html 	#重設密碼郵件模板
│      │          
│      ├─tools
│      ├─usercart                   	#購物車功能
│      ├─userorder                  	#用戶下訂單功能
│      └─users                      	#用戶功能
└─fronted
    └─keyboardmarket              
        ├─public
        └─src
            │  App.vue
            │  main.js 
            ├─apis  				    #連接後端的api      
            ├─assets 
            ├─components
            │      createOrder.vue		#創建訂單
            │      createResetPage.vue	#重置密碼頁面
            │      favoritePage.vue	    #按讚頁面
            │      HeadLogo.vue		    #導覽列頁面
            │      HelloWorld.vue               
            │      indexPage.vue		#首頁
            │      loginPage.vue		#登入頁面
            │      orderCanceled.vue	#付款取消
            │      orderCreated.vue	    #付款成功
            │      orderDetail.vue		#訂單詳情頁面
            │      orderPage.vue		#訂單
            │      productDetail.vue	#商品詳情頁面
            │      productsPage.vue	    #分類商品頁面
            │      registerPage.vue	    #註冊頁面
            │      resetPage.vue		#修改密碼頁面
            │      selfPage.vue		    #個人頁面
            │      
            └─router				    #路由設定
```                 
<使用 pyhton 3.10.6 環境 django 3.1.5 網站架構 Mysql資料庫
## 2.框架、資料庫及上傳網站
## 使用Python-Django框架、Mysql資料庫
## 3.作品簡單描述
## 1.會員系統：
## 使用的是Mysql資料庫(sql)儲存檔案。 你可以在其中使用登入、註冊、修改個人資料、重設密碼功能。
### 步驟一：點選註冊，輸入基本資料後即可註冊

![](https://user-images.githubusercontent.com/114495866/222632855-addb7556-d0aa-4857-8d6f-5534fa4d2abf.png)
<img width="958" alt="image" src="https://user-images.githubusercontent.com/114495866/222632855-addb7556-d0aa-4857-8d6f-5534fa4d2abf.png">
<h3>步驟二：點選會員登入
<img width="960" alt="image" src="https://user-images.githubusercontent.com/114495866/222631849-53ff0e96-33e7-4193-bcdc-4c23eaebc8c7.png">
<h3>步驟三: 在個人資料頁面修改自己的會員資訊:大頭照、用戶名稱、地址。
<img width="960" alt="image" src="https://user-images.githubusercontent.com/114495866/222631946-552535f6-1882-4fe6-9cae-f67d562d2cd2.png">
<h3>步驟四：點選登出，可再次重新登入
<h3>步驟五:重設密碼，並收到信件
<img width="960" alt="image" src="https://user-images.githubusercontent.com/114495866/222690847-e4259ca4-7672-436c-99b3-8a66ef5fc394.png">
<h3>2.加入購物車、結帳系統
<h3>步驟一、點選加入購物車 
從商品頁面中點選喜歡商品加入購物車：
<img width="960" alt="image" src="https://user-images.githubusercontent.com/114495866/222632022-5f5f41e6-07ce-4de5-afcb-748496c92e8f.png">
<h3>步驟二、點選導覽列購物車圖案可查看商品是否已加入購物車
<img width="960" alt="image" src="https://user-images.githubusercontent.com/114495866/222632210-b0c80c8b-99fb-479f-87ce-266758a73dc9.png">
<h3>步驟三、結帳頁面，修改、刪除商品、確認結帳功能
<img width="956" alt="image" src="https://user-images.githubusercontent.com/114495866/222632280-9a10b154-b758-4819-99d7-ba10f70dfd5b.png">
<h3>步驟四、導到付款頁面
<img width="904" alt="image" src="https://user-images.githubusercontent.com/114495866/222582298-834b78cd-3c22-4fdb-aac0-44553bab9650.png">
<h3>步驟五、結帳成功畫面
<img width="916" alt="image" src="https://user-images.githubusercontent.com/114495866/222583009-a495c7f6-2fcd-4407-bd91-3927ad2b81ed.png">
<h3>步驟六、收到訂購成功的信件
<h3>3.查詢訂單
<h3>步驟一、點選訂單
<img width="907" alt="image" src="https://user-images.githubusercontent.com/114495866/222583560-ee4a2b05-d99a-4513-8210-e2f8b2ea4b8e.png">
<h3>步驟二、可依照條件搜尋
<img width="584" alt="image" src="https://user-images.githubusercontent.com/114495866/222706186-8289556f-59c7-412f-8f77-1bc8f322b6ad.png">
<h3>步驟三、點選前往詳情，可查看已購買的訂單資訊
<img width="919" alt="image" src="https://user-images.githubusercontent.com/114495866/222583809-ccddf962-27f6-4462-be7e-8b8efcacf3ab.png">
<h3>4.分享及按讚商品
<img width="919" alt="image" src="https://user-images.githubusercontent.com/114495866/222584493-e51c01d2-9e25-4b6a-9e4c-f7f65c028e80.png">
<h3>到收藏頁面查看按讚內容
<img width="923" alt="image" src="https://user-images.githubusercontent.com/114495866/222584625-5988e8cb-2b7e-4abc-864f-277ed64307e3.png">
