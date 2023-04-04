import streamlit as st
import os
import time
import cv2
import numpy as np
# from ocr import *
from passporteye import read_mrz


os.system("clear")
st.set_page_config(layout="wide")

st.header("OCR Passport")

upload_methods = ["Từ thư viện trong máy"] #, "Chụp ảnh mới"]
upload_method = st.radio("Phương pháp upload ảnh", upload_methods)

image_file = st.file_uploader("Upload file")

left, right = st.columns(2)

if image_file is not None:
    #images= convert_from_bytes(image_file.getvalue())
    left.image(image_file,use_column_width="always")
    nparr = np.fromstring(image_file.getvalue(), np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite("./temp.jpg",img_np)
    submit = left.button("Nhận dạng")
else:
    submit = clear = False



if submit:
    with st.spinner(text="Processing..."):
        a=time.time()
        mrz = read_mrz("./temp.jpg")

        # Obtain image
        mrz_data = mrz.to_dict()
        
        b=time.time()
        # In kết quả đã gộp
        # for text in merged_texts:
        #     right.write(text)

        right.write(mrz_data)

        # right.write(fulltext)
        right.write(f"Thời gian đọc là: {b-a}s")