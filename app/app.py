from flask import Flask, render_template, request
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from predictor import load_model, predict 

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join('app', 'static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = load_model("../models/model.pth")

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    image_url = None

    if request.method == 'POST':
        file = request.files['image']
        if file:
            image_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(image_path)
            prediction = predict(model, image_path)
            image_url = f"static/uploads/{file.filename}"

    return render_template('index.html', prediction=prediction, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)
