# QA_LLM

A lightweight web application that leverages a fine-tuned CamemBERT model to answer French multiple-choice questions (QCM) using a multi-label classification approach.

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Download the fine-tuned model

Download the pre-trained CamemBERT multi-label model from the following Google Drive link:

🔗 [camembert_multilabel_model.zip](https://drive.google.com/file/d/1_fEFhry3Z3RmI_1j8zhxsH3-YBlifF6-/view?usp=sharing)

Unzip the file and place the extracted `camembert_multilabel_model` folder at the root of the project, alongside the following structure:

```
project_root/
├── app.py
├── templates/
├── camembert_multilabel_model/
├── dataset/
├── requirements.txt
```

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

Then open your browser and go to:

👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## 📓 Colab Notebooks

You will also find Colab notebooks that reproduce the training and evaluation steps in the **same Drive folder** as the model zip file.

These notebooks:
- Show data preprocessing
- Perform fine-tuning of CamemBERT for multi-label QCM
- Evaluate performance on dev/test sets

## 🖼️ Screenshots

The included screenshots (`QA_LLM_1.png`, `QA_LLM_2.png`) demonstrate:
- The interactive web interface
- The model's predicted answers and probabilities

## 💡 Features

- Supports multi-label predictions (multiple correct answers)
- Dynamic probability display for each choice
- Auto-highlights predicted answers
- French language support via CamemBERT
