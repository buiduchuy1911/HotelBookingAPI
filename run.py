import os
import sys
from app import create_app

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

env_name = os.getenv('FLASK_ENV', 'development')
app = create_app(env_name)

if __name__ == '__main__':
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        print("="*60)
        print("Backend đã khởi chạy thành công")
        print("Xem toàn bộ tài liệu API tại: http://localhost:5000/apidocs/")
        print("="*60)
    app.run(host='0.0.0.0', port=5000)
