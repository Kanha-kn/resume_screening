import streamlit as st
import pickle
from preprocess import clean_text
import docx
import fitz  # PyMuPDF

# Load model and vectorizer
model = pickle.load(open('resume_model.pkl', 'rb'))
vectorizer = pickle.load(open('tfidf_vectorizer.pkl', 'rb'))

# Helper to extract text from docx
def read_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

# Helper to extract text from PDF
def read_pdf(file):
    text = ""
    pdf = fitz.open(stream=file.read(), filetype="pdf")
    for page in pdf:
        text += page.get_text()
    return text

st.title("Resume Job Role Predictor")
st.write("Upload or paste your resume to predict the most suitable job role.")

upload_option = st.radio("Choose input method:", ["Paste Text", "Upload File"])

resume_text = ""

if upload_option == "Paste Text":
    resume_text = st.text_area("Paste your resume text here:")

elif upload_option == "Upload File":
    uploaded_file = st.file_uploader("Upload a PDF or DOCX file", type=["pdf", "docx"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".pdf"):
            resume_text = read_pdf(uploaded_file)
        elif uploaded_file.name.endswith(".docx"):
            resume_text = read_docx(uploaded_file)

if resume_text:
    st.subheader("Raw Resume Text:")
    st.write(resume_text)

    cleaned_text = clean_text(resume_text)
    vectorized_input = vectorizer.transform([cleaned_text])
    prediction = model.predict(vectorized_input)[0]

    st.subheader("Predicted Job Role:")
    st.success(prediction)
