from flask import Blueprint, request, jsonify, render_template
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
    Photo = request.json['Photo']
    Parent1 = request.json['Parent1']
    Parent2 = request.json['Parent2']
    Phone1 = request.json['Phone1']
    Phone2 = request.json['Phone2']
    Email1 = request.json['Email1']
    Email2 = request.json['Email2']
    Address1 = request.json['Address1']
    Address2 = request.json['Address2']
    user_token = current_user_token.token
    
    print(f'BIG TESTER: {current_user_token.token}')

    student = Student(FirstName, LastName, Photo, Parent1, Parent2, Phone1, Phone2, Email1, Email2, Address1, Address2, user_token=user_token)

    db.session.add(student)
    db.session.commit()

    response = student_schema.dump(student)
    return jsonify(response)

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
    student.Photo = request.json['Photo']
    student.Parent1 = request.json['Parent1']
    student.Parent2 = request.json['Parent2']
    student.Phone1 = request.json['Phone1']
    student.Phone2 = request.json['Phone2']
    student.Email1 = request.json['Email1']
    student.Email2 = request.json['Email2']
    student.Address1 = request.json['Address1']
    student.Address2 = request.json['Address2']
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

