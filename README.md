# Streamlit PCB Defect Detection App

This Streamlit app detects defects in Printed Circuit Boards (PCBs) using computer vision techniques and YOLO object detection model.

## Features

- Upload images or videos (supported formats: jpg, jpeg, png, mp4).
- Real-time detection of PCB defects including missing hole, mouse bite, open circuit, short, spur, and spurious copper.
- Displays total defects detected and a summary of each defect type.
- User-friendly interface with sidebar navigation for defect classes.

## Installation

To run this app, you need to have Python installed. You can install the required packages using `pip` and the provided `requirements.txt` file:

<h1>Streamlit PCB Defect Detection App</h1>

<p>This Streamlit app is designed for detecting and analyzing defects in Printed Circuit Boards (PCBs) using computer vision techniques. It employs the YOLO (You Only Look Once) object detection model to identify various types of PCB defects in uploaded images or videos.</p>

<h2>Features</h2>
<ul>
  <li>Real-time Detection: The app performs real-time detection of PCB defects such as missing holes, mouse bites, open circuits, shorts, spurs, and spurious copper traces.</li>
  <li>Defect Classification: Detected defects are categorized and displayed with their respective counts and a summary.</li>
  <li>User Interface: The app features a user-friendly interface with sidebar navigation for different defect classes, making it easy to explore and analyze results.</li>
  <li>Upload Functionality: Users can upload images or videos (supported formats include jpg, jpeg, png, and mp4).</li>
</ul>

<h2>Installation</h2>
<p>To run this app, you need to have Python installed. You can install the required packages using <code>pip</code> and the provided <code>requirements.txt</code> file:</p>

<pre><code>pip install -r requirements.txt</code></pre>

<h2>Usage</h2>
<ol>
  <li>Clone this repository:</li>
</ol>
<pre><code>git clone https://github.com/mehulnaik16/PCB-2.0-YOLOV8-STREAMLIT.git
cd PCB-2.0-YOLOV8-STREAMLIT
</code></pre>

<ol start="2">
  <li>Install the required packages:</li>
</ol>
<pre><code>pip install -r requirements.txt</code></pre>


<ol start="3">
  <li>Run the Streamlit app:</li>
</ol>
<pre><code>streamlit run app.py</code></pre>


<ol start="4">
  <li>You can create a virtual environment (Better Option) or directly run code </li>
</ol>
