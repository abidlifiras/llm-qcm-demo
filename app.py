from flask import Flask, render_template, request, jsonify
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = Flask(__name__)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_path = "camembert_multilabel_model"

tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
model = AutoModelForSequenceClassification.from_pretrained(model_path, local_files_only=True)
model.to(device)
model.eval()

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    question = data.get("question")
    choices = data.get("choices")

    if not question or not choices or len(choices) < 2:
        return jsonify({"error": "Entrée invalide"}), 400

    inputs = tokenizer(
        [f"{question} {choice}" for choice in choices],
        padding="max_length",
        truncation=True,
        max_length=128,
        return_tensors="pt"
    )

    input_ids = inputs["input_ids"].to(device)
    attention_mask = inputs["attention_mask"].to(device)

    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        logits = outputs.logits.squeeze().cpu()
        if logits.dim() == 2 and logits.shape[1] == 1:
            logits = logits.squeeze(1)
        probs = torch.sigmoid(logits).detach().cpu().numpy().flatten()


    probs = probs[:len(choices)]
    predicted_indices = [i for i, p in enumerate(probs) if p > 0.5]

    return jsonify({
        "predicted_indices": predicted_indices,
        "probabilities": [round(float(p), 4) for p in probs]
    })

if __name__ == "__main__":
    app.run(debug=True)
