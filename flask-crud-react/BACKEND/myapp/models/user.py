from myapp import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.Text)
    role = db.Column(db.String(50))


    def __init__(self, username, password, role) -> None:
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self) -> str:
        return f'User: {self.username}'