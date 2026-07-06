# 📝 Handwritten Text Recognition using Deep Learning

A modern AI-powered web application that recognizes handwritten text from images using **Microsoft TrOCR (Transformer-based Optical Character Recognition)**. The application is built with **Flask**, **PyTorch**, and **Hugging Face Transformers**, providing an intuitive interface for uploading handwritten images and extracting text accurately.

---

## 📖 Overview

Handwritten Text Recognition (HTR) is an important application of **Artificial Intelligence**, **Deep Learning**, and **Computer Vision**. This project uses Microsoft's **TrOCR** model to recognize handwritten English text from images and display the extracted text through a clean, responsive web interface.

---

## ✨ Features

- 📝 Recognizes handwritten English text
- 🤖 AI-powered OCR using Microsoft TrOCR
- 📤 Upload images in JPG, JPEG, and PNG formats
- 🖼️ Live image preview before recognition
- 📋 Copy recognized text with one click
- 📥 Download recognized text as a text file
- 💻 Responsive and user-friendly web interface
- ⚡ Fast inference using PyTorch

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Backend
- Flask

### Deep Learning
- Microsoft TrOCR
- Hugging Face Transformers
- PyTorch

### Image Processing
- OpenCV
- Pillow (PIL)

### Frontend
- HTML5
- CSS3
- JavaScript

---

## 📂 Project Structure

```text
Handwritten-Text-Recognition-using-DeepLearning/
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── uploads/
│
├── app.py
├── model_loader.py
├── predict.py
├── preprocess.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/ramesh-devv/Handwritten-Text-Recognition-using-DeepLearning.git
```

### 2. Navigate to the Project Folder

```bash
cd Handwritten-Text-Recognition-using-DeepLearning
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
python app.py
```

### 7. Open Your Browser

```
http://127.0.0.1:5000
```

---

## 🖥️ How It Works

1. Launch the Flask application.
2. Upload a handwritten image.
3. Click the **Recognize** button.
4. The Microsoft TrOCR model processes the image.
5. The recognized text is displayed on the screen.
6. Copy or download the extracted text.

---

## 📸 Screenshots

<img width="563" height="470" alt="Screenshot 2026-07-06 135212" src="https://github.com/user-attachments/assets/fd5417dd-912d-4eb1-a29a-a429c9b4db18" />

ResultL:
 <img width="960" height="540" alt="Screenshot 2026-07-06 151231" src="https://github.com/user-attachments/assets/684bbab0-3bd5-483a-b636-6c18f77f993a" />
 
---

## 🎯 Future Improvements

- Multi-line paragraph recognition
- PDF document support
- Batch image processing
- OCR confidence visualization
- Export results as PDF
- Drag-and-drop image upload
- Cloud deployment
- Multilingual handwriting recognition

---

## 📚 Learning Outcomes

Through this project, I gained practical experience in:

- Deep Learning
- Optical Character Recognition (OCR)
- Computer Vision
- Transformer-based Models
- Flask Web Development
- Image Processing
- PyTorch
- Hugging Face Transformers

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you'd like to contribute:

1. Fork this repository
2. Create a new branch
3. Commit your changes
4. Submit a Pull Request

---

## 📄 License

This project is intended for educational and learning purposes.

---

## 👨‍💻 Author

**Malavath Ramesh**

- 🔗 LinkedIn: https://www.linkedin.com/in/ramimalavath06
- 💻 GitHub: https://github.com/ramesh-devv

---

## ⭐ Show Your Support

If you found this project helpful, consider giving it a ⭐ **Star** on GitHub. Your support motivates me to continue building and sharing more AI and Deep Learning projects.
