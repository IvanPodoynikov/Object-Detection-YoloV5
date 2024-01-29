import streamlit as st
import torch
import os
import cv2
import sys
import telebot
from PIL import Image

# Get info from .env file
from dotenv import load_dotenv
load_dotenv()

#@st.cache_resource
#def get_token_chatid_path():
#	env_token = os.getenv("API_KEY")
#	env_chat_id = os.getenv("CHAT_ID")
#	pth = os.getenv("_PATH_")
#	return (env_token, env_chat_id, pth)
#
#token, chat_id, pth = get_token_chatid_path()

# Loading Telegram Bot
@st.cache_resource
def load_bot():
	bt = telebot.TeleBot(token)
	
	return bt 
bt = load_bot()

#Loading model
@st.cache_resource
def load_model():
	with st.spinner('Loading model'): model = torch.hub.load('ultralytics/yolov5', 'custom', path=pth)
	model.eval()
	return model
model = load_model()

# Updating amount of detections
def on_update(count):
	t.text(f'Amount of detections: {count}')

#Setting Streamlit interface
st.title("Face Detection App")
st.sidebar.title("Face Detection App") 
st.sidebar.title("Selection of camera") 
camera = st.sidebar.selectbox("From camera", ['None', 'Webcam'])
st.sidebar.text(f'{camera} is activated')
stframe = st.empty()
st.sidebar.title("Additions")
use_label = st.sidebar.checkbox('Label')
use_conf = st.sidebar.checkbox('Confidence')
amount = st.sidebar.checkbox('Count Detections')
finish = st.sidebar.button('Exit')
t = st.empty()
old_amount = -1

# Exit if "Exit" button is pressed
if finish:
	bt.send_message(chat_id, text = 'Finish Detecting')
	sys.exit(0)

if camera:
	#Making detection on Webcam
	if camera == 'Webcam':
		if amount: bt.send_message(chat_id, "Start Detecting with {}".format(camera) )

		# Start video
		cap = cv2.VideoCapture(0)
		frame_width = int(cap.get(3))
		frame_height = int(cap.get(4))

		while True:
			
			# Get frames and preprocess images to RGB format
			success, img = cap.read()
			img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

			if success:
				
				# Making predictions
				results = model(img)
				df = results.pandas().xyxy[0]
				new_amount = df.shape[0]

				# Show out image with predictions
				for ind in df.index:

					x1, y1 = int(df['xmin'][ind]), int(df['ymin'][ind])
					x2, y2 = int(df['xmax'][ind]), int(df['ymax'][ind])
					label = df['name'][ind]
					conf = "{:.2f}".format(df['confidence'][ind])

					cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
					if use_label:
						cv2.putText(img, label, (x1, y1-5), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
					if use_conf:
						cv2.putText(img, conf, (x2, y1-5), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
				
				# If number of detected people changed, send message and photo in Telegram
				if amount == True:
					if new_amount != old_amount:
						old_amount = new_amount
						if new_amount > 0: 
							bt.send_message(chat_id, 'Someone is detected')
							bt.send_photo(chat_id, Image.fromarray(img))
						on_update(new_amount)

			stframe.image(img, use_column_width = True)
