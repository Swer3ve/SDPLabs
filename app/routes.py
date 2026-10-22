import os
from flask import Blueprint, render_template, request, current_app
from werkzeug.utils import secure_filename

main = Blueprint('main', __name__)


def allowed_file(filename):
    return ('.' in filename and
            filename.rsplit('.', 1)[1].lower()
            in current_app.config['ALLOWED_EXTENSIONS'])


@main.route('/cv/upload', methods=['GET', 'POST'])
def cv_upload():
    if request.method == 'POST':
        file = request.files.get('cv')
        if file is None or file.filename == '':
            return render_template(
                'cv_upload.html',
                error='Файл сонгоогүй байна.'), 400
        if not allowed_file(file.filename):
            return render_template(
                'cv_upload.html',
                error='Зөвхөн PDF эсвэл DOCX файл зөвшөөрнө.'), 400
        filename = secure_filename(file.filename)
        file.save(os.path.join(
            current_app.config['UPLOAD_FOLDER'], filename))
        return render_template(
            'cv_upload.html',
            message='CV амжилттай байршлаа.'), 200
    return render_template('cv_upload.html')


@main.errorhandler(413)
def file_too_large(e):
    return render_template(
        'cv_upload.html',
        error='Файлын хэмжээ 5MB-аас ихгүй байх ёстой.'), 400