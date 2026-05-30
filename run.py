import os
from app import create_app

env_name = os.getenv('FLASK_ENV', 'development')
app = create_app(env_name)

if __name__ == '__main__':
    # Đoạn if này giúp chặn việc in ra 2 lần do tính năng auto-reload của Flask
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        print("="*60)
        print("🚀 BACKEND SERVER ĐÃ SẴN SÀNG")
        print("👉 Xem toàn bộ tài liệu API tại: http://localhost:5000/apidocs/")
        print("="*60)
        
    app.run(host='0.0.0.0', port=5000)
