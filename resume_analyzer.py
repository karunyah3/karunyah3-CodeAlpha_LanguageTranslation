import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Extract text from PDF
def extract_text(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text.lower()

# Analyze resume
def analyze_resume():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not file_path:
        return

    resume_text = extract_text(file_path)
    job_role = job_entry.get().lower()

    if job_role == "":
        result_label.config(text="⚠ Please enter job role/skills")
        return

    texts = [resume_text, job_role]

    vectorizer = CountVectorizer().fit_transform(texts)
    similarity = cosine_similarity(vectorizer[0:1], vectorizer[1:2])
    score = round(similarity[0][0] * 100, 2)

    # Missing skills detection
    resume_words = set(resume_text.split())
    job_words = set(job_role.split())

    missing_skills = job_words - resume_words

    # Display result
    result_text = f"Match Score: {score}%\n\n"

    if missing_skills:
        result_text += "Missing Skills:\n"
        for skill in missing_skills:
            result_text += f"- {skill}\n"
    else:
        result_text += "No missing skills 🎉"

    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, result_text)

# GUI
root = tk.Tk()
root.title("AI Resume Analyzer Pro")
root.geometry("750x500")
root.config(bg="#0f172a")

# Title
title = tk.Label(root, text="AI Resume Analyzer", font=("Arial", 20, "bold"),
                 bg="#0f172a", fg="#38bdf8")
title.pack(pady=15)

# Input
job_entry = tk.Entry(root, width=50, font=("Arial", 12))
job_entry.pack(pady=10)
job_entry.insert(0, "Enter job role or skills (e.g. python machine learning sql)")

# Button
btn = tk.Button(root, text="Upload Resume & Analyze",
                command=analyze_resume,
                bg="#22c55e", fg="white",
                font=("Arial", 12, "bold"),
                padx=10, pady=5)
btn.pack(pady=15)

# Result box
result_box = tk.Text(root, height=15, width=80, font=("Arial", 11),
                     bg="#020617", fg="white")
result_box.pack(pady=10)

root.mainloop()
