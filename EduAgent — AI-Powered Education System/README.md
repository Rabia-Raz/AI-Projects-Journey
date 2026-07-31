
# 🎓 EduAgent — AI-Powered Education System

EduAgent is an intelligent, multi-agent AI application designed to streamline and automate educational workflows. Powered by **Groq AI (Llama-3.3-70b-versatile)**, EduAgent helps educators train custom study materials, generate personalized question papers, grade student answer sheets with AI feedback, and produce class performance analytics.

---

## ✨ Features

* 📚 **Train Data & Knowledge Base:** Upload study materials (PDFs, text notes) or paste custom content to build a localized knowledge base for your AI.
* 📝 **Question Paper Generator:** Automatically generate tailored exam papers based on your trained knowledge base with customizable difficulty levels, mark allocations, and question types (MCQs, Short/Long questions, Fill in the Blanks, T/F).
* ✅ **AI-Powered Paper Checking:** Evaluate student answer sheets with customizable strictness (Lenient, Standard, Strict). Provides detailed feedback, mark breakdown per question, and overall scoring.
* 📊 **Grading & Reports:** View compiled student results, export grades to CSV, and generate comprehensive AI-powered class performance summaries for teachers.
* ⚡ **Ultra-Fast AI Inference:** Integrates with Groq API for rapid LLM processing.

---

## 📁 Project Structure

```text
EduAgent/
├── index.html              # Main Dashboard
├── css/
│   └── style.css           # Global Stylesheet
├── js/
│   ├── config.js           # Configuration & API Key setup
│   └── app.js              # State management & Groq AI calls
└── pages/
    ├── train.html          # Train Data & Document Upload page
    ├── question-paper.html # Question Paper Generator page
    ├── check-paper.html    # Student Paper Checking & Grading page
    └── grading.html        # Class Reports & CSV Export page
