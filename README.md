# Object-Detection-YoloV5
This repository shows how to solve 3 problems:  
1. Training YoloV5 on <a href="http://shuoyang1213.me/WIDERFACE/">Wider Train</a> dataset for video face recognition.
2. Making web-demo using interactive <a href="https://streamlit.io">Streamlit</a>.  
   I decided not to use Streamlit cloud because project is for local usage.
3. Implementing Telegram Bot which will send message if someone detected (so-called Security-Bot).
## <div align="center">Photo and video examples</div>
###  First Problem

#### Loss Functions and Metrics
<img src="https://github.com/IvanPodoynikov/Object-Detection-YoloV5/blob/main/assets/results.png" >

#### First bunch of photos
<img src="https://github.com/IvanPodoynikov/Object-Detection-YoloV5/blob/main/assets/pic_1.jpg" >

#### Second bunch of photos
<img src="https://github.com/IvanPodoynikov/Object-Detection-YoloV5/blob/main/assets/pic_2.jpg" >

### Second and Third Problem
https://github.com/IvanPodoynikov/Object-Detection-YoloV5/assets/157584243/b252210b-06a4-4bf7-aa54-b61146bc014a

## <div align="center">Documentation</div>
Get started with
```bash
pip install ultralytics
```

<details open>
<summary>Install</summary>
   
Clone repo and install requirements
```bash
git clone https://github.com/IvanPodoynikov/Object-Detection-YoloV5  # clone
cd Object-Detection-Yolov5
pip install -r requirements.txt  # install
```
</details>

<details>
<summary>Get bot</summary>

- Open <a href = "https://telegram.me/BotFather">Bot Father</a> in Telegram and type
```bash
/newbot
```
- Choose name for Your bot and username, You should get something like this. You need API key from here.  
![Bot](https://github.com/IvanPodoynikov/Object-Detection-YoloV5/assets/157584243/6e65f23f-a421-4f1c-84e0-c4fa5b3e71de)

- Open <a href = "https://t.me/RawDataBot">RawDataBot</a> in Telegram and type: "/start". 
You will get json file, You need message -> chat -> id.








