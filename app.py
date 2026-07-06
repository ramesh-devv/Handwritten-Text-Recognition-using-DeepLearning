from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
import traceback

from predict import predict_text

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        if "image" not in request.files:
            return jsonify({
                "success": False,
                "message": "No image uploaded."
            })

        file = request.files["image"]

        if file.filename == "":
            return jsonify({
                "success": False,
                "message": "Please select an image."
            })

        if not allowed_file(file.filename):
            return jsonify({
                "success": False,
                "message": "Only PNG, JPG and JPEG images are allowed."
            })

        filename = secure_filename(file.filename)

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        file.save(filepath)

        text, confidence = predict_text(filepath)

        return jsonify({
            "success": True,
            "text": text,
            "confidence": confidence
        })

    except Exception as e:

        print("\n" + "=" * 80)
        print("FULL ERROR")
        print("=" * 80)
        traceback.print_exc()
        print("=" * 80 + "\n")

        return jsonify({
            "success": False,
            "message": str(e)
        })


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )