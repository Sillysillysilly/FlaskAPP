
from sqlalchemy import create_engine,text

engine = create_engine("mysql+pymysql://root:1244468436@localhost:3306/flasklearning?charset=utf8mb4")

def load_students_from_db():
    with engine.connect() as conn:
        result = conn.execution_options(stream_results=True).execute(
            text("select * from students"))
    
        students=[]
        for row in result.all():
            students.append(row._asdict())
        return students

    
def load_student_from_db(student_id):
    with engine.connect() as conn:
        result = conn.execution_options(stream_results=True).execute(
            text("select * from students where student_id= :val"),{"val":student_id})

        rows=result.all()
        if len(rows) == 0:
            return None
        else:
            return rows[0]._asdict()


def add_comment_to_db(user_id,student_id,comment):
    with engine.connect() as conn:
        query=text("INSERT INTO comments VALUES(:comment_id,:user_id,:student_id,:comment_content,:comment_rank)")
        
        # print("-----------------------------------")
        # print(query,{"comment_id":None,"user_id":user_id,"student_id":student_id,"comment_content":comment['comment_content'],"comment_rank":comment['comment_rank']})
        conn.execution_options(stream_results=True).execute(query,{"comment_id":None,"user_id":user_id,"student_id":student_id,"comment_content":comment['comment_content'],"comment_rank":comment['comment_rank']})
        conn.commit()

    # print(type(result))
    # result_all=result.all()
    # print(type(result_all))
    # print(result_all)
    # print("---------------")
    # first_result=result_all[0]
    # print(type(first_result))
    # print(first_result)
    # first_result_dict=first_result._asdict()
    # print(type(first_result_dict))
    # print(first_result_dict)



