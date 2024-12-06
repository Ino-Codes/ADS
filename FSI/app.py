from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

app = Flask(__name__)

#inserindo os dados
texts = [
    "Muito ruim",
    "Ruim",
    "Razoável",
    "Bom",
    "Excelente"
]
labels = [1, 2, 3, 4, 5]

#treinando o modelo
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
model = MultinomialNB()
model.fit(X, labels)

#salvando o modelo e o vetor pra reutilizar
with open("model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)
with open("vectorizer.pkl", "wb") as vec_file:
    pickle.dump(vectorizer, vec_file)

#rota raiz
@app.route('/')
def home():
    return "Deu bom, a API tá funcionando!"

#endpoint da API
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get("text", "")

    #carregando o modelo e o vetor
    with open("model.pkl", "rb") as model_file:
        loaded_model = pickle.load(model_file)
    with open("vectorizer.pkl", "rb") as vec_file:
        loaded_vectorizer = pickle.load(vec_file)

    X_input = loaded_vectorizer.transform([text])
    prediction = loaded_model.predict(X_input)

    return jsonify({"text": text, "prediction": int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)