這是一個簡單的作品集-購物車系統
## 1.環境依賴及目錄
 使用 pyhton 3.10.6 環境 django 3.1.5 網站架構 Mysql資料庫
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
## 2.框架、資料庫及上傳網站
 使用Python-Django框架、Mysql資料庫
## 3.作品簡單描述
### 1.會員系統：
 使用Mysql資料庫(sql)儲存檔案。 你可以在其中使用登入、註冊、修改個人資料、重設密碼功能。
 
 步驟一：點選註冊，輸入基本資料後即可註冊

<img width="960" alt="image" src="https://user-images.githubusercontent.com/114495866/222881375-0fc4f5fa-7b57-4814-af91-b35a87c026f0.png">

 步驟二：點選會員登入

<img width="960" alt="image" src="https://user-images.githubusercontent.com/114495866/222881628-e7b1c276-72e4-48e4-990d-56a55da4c250.png">

步驟三: 在個人資料頁面修改會員資訊:大頭照、用戶名稱、地址

<img width="959" alt="image" src="https://user-images.githubusercontent.com/114495866/222881425-12ca75d1-fa32-4e60-9afe-4eb1c3ae3b5e.png">

步驟四：點選登出，可再次重新登入

步驟五：重設密碼，並收到通知信

<img width="960" alt="image" src="https://user-images.githubusercontent.com/114495866/222881650-d1841e75-7a89-4a80-b2a2-d375046def4c.png">

### 2.加入購物車、結帳系統

步驟一：加入購物車

從商品頁面中點選喜歡商品加入購物車

<img width="960" alt="image" src="https://user-images.githubusercontent.com/114495866/222881238-0f1257c9-4474-4246-84c8-beaf38e51b20.png">

步驟二：點選購物車圖示查看購物車裡的商品

<img width="952" alt="image" src="https://user-images.githubusercontent.com/114495866/222881832-c8c33934-cfcd-48c6-974e-2a1e81e9d741.png">

步驟三：結帳頁面，修改、刪除商品、確認結帳功能

<img width="959" alt="image" src="https://user-images.githubusercontent.com/114495866/222881856-1dd4af0f-11cc-4b60-8870-fe4bb3a8db76.png">

步驟四：導到付款頁面

<img width="960" alt="image" src="https://user-images.githubusercontent.com/114495866/222881926-bffb3955-a05f-47ee-a250-57f1f77e48db.png">

步驟五：結帳成功畫面

<img width="959" alt="image" src="https://user-images.githubusercontent.com/114495866/222881945-d814b90f-cc6a-465e-be74-6ae56262206a.png">

步驟六：收到訂單建立成功的通知信 

<img width="925" alt="image" src="https://user-images.githubusercontent.com/114495866/222882308-b5f0985b-4685-4ee8-87c3-80151eef25aa.png">

### 3.查詢訂單
步驟一：搜尋訂單編號、依條件搜尋

<img width="956" alt="image" src="https://user-images.githubusercontent.com/114495866/222882347-543b102b-3529-4251-ba1e-a7a98e0d1461.png">

步驟二：點選前往詳情，可查看已購買的訂單資訊

<img width="957" alt="image" src="https://user-images.githubusercontent.com/114495866/222882458-0c136592-1294-4878-9484-1780392c8f16.png">

### 4.分享及按讚商品
步驟一：點選FB、LINE即可分享到社群、按讚功能鍵

<img width="958" alt="image" src="https://user-images.githubusercontent.com/114495866/222882515-8627315b-2828-423c-9b4f-0ac30c20cf2d.png">

步驟二：按讚好物頁面查看按讚商品

<img width="954" alt="image" src="https://user-images.githubusercontent.com/114495866/222882553-cebed7f6-ea2d-460e-90c9-2c5d5527ad2d.png">
