import os
import sys
from django.core.management import execute_from_command_line

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'repo.settings')

    # 使用SQLite数据库(简化打包)
    db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
    os.environ['DATABASE_URL'] = f'sqlite:///{db_path}'

    # 模拟runserver命令
    sys.argv = ['manage.py', 'runserver', '--noreload']
    execute_from_command_line(sys.argv)