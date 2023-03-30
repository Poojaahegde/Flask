from flask_sqlalchemy import SQLAlchemy
 
db =SQLAlchemy()
 
class StudentModel(db.Model):
    __tablename__ = "students"
 
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    student_id = db.Column(db.Integer)
    birthdate = db.Column(db.String())
    ammountdue = db.Column(db.String())
  
 
    def __init__(self, first_name,last_name,student_id,birthdate,ammountdue):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id=student_id
        self.birthdate=birthdate
        self.ammountdue=ammountdue
        
    def __repr__(self):
        return f"{self.first_name}:{self.last_name}"