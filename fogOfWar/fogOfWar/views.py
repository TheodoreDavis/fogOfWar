"""
Routes and views for the flask application.
"""

import os
from datetime import datetime
from flask import flash, render_template, request, redirect, url_for
from fogOfWar import app
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'C:\\Users\\Theodore\\source\\repos\\fogOfWar\\fogOfWar\\fogOfWar\\uploads\\'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/upload', methods=['GET', 'POST'])
def upload():
        """Renders the websocket testpage"""
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('upload',
                                    filename=filename))
        return render_template('upload.html',
            title = 'Upload a file',
            year = datetime.now().year,
            message = 'pdf, png, jpeg, and jpg are accepted'
        )
