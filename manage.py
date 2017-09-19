from flask.ext.script import Manager
from app import app
from app.db_create import db
manager = Manager(app)
@manager.command
def createdb():
    print "Creating DataBase ..."
    db.drop_all()
    db.create_all()
if __name__ == "__main__":
    manager.run()
