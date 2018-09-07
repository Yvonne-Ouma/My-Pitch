
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager,Server
from app.models import User,db
from app import create_app

app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)
@manager.command
def test():
   """Run the unit tests."""
   import unittest
   tests = unittest.TestLoader().discover('tests')
   unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )

if __name__ == '__main__':
   manager.run()