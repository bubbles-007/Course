# 🎓 First-Order Logic (FOL) Course Registration Reasoner

An AI knowledge representation and inference system built from scratch in Python to determine student course eligibility based on prerequisites, course completion facts, and academic rules.

## 🚀 Project Overview
This project implements a complete First-Order Logic reasoning engine featuring:
* Custom **FOL Unification** algorithm (Russell & Norvig style).
* **Forward Chaining** (data-driven inference with visual trace logging).
* **Backward Chaining** (goal-driven inference with proof trees).
* **Multi-scale Dataset Benchmarking** (Small, Medium, and Large scales).
* **Streamlit Interactive UI & Visualization Dashboard**.

---

## 🛠️ Project Structure
```text
fol_course_registration/
│
├── venv/                  # Virtual environment
├── knowledge_base.py      # Horn clauses and multi-scale datasets
├── fol_engine.py          # Core Unification, Forward & Backward chaining
├── experiments.py         # Automated performance benchmarking script
└── app.py                 # Streamlit interactive web interface