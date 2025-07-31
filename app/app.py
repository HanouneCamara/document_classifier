from flask import Flask, render_template, request
import os
import sys
from werkzeug.utils import secure_filename

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from predictor import load_model, predict

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = load_model("../models/model.pth")

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    image_url = None

    if request.method == 'POST':
        file = request.files.get('image')
        if file:
            filename = secure_filename(file.filename)
            image_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(image_path)
            prediction, confidence = predict(model, image_path)
            confidence = f"{confidence:.2f}"  # Formate à 2 décimales

            # Nouveau : déplacer l'image dans le dossier correspondant à la prédiction
            if prediction:
                class_folder = os.path.join(UPLOAD_FOLDER, prediction)
                os.makedirs(class_folder, exist_ok=True)
                new_image_path = os.path.join(class_folder, filename)
                os.rename(image_path, new_image_path)
                image_url = f"/static/uploads/{prediction}/{filename}"
            else:
                image_url = f"/static/uploads/{filename}"
    else:
        confidence = None

    return render_template('index.html', prediction=prediction, confidence=confidence, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
