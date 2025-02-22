# The 'Flask' class (used to create a Flask web application) and a function to render page templates are imported.
from flask import Flask
from flask import render_template

# A Flask form, and two fields and a validator for said form are imported.
from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms import SubmitField
from wtforms.validators import InputRequired

# A function used to get a secure file name (to protect against CSRF attacks) is imported.
from werkzeug.utils import secure_filename

# The 'OS' library is imported, which will allow saving and accessing via path of an uploaded image.
import os

# Two functions from the 'Keras' API, used to preprocess uploaded images, are imported.
from keras._tf_keras.keras.utils import load_img, img_to_array

# The 'Joblib' library is imported, which will allow loading of a deepfake detection machine learning model.
import joblib

# The 'NumPy' library is imported, used to preprocess uploaded images.
import numpy

#
#import PIL


# A list is used to store extensions of files that a user is allowed to upload.
allowed_extensions = ["jpg"]


# An Flask instance is created, which represents the web application.
app = Flask(__name__)

# The Flask app is configured to have a secret key.
app.config["SECRET_KEY"] = "supersecretkey"

# The Flask app is configured to have a folder where uploaded files can be saved.
app.config["UPLOAD_FOLDER"] = "static/files"


# A class is created, to represent a form to be used in the flask web app (where users can upload image files.)
class upload_file_form(FlaskForm):
    file = FileField("File",validators=[InputRequired()])
    submit = SubmitField("Upload File")


# This function loads a machine learning model, preprocesses an uploaded image, and generates a classification prediction on said image using said model.
def image_classification_prediction(upload_path):
    deepfake_detection_model = joblib.load("static/14.02.2025__Deepfake-Detection-Model.pkl",mmap_mode=None)
    resized_upload = load_img(upload_path,target_size=(150,150))
    resized_upload_array = img_to_array(resized_upload)
    resized_upload_array = numpy.expand_dims(resized_upload_array,axis=0)
    resized_upload_array /= 255.
    prediction = deepfake_detection_model.predict(resized_upload_array)
    prediction_class_index = numpy.argmax(prediction)
    return prediction_class_index


# A URL route is created for the index page of the application.
@app.route("/")
def home():
    return render_template("index.html")

# A URL route is created for the page where image files will be uploaded via a form. The code here will check the file is a '.jpg' image, save it in the app's static folder, and call the function which will generate a classification prediction.
@app.route("/upload",methods=["GET","POST"])
def upload():
    form = upload_file_form()
    if (form.validate_on_submit()):
        uploaded_file = form.file.data
        uploaded_file_name = secure_filename(uploaded_file.filename)
        uploaded_file_type = str(uploaded_file_name.split(".")[-1])
        uploaded_file_type = uploaded_file_type.lower()
        if (uploaded_file_type in allowed_extensions):
            # A path is created which is where the uploaded image will be saved.
            uploaded_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config["UPLOAD_FOLDER"],secure_filename(uploaded_file.filename))
            # The uploaded image is now saved using the above path.
            uploaded_file.save(uploaded_file_path)
            # A classification prediction on the uploaded image is made, and passed as a value to an output page (which doesn't have a URL route).
            prediction_for_upload = image_classification_prediction(str(uploaded_file_path))
            return render_template("output.html",value_pass=prediction_for_upload)
        else:
            return render_template("upload_fail.html")
    return render_template("upload.html",form=form)

# A URL route is created for a 'Hello World' page (made while first creating the web app).
@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


# Whenever this script file is ran, so too will be the above flask web app, on a localhost.
if (__name__=="__main__"):
    app.run(debug=True)