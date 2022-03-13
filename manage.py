


from flask_script import Manager,Server
from app.models import Blog, Comment, Subscriber, User
from flask_migrate import Migrate, MigrateCommand
from app import create_app,db



# Creating app instance
app = create_app('development')
app = create_app('production')
app = create_app('test')


manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User=User,Blog=Blog,Comment=Comment,Subscribe=Subscriber)
if __name__ == '__main__':
    manager.run()


# app = create_app()

# manager =  Manager(app)
# migrate = Migrate(app,db)
# manager.add_command('db',MigrateCommand)
# manager.add_command('run',Server(use_debugger=True))

# @manager.shell
# def make_shell_context():
#     return dict(app = app,db = db,User = User)

# @app.before_first_request
# def create_tables():
#     db.create_all()
    
# @manager.command
# def test():
#     '''
#     Run the unit tests
#     '''
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=5).run(tests)

# if __name__ == '__main__':
#     manager.run()