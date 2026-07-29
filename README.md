# Smart MCQ Solver - DL & GenAI Project

**Student:** Soumya Ranjan Panda  
**Roll number:** 23f2004742

This repository contains experiments for a deep learning and generative AI project on multiple-choice question answering. Given a prompt and five candidate answers (`A`-`E`), the goal is to rank the most likely correct options and produce top-3 predictions.

## Project Structure

```text
.
+-- data/
|   +-- train.csv
|   +-- test.csv
+-- final/
|   +-- dl-23f2004742-notebook-t22026.ipynb
+-- notebooks/
|   +-- Final Submission.ipynb
|   +-- Submission.ipynb
|   +-- experiment notebooks...
+-- reports/
|   +-- Smart_MCQ_Report_Final.pdf
+-- README.md
```

## Data

The dataset is stored in `data/`.

- `train.csv`: training rows with `id`, `prompt`, answer choices `A`-`E`, and the correct `answer`.
- `test.csv`: test rows with `id`, `prompt`, and answer choices `A`-`E`.

## Final Notebook

The final notebook is kept separate in `final/`.

- `final/dl-23f2004742-notebook-t22026.ipynb`: final consolidated project notebook.

## Experiment Notebooks

Supporting notebooks are in `notebooks/`.

- `Final Submission.ipynb` and `Submission.ipynb`: submission workflow drafts.
- Other notebooks document experiments such as TF-IDF baselines, transformers, RAG, cross-encoder reranking, LoRA, leakage fixes, metric updates, and model upgrades.

## Approach

The project explores a progression of methods:

1. TF-IDF and cosine-similarity baselines.
2. Sentence-transformer embeddings.
3. Retrieval-augmented generation and reranking.
4. Transformer fine-tuning and LoRA-style improvements.
5. Ensembling and submission generation.

Evaluation is centered on top-3 answer ranking, using MAP@3-style validation in the notebooks.

## How to Run

Open the final notebook in Jupyter, VS Code, or Kaggle and run it from top to bottom. The notebooks expect `train.csv` and `test.csv` to be available under `data/` or the corresponding Kaggle input path used inside the notebook.

Common Python packages used across the experiments include:

- `pandas`
- `numpy`
- `scikit-learn`
- `sentence-transformers`
- `transformers`
- `torch`
- `wandb`

Some notebook runs may require internet access for downloading pretrained models and may use Weights & Biases for experiment tracking.

## Report

The final report is available at `reports/Smart_MCQ_Report_Final.pdf`.
