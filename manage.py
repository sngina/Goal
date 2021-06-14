from app import create_app, db
from app.models import User,Role
from flask_script import Manager ,Server
from flask_migrate import Migrate, MigrateCommand

# creating app instances..
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)
migrate = Migrate(app, db) # intialze migrate pass in db and app instance
manager.add_command('db',MigrateCommand) #manager command and pass the migratecommand class

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Role = Role )
    
if __name__ == '__main__':
    manager.run()