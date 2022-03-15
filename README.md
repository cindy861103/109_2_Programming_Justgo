# :taxi: PROGRAMMING(II)_2021(109-2)
> * **課程名稱：**【BDM11101】程式設計（二）PROGRAMMING(II)
> * **指導老師：** **_金凱儀老師、陳宏仁老師_**

## :bulb: 程式設計【第三組】期末專題
> * **專案名稱：** 【JustGo 揪車GO】 
> * **成員簡介**
>
> | 組員  |  系級  |專題職位|
> | :------: |  :--------:  | :-----: |
> | 劉語萱 | 巨資一A | Art Designer、Associate Engineer、Line Bot Designer|
> | 陳柏尹 | 巨資一A | Associate Engineer、Web Designer|
> | 廖曉珺 | 巨資一A | Main System Engineer|
> | 洪鈺姍 | 企延B | Planner、System Engineer、Database Engineer |
> | 柳映萱 | 巨資三A | System Engineer|
> * **創作理念：**  
>   * 痛點：  
>       1. 雖有多班公車可至東吳外雙溪校區，但下車地點至校園仍有段不算近的路程。  
>       2. 部分教學大樓位於山腰，557或專車最多也只開到校內1樓平地，若要至除了校門口附近幾棟外的大樓仍需耗費一段腳程。  
>       3. 校內的綜合大樓僅有的一部電梯，一旦臨近上課時間排隊人潮便會暴增，對於趕時間或行動較為不便的學生而言，簡直就是一大噩夢。  
>       4. 若以計程車作為接駁工具，能直接駛進山腰上的目標大樓，但對一般的學生而言，此選擇的負擔較大。
>   * 預期達到解決痛點的效益：  
> 　　士林捷運站至東吳雙溪的車資大約落在NT$100～140左右，倘若可以多召集一些擁有相同目的地的學生們一起共乘，不但可以減低個人負擔，也能讓社會資源達到更有效的利用。
>
> * **主要構想與施行目的：**  
>   * **用較低的時間與金錢成本擁有較高的生活品質**：  
>製作一個供東吳學生使用的P2P平台，匹配具有相同目的地的學生。
>   * **確保基本的搭乘安全**：  
> 使用者可以利用看板公告的功能查看即時的共乘需求，加入共乘後可知道發起人與計程車的相關訊息。
>   * **顯示在刊登頁面上以提高他人的匹配意願**：  
行程結束後會自動增加1點信用值，而信用值高低可以顯示使用者的搭乘優良誠信程度。

### :star2:【JustGo 揪車GO】專案成果
> * Logo：**_加賴共乘 相付相乘_**    
> ![JustGo_Logo](./picture/JustGo_Logo.png)
> * 網頁佈告欄  
> 　　建構即時刊登的下拉式單頁網頁，顯示即時的發起、共乘訂單 資訊與個人的乘車歷史紀錄三個摺疊的表單、並將教學影片的連結、簡易Q&A問答以及平臺聯絡方式皆置於網頁底部。
>
> * 介面設計流程架構  
> 　以LinBot上的介面按鈕為設計架構，分為以下六大主要功能。   
>   * **會員**：註冊、更改資料、查看信用值。
>   * **即時資訊**：即時刊登資訊、查看歷史記錄。
>   * **我要揪車【發起】**：一定要揪車、湊滿人才揪車。
>   * **尋找共乘【共乘】**：一定要揪車、湊滿人才揪車。
>   * **揪車情況/取消揪車**：揪車現況、取消揪車、查看狀態。
>   * **使用說明/QA/其他**：使用說明、基本QA問答、其他聯絡資訊，並整合至網頁上。
> 
> * Code
>   
> | 項目 | 說明 |   
> | :-----: | :-------- |
> |[app](./JustGo_Code/app.py)|LineBot與功能系統相關訊息處理的主要檔案|
> |[answer](./JustGo_Code/answer.py)|查看共乘的訂單狀態|
> |[db_action](./JustGo_Code/db_actions.py)|跟雲端資料庫PostgreSQL互動的資料庫指令|
> |[line_save](./JustGo_Code/line_save.py)|共乘系統以及跑單處理|
> |[member](./JustGo_Code/member.py)|連接Database與初始設定CRUD，並架構會員所有系統功能|
> |[new_button](./JustGo_Code/new_button.py)|揪車與共乘的LineBot按鈕設計| 
> |[ride](./JustGo_Code/ride.py)|發起功能架構以及偵測棄單與否|
> |[db_create_table](./JustGo_Code/db_create_table.ipynb)|初始化PostgreSQL的資料庫欄位，並預先存入假想數據|
> |[publish_web](./JustGo_Code/pulish_web)|建構獨立的即時刊登的下拉式單頁網頁(Flask)| 
> 
> * Report
> 
> | 成果 | 說明 |   
> | :-----: | :-------- |
> |[PPT](./report/JustGo_PPT.pdf)|揪車GO(JustGo)的期末專題簡報|
> |[專案企劃書](./report/JustGo_共乘系統企畫書.pdf)|揪車GO(JustGo)的期末專題完整企畫書【書面報告】| 
> |[LineBot使用教學](https://youtu.be/bHd_7tuHBwI)|完整使用揪車Go(JustGo)平臺服務的示範(Demo)影片|
> |[期末專題匯報](https://youtu.be/m1Go8lC0oR0)|預錄的期末專題匯報簡報影片|
