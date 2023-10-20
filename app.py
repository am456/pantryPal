from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
import pytesseract

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)

# Home page functions
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return extract_text_from_image('static/img/' + filename)
    return render_template('upload.html')

# Extract text from image
def extract_text_from_image(img_path):
    text = pytesseract.image_to_string(img_path)
    return text
