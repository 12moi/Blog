


from xml.etree.ElementTree import Comment
from flask_script import Manager,Server
from app.main.views import Blog
from app.models import Blog, User
from flask_migrate import Migrate, MigrateCommand
from app import create_app,db
from config import config_options

app = create_app('development')

manager =  Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
manager.add_command('run',Server(use_debugger=True))

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Blog=Blog, Comment=Comment)

@app.before_first_request
def create_tables():
    db.create_all()
    
@manager.command
def test():
    '''
    Run the unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=5).run(tests)

if __name__ == '__main__':
    manager.run()