from flask import Blueprint, request, jsonify, render_template, send_from_directory
from PIL import Image
from helpers import token_required
from models import db, User, Student, student_schema, students_schema
import os


api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'yee': 'haw'}

@api.route('/students',methods = ['POST'])
@token_required
def create_student(current_user_token):
    FirstName = request.json['FirstName']
    LastName = request.json['LastName']
    Parent1 = request.json['Parent1']
    Parent2 = request.json['Parent2']
    Phone1 = request.json['Phone1']
    Phone2 = request.json['Phone2']
    Email1 = request.json['Email1']
    Email2 = request.json['Email2']
    Address1 = request.json['Address1']
    Address2 = request.json['Address2']
    City_ST_Zip1 = request.json['City_ST_Zip1']
    City_ST_Zip2 = request.json['City_ST_Zip2']
    user_token = current_user_token.token
    
    print(f'BIG TESTER: {current_user_token.token}')

    student = Student(FirstName, LastName, Parent1, Parent2, Phone1, Phone2, Email1, Email2, Address1, Address2, City_ST_Zip1, City_ST_Zip2, user_token=user_token)

    db.session.add(student)
    db.session.commit()

    response = student_schema.dump(student)
    return jsonify(response)


# NEW STUFF - IMAGE UPLOAD AND PROCESSING =====================================================
# UPLOAD_FOLDER = '../static/student_images'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# def resize_image(image, size):
#     """Resizes an image to a given size.

#     Args:
#         image: The image to resize.
#         size: The size to resize the image to.

#     Returns:
#         The resized image.
#     """

#     width, height = image.size
#     if width > size or height > size:
#         image = image.resize((size, size), Image.ANTIALIAS)
#     return image

# @api.route('/students/<id>/upload', methods = ['POST','PUT'])
# @token_required
# def upload_image(current_user_token,id):
#     student = Student.query.get(id)
#     student.id = request.json['id']
#     student.Photo = request.json['Photo']
#     student.user_token = current_user_token.token

#     """ Uploads an image and returns the URL of the thumbnail image."""

#     if 'photo' not in request.files:
#         return jsonify({'error': 'No file part'}), 400
    
#     file = request.files['Photo']

#     if file.filename == '':
#         return jsonify({'error': 'No selected file'}), 400
    
#     if file.filename.rsplit('.', 1)[1].lower() not in ALLOWED_EXTENSIONS:
#         return jsonify({'error': 'File type must be .png, .jpg, .jpeg, or .gif'})
#     if file:
#         filename = student.id + '.' + file.filename.rsplit('.', 1)[1].lower()
    
#     file.save(os.path.join(UPLOAD_FOLDER, filename))

#     image = Image.open(os.path.join(UPLOAD_FOLDER, filename))
#     thumbnail = resize_image(image, 128)
#     thumbnail.save(os.path.join(UPLOAD_FOLDER, filename))

#     student.Photo = request.json[os.path.join(UPLOAD_FOLDER, filename)]

#     db.session.commit()
#     response = student_schema.dump(student)
#     return jsonify(response)

# =================================================================================
@api.route('/students', methods = ['GET'])
@token_required
def get_student(current_user_token):
    a_user = current_user_token.token
    students = Student.query.filter_by(user_token = a_user).all()
    response = students_schema.dump(students)
    return jsonify(response)

@api.route('/students/<id>', methods = ['GET'])
@token_required
def get_single_student(current_user_token, id):
    student = Student.query.get(id)
    response = student_schema.dump(student)
    return jsonify(response)

@api.route('/students/<id>', methods = ['POST','PUT'])
@token_required
def update_student(current_user_token,id):
    student = Student.query.get(id)
    student.FirstName = request.json['FirstName']
    student.LastName = request.json['LastName']
    student.Parent1 = request.json['Parent1']
    student.Parent2 = request.json['Parent2']
    student.Phone1 = request.json['Phone1']
    student.Phone2 = request.json['Phone2']
    student.Email1 = request.json['Email1']
    student.Email2 = request.json['Email2']
    student.Address1 = request.json['Address1']
    student.Address2 = request.json['Address2']
    student.City_ST_Zip1 = request.json['City_ST_Zip1']
    student.City_ST_Zip2 = request.json['City_ST_Zip2']
    student.user_token = current_user_token.token

    db.session.commit()
    response = student_schema.dump(student)
    return jsonify(response)

@api.route('/students/<id>', methods = ['DELETE'])
@token_required
def delete_student(current_user_token, id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    response = student_schema.dump(student)
    return jsonify(response)

