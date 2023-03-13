from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Department(db.Model):
    __tablename__= 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    students = db.relationship('Student', backref='department', lazy=True)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_departments(cls):
        return cls.query.all()



class Student(db.Model):
    __tablename__= 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email= db.Column(db.String(100),unique=True, nullable=True)
    accepted = db.Column(db.Boolean, default=True)
    age = db.Column(db.Integer, default=10, nullable=True)
    dept_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable= True)


    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_students(cls):
        return cls.query.all()


    def delete_object(self):
        db.session.delete(self)
        db.session.commit()
        return True

