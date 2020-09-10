from project import db


class UserVO(db.Model):
    __tablename__ = 'usermaster'
    userId = db.Column('userId', db.Integer, primary_key=True, autoincrement=True)
    userName = db.Column('userName', db.String(50), nullable=False)
    userCity = db.Column('userCity',db.String(50),nullable=False)
    userAge = db.Column('userAge',db.Integer,nullable=False)
    userStartDate = db.Column('userStartDate',db.String(50),nullable=False)

    def __repr__(self):
        return f"userId: {self.userId}, userName: {self.userName}, userCity: {self.userCity},\
            userAge: {self.userAge}, userStartDate: {self.userStartDate}"

db.create_all()
