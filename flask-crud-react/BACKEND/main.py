from myapp import app
with app.app_context():
    from myapp import db
    db.create_all()
if __name__ == '__main__':
    app.run()