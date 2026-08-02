---
title: Smart MCQ Solver
emoji: 🧠
colorFrom: blue
colorTo: purple
sdk: gradio
app_file: app.py
pinned: false
---

# 🧠 Smart MCQ Solver – Deep Learning & Generative AI

> **Student:** Soumya Ranjan Panda  
> **Roll Number:** 23F2004742

Smart MCQ Solver is a Deep Learning and Generative AI project for **Multiple Choice Question Answering (MCQA)**. The objective is to predict the **top-3 most probable correct answers** from five options (A–E) for each question.

The project explores multiple NLP and Deep Learning approaches, compares their performance, and builds an ensemble for improved accuracy.

---

## 📂 Project Structure

```text
.
├── data/
│   ├── train.csv
│   └── test.csv
│
├── final/
│   └── dl-23f2004742-notebook-t22026.ipynb
│
├── models/
│   ├── 01_tfidf.ipynb
│   ├── 02_sentence_transformer.ipynb
│   ├── 03_deepnet_mpnet.ipynb
│   ├── 04_tfidf_deepnet.ipynb
│   ├── 05_bilstm_attention.ipynb
│   ├── 06_deberta_finetune.ipynb
│   └── 07_discriminator.ipynb
│
├── notebooks/
│   ├── archive/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_comparison.ipynb
│   └── 04_ensemble.ipynb
│
├── outputs/
│   └── submission.csv
│
├── reports/
│   └── Smart_MCQ_Report_Final.pdf
│
└── README.md
```

---

# 📊 Dataset

The dataset contains multiple-choice questions with five candidate answers.

### **train.csv**

Contains:

- `id`
- `prompt`
- Options `A`, `B`, `C`, `D`, `E`
- `answer` (ground truth)

### **test.csv**

Contains:

- `id`
- `prompt`
- Options `A`, `B`, `C`, `D`, `E`

The task is to predict the **Top-3 ranked answers** for each test question.

---

# 🚀 Models Implemented

The project evaluates several approaches, starting from classical NLP methods to modern transformer architectures.

| Notebook | Method |
|-----------|--------|
| **01_tfidf.ipynb** | TF-IDF + Cosine Similarity baseline |
| **02_sentence_transformer.ipynb** | Sentence Transformer embeddings |
| **03_deepnet_mpnet.ipynb** | MPNet-based Deep Neural Network |
| **04_tfidf_deepnet.ipynb** | Hybrid TF-IDF + Deep Learning model |
| **05_bilstm_attention.ipynb** | BiLSTM with Attention |
| **06_deberta_finetune.ipynb** | Fine-tuned DeBERTa Transformer |
| **07_discriminator.ipynb** | Discriminator model for answer ranking |

---

# 📓 Supporting Notebooks

The `notebooks/` directory contains supporting experiments and analysis.

- **01_eda.ipynb**
  - Dataset exploration
  - Label distribution
  - Missing value analysis
  - Data statistics

- **02_preprocessing.ipynb**
  - Text cleaning
  - Tokenization
  - Feature preparation

- **03_comparison.ipynb**
  - Model performance comparison
  - Validation metrics
  - Error analysis

- **04_ensemble.ipynb**
  - Ensemble techniques
  - Final prediction generation

---

# 🏆 Final Submission

The final consolidated notebook is located at:

```text
final/
└── dl-23f2004742-notebook-t22026.ipynb
```

This notebook includes:

- Data loading
- Preprocessing
- Model inference
- Ensemble
- Submission generation

---

# 📈 Evaluation Metric

Models are evaluated using **MAP@3 (Mean Average Precision @ 3)**.

The objective is to rank the three most likely correct answers for each question.

---

# 📦 Requirements

Main Python libraries used:

```text
Python 3.10+

pandas
numpy
scikit-learn
torch
transformers
sentence-transformers
datasets
accelerate
wandb
matplotlib
```

Install dependencies using:

```bash
pip install -r requirements.txt
```

or install the required packages individually.

---

# ▶️ Running the Project

Clone the repository:

```bash
git clone <repository-url>
cd Smart-MCQ-Solver
```

Run the notebooks in the following order:

1. `notebooks/01_eda.ipynb`
2. `notebooks/02_preprocessing.ipynb`
3. Model notebooks under `models/`
4. `notebooks/03_comparison.ipynb`
5. `notebooks/04_ensemble.ipynb`

Or simply execute the final notebook:

```text
final/dl-23f2004742-notebook-t22026.ipynb
```

---

# 📁 Outputs

Generated prediction files are stored in:

```text
outputs/
└── submission.csv
```

---

# 📄 Report

The complete project report is available in:

```text
reports/
└── Smart_MCQ_Report_Final.pdf
```

The report discusses:

- Problem formulation
- Data preprocessing
- Model architectures
- Experimental setup
- Results and comparisons
- Final conclusions

---

# 👨‍💻 Author

**Soumya Ranjan Panda**

**Roll Number:** 23F2004742

Deep Learning & Generative AI Project
IIT Madras
