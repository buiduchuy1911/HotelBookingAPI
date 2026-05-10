import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "frontend"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == "__main__":
    if not os.path.exists(DIRECTORY):
        print(f"Lỗi: Không tìm thấy thư mục '{DIRECTORY}'.")
    else:
        with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
            print("="*50)
            print("🚀 FRONTEND SERVER ĐÃ KHỞI ĐỘNG THÀNH CÔNG")
            print(f"👉 Vui lòng mở trình duyệt và truy cập: http://localhost:{PORT}")
            print("="*50)
            print("Lưu ý: Đảm bảo Backend Server (python run.py) vẫn đang chạy ở cổng 5000.")
            print("(Bấm Ctrl + C để tắt server này)")
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("\nĐã tắt Frontend Server.")
