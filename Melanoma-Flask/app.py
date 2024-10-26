import os
import glob
import tensorflow as tf
from flask import Flask, render_template, request, send_from_directory
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array

app = Flask(__name__)

# Folder paths
dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = os.path.join(dir_path, "uploads", "all_class")
STATIC_FOLDER = os.path.join(dir_path, "static")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load the model from the static folder
model = tf.keras.models.load_model(os.path.join(STATIC_FOLDER, "model.h5"))

IMAGE_SIZE = 224

# Function to preprocess uploaded images
def load_and_preprocess_image():
    test_fldr = 'uploads'
    test_generator = ImageDataGenerator(rescale=1./255).flow_from_directory(
        test_fldr,
        target_size=(IMAGE_SIZE, IMAGE_SIZE),
        batch_size=1,
        class_mode=None,
        shuffle=False
    )
    test_generator.reset()
    return test_generator

# Function to classify the uploaded image
def classify(model):
    batch_size = 1
    test_generator = load_and_preprocess_image()
    
    # Replaced deprecated predict_generator with predict
    prob = model.predict(test_generator, steps=len(test_generator) // batch_size)
    
    labels = {0: 'Just another beauty mark', 1: 'Get that mole checked out'}
    label = labels[1] if prob[0][0] >= 0.5 else labels[0]
    classified_prob = prob[0][0] if prob[0][0] >= 0.5 else 1 - prob[0][0]
    
    return label, classified_prob

# Home route to clean up old files and render home page
@app.route("/", methods=['GET'])
def home():
    # Clean up old files in the uploads folder
    filelist = glob.glob(os.path.join(UPLOAD_FOLDER, "*.*"))
    for filePath in filelist:
        try:
            os.remove(filePath)
        except OSError as e:
            print(f"Error while deleting file {filePath}: {e}")
    
    return render_template("home.html")

# Route to handle file upload and classification
@app.route("/classify", methods=["POST", "GET"])
def upload_file():
    if request.method == "GET":
        return render_template("home.html")

    if "image" not in request.files:
        return render_template("home.html", error="No file part")

    file = request.files["image"]

    if file.filename == "":
        return render_template("home.html", error="No selected file")

    # Save the uploaded file
    upload_image_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(upload_image_path)
    
    # Classify the uploaded image
    label, prob = classify(model)
    prob = round(prob * 100, 2)

    return render_template(
        "classify.html", image_file_name=file.filename, label=label, prob=prob
    )

# Route to serve the uploaded image
@app.route("/classify/<filename>")
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
