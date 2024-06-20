import os
import logging
import tempfile
import cv2 as cv
from PIL import Image
import streamlit as st
from ultralytics import YOLO

MODEL_DIR = './runs/detect/train2/weights/best.pt'

# Defect names corresponding to class indices 0-6
defect_names_map = {
    0: "Missing hole",
    1: "Mouse bite",
    2: "Open circuit",
    3: "Short",
    4: "Spur",
    5: "Supurious copper"
}


def main():
    global model
    model = YOLO(MODEL_DIR)

    # Define a function to create sidebar headers and lists for PCB defect classes
    def create_sidebar_header_and_list(classifications):
        """Creates sidebar headers and lists based on a dictionary of PCB defect classifications"""
        for category, defect_list in classifications.items():
            st.sidebar.header(f"**{category.capitalize()} Classes**")
            for defect in defect_list:
                st.sidebar.markdown(f"- *{defect.capitalize()}*")

    # Define PCB defect classifications using a dictionary (modify as needed)
    defect_classifications = {
        "Defects": ["missing hole", "mouse bite", "open circuit", "short", "spur", "supurious copper"]
    }

    # Call the function with the PCB defect classifications dictionary
    create_sidebar_header_and_list(defect_classifications)
    
    st.title("PCB Defect Detection")
    st.write("The aim of this project is to develop an efficient computer vision model capable of detecting defects in PCBs.")

    # Load image or video
    uploaded_file = st.file_uploader("Upload an image or video", type=['jpg', 'jpeg', 'png', 'mp4'])

    if uploaded_file:
        if uploaded_file.type.startswith('image'):
            inference_images(uploaded_file)
        
        if uploaded_file.type.startswith('video'):
            inference_video(uploaded_file)

def inference_images(uploaded_file):
    image = Image.open(uploaded_file)
    # Predict the image
    results = model.predict(image)

    # Plot boxes and get defect names
    boxes = results[0].boxes
    plotted = results[0].plot()[:, :, ::-1]

    if len(boxes) == 0:
        st.markdown("**No Defects Detected**")
    else:
        defect_indices = boxes.cls.cpu().numpy()  # Extract class indices
        defect_names = [defect_names_map[int(cls_idx)] for cls_idx in defect_indices if int(cls_idx) in defect_names_map]  # Map indices to class names
        defect_count = len(defect_names)
        defect_summary = {}
        for defect in defect_names:
            if defect in defect_summary:
                defect_summary[defect] += 1
            else:
                defect_summary[defect] = 1

        defect_summary_str = ', '.join([f"{name}: {count}" for name, count in defect_summary.items()])

        st.markdown(f"**Total Defects Detected:** {defect_count}")
        st.markdown(f"**Defect Summary:** {defect_summary_str}")

    # Display the image with detections
    st.image(plotted, caption="Detected Defects", width=600)
    logging.info(f"Detected defects in uploaded image: {defect_summary_str}")

def inference_video(uploaded_file):
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(uploaded_file.read())
    temp_file.close()

    cap = cv.VideoCapture(temp_file.name)
    frame_count = 0
    if not cap.isOpened():
        st.error("Error opening video file.")
        return

    frame_placeholder = st.empty()
    stop_placeholder = st.button("Stop")

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1
        if frame_count % 2 == 0:
            # Predict the frame
            results = model.predict(frame, conf=0.75)
            # Plot boxes and get defect names
            plotted = results[0].plot()
            defect_indices = results[0].boxes.cls.cpu().numpy()  # Extract class indices
            defect_names = [defect_names_map[int(cls_idx)] for cls_idx in defect_indices if int(cls_idx) in defect_names_map]  # Map indices to class names

            if defect_names:
                defect_summary = {}
                for defect in defect_names:
                    if defect in defect_summary:
                        defect_summary[defect] += 1
                    else:
                        defect_summary[defect] = 1

                defect_summary_str = ', '.join([f"{name}: {count}" for name, count in defect_summary.items()])
                frame_placeholder.image(plotted, channels="BGR", caption=f"Video Frame - Detected Defects: {defect_summary_str}")
                logging.info(f"Detected defects in video frame: {defect_summary_str}")

            if stop_placeholder:
                break

    cap.release()
    os.unlink(temp_file.name)

if __name__ == '__main__':
    main()
