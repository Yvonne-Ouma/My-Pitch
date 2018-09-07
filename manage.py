
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager,Server

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )

if __name__ == '__main__':
   manager.run()