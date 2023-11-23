from flask import Flask,render_template,jsonify,request
from database import load_students_from_db,load_student_from_db,add_comment_to_db


app = Flask(__name__)

# STUDENTS=[
#     {
#         'id':1,
#         'title':'master',
#         'location':'Hangzhou,China',
#         'name':'Young'
#     },
#     {
#         'id':2,
#         'title':'master',
#         'location':'Hangzhou,China',
#         'name':'QIQI'
#     },
#     {
#         'id':3,
#         'title':'master',
#         'location':'Hangzhou,China',
#         'name':'Elaine'
#     },
#     {
#         'id':4,
#         'location':'Hangzhou,China',
#         'name':'NIUNIU'
#     },
# ]





@app.route("/")
def hello_world():
    students=load_students_from_db()
    return render_template('home.html',
                           students=students,
                           school='ZJUT')


@app.route("/api/students")
def list_students():
    return jsonify(load_students_from_db())

@app.route("/student/<student_id>")
def show_student(student_id):
    student=load_student_from_db(student_id)
    if not student:
        return "Not Found", 404
    return render_template('studentpage.html',
                           student=student)


@app.route("/student/<student_id>/comment",methods=['post'])
def leave_comment(student_id):
    data=request.form
    student=load_student_from_db(student_id)
    #print(data)
    add_comment_to_db(user_id=1,student_id=student_id,comment=data)
    return render_template('comment_submitted.html',
                           comment=data,
                           student=student)




if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)