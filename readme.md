
# 🧠 Resume Job Role Predictor

This Streamlit application predicts the most suitable job role based on a candidate's resume. Users can either paste their resume text or upload a `.pdf` or `.docx` file. The app uses a machine learning model trained on labeled resume data to classify job roles such as **Data Scientist**, **Web Developer**, **HR**, **DevOps**, etc.

---

## 🚀 Features

- 🔍 Predicts job type from resume text
- 📎 Upload support for `.pdf` and `.docx`
- 🧼 Automatically cleans and preprocesses resume text
- 💬 Shows predicted job role in real-time
- 🌐 Deployable with Streamlit Cloud, Render, or custom hosting

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **scikit-learn**
- **TF-IDF Vectorizer**
- **PyMuPDF** (for PDF parsing)
- **python-docx** (for DOCX parsing)

---

## 📁 File Structure

```
job_predictor/
│
├── app.py                   # Streamlit app
├── resume_preprocessor.py   # Resume cleaning logic
├── model.pkl                # Trained ML model (Logistic Regression or similar)
├── tfidf_vectorizer.pkl     # TF-IDF vectorizer
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 📦 Installation

### Clone the repository:

```bash
git clone https://github.com/your-username/job-role-predictor.git
cd job-role-predictor
```

### Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App Locally

```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser.

---

## ☁️ Deployment

### ✅ Streamlit Cloud:
1. Push this project to a public GitHub repo
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your repo and deploy `app.py`
4. Your app gets a live URL like:
   ```
   https://your-username-job-role-predictor.streamlit.app
   ```

---

## 📚 Dataset

This project was trained using a resume dataset containing labeled job categories. You can use datasets like:

- [`anukalp-mishra/Resume-Screening`](https://github.com/anukalp-mishra/Resume-Screening)

---

## 🧠 Future Improvements

- Show top 3 matching job roles with confidence
- Extract key skills from resumes
- Use BERT/Transformer models for better accuracy
- Add support for `.txt` files and OCR for scanned resumes

---

## 🙌 Credits

Made with ❤️ by [Your Name]

---

## 📃 License

This project is licensed under the MIT License.
