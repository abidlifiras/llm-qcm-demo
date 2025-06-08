# 🧠 QA_LLM – CamemBERT for French Multi-label QCM

A lightweight and interactive web application that leverages a fine-tuned **CamemBERT** model to solve French multiple-choice questions (QCM) using a **multi-label classification approach**.

---

## 💡 Features

- 🔤 Full support for **French language questions**
- ✅ Handles **multiple correct answers** (multi-label)
- 📊 Displays prediction **probabilities** for each choice
- 🎯 Automatically highlights the predicted correct options
- 🧪 Based on a fine-tuned version of **camembert-base**

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Download the fine-tuned model

Download the exported CamemBERT model (multi-label version) from this Google Drive link:

🔗 [camembert_multilabel_model.zip](https://drive.google.com/file/d/1_fEFhry3Z3RmI_1j8zhxsH3-YBlifF6-/view?usp=sharing)

Unzip it and place the folder named `camembert_multilabel_model` in the root of the project:

```
project_root/
├── app.py
├── templates/
├── camembert_multilabel_model/
├── dataset/
├── requirements.txt
```

---

### 3. Run the Flask application

#### On Linux/macOS (or WSL):

```bash
export FLASK_APP=app.py
flask run
```

#### On Windows:

```cmd
set FLASK_APP=app.py
flask run
```

Then open your browser at:

👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📓 Colab Notebooks

Colab notebooks reproducing the full pipeline are included in the same Drive folder as the model (and also available in this repository).  
These notebooks demonstrate:

- 📊 Dataset analysis and preprocessing
- 🧠 Fine-tuning CamemBERT on `train.json`
- 📈 Evaluation on `dev.json` and `test.json` using strict and tolerant metrics

---

## 🖼️ Screenshots

Included screenshots:
- `QA_LLM_1.png` – The main web interface
- `QA_LLM_2.png` – Prediction results and visual probabilities

---

## 📁 Repository Structure (Overview)

```
QA_LLM/
├── app.py                        # Main Flask app
├── templates/                   # HTML templates
├── camembert_multilabel_model/ # Fine-tuned model files
├── dataset/                     # JSON files (train/dev/test)
├── notebooks/                   # Colab notebooks for training and evaluation
├── requirements.txt
├── README.md
```

---
