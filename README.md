# 🏨 Hotel Booking REST API

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.3-black)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![JWT](https://img.shields.io/badge/JWT-Authentication-orange)
![Swagger](https://img.shields.io/badge/Swagger-Flasgger-brightgreen)

Đây là đồ án môn học **[IE221] Kỹ thuật Lập trình Python**. Dự án cung cấp một hệ thống API RESTful mạnh mẽ phục vụ cho ứng dụng Đặt phòng Khách sạn, được xây dựng hoàn toàn bằng **Python, Flask** và kiến trúc **MVC**.

## 🌟 Tính năng Nổi bật (Features)

- **Authentication & RBAC**: Đăng ký, Đăng nhập với JSON Web Token (JWT). Phân quyền tự động giữa `Guest`, `Registered User` và `Admin`.
- **Quản lý Khách sạn & Phòng**: Hỗ trợ đầy đủ các thao tác CRUD dành cho quản trị viên, tìm kiếm và phân trang khách sạn cho Guest.
- **Thuật toán Kiểm tra Phòng trống**: Tự động quét cơ sở dữ liệu `Bookings` để trả về danh sách các phòng trống thực sự dựa trên khoảng thời gian `check_in` và `check_out`.
- **Hệ thống Đặt phòng & Thanh toán**: Tự động tính toán tổng hóa đơn dựa trên số đêm ở lại và `base_price` của từng loại phòng. Chặn đặt trùng lịch.
- **Đánh giá (Reviews)**: Xác thực người dùng phải từng hoàn tất việc đặt phòng tại một khách sạn mới có quyền đưa ra đánh giá sao (1-5) và bình luận.
- **Bảo mật & Chuẩn hoá**: Password được băm bằng `Bcrypt`. Dữ liệu input/output được kiểm duyệt và format chặt chẽ qua `Marshmallow`. Global Error Handler bắt lỗi tập trung (JSON response).
- **Tài liệu API Tự động**: Tích hợp sẵn `Swagger UI` thông qua `Flasgger`.

## 🛠️ Công nghệ Sử dụng (Tech Stack)

- **Core**: Python, Flask
- **Database**: SQLite (dùng cho Development), Flask-SQLAlchemy, Flask-Migrate
- **Security**: Flask-JWT-Extended, Flask-Bcrypt, Flask-CORS
- **Validation**: Marshmallow, Flask-Marshmallow
- **API Documentation**: Flasgger

## 🚀 Hướng dẫn Cài đặt & Chạy (Installation)

### 1. Clone dự án và Cài đặt môi trường
```bash
# Clone repository
git clone <đường-link-github-của-bạn>
cd IE221_HotelBookingAPI

# Tạo môi trường ảo (Virtual Environment)
python -m venv venv

# Kích hoạt môi trường ảo
# Trên Windows:
.\venv\Scripts\activate
# Trên macOS/Linux:
source venv/bin/activate

# Cài đặt các thư viện cần thiết
pip install -r requirements.txt
```

### 2. Cấu hình Biến Môi trường
Tạo một file `.env` ở thư mục gốc của dự án và điền các thông tin sau:
```env
SECRET_KEY=your-super-secret-key
JWT_SECRET_KEY=your-jwt-secret-key
FLASK_ENV=development
```

### 3. Khởi tạo Cơ sở dữ liệu (Database)
```bash
# Thiết lập các thư mục migrations
flask db init

# Tạo file migration dựa trên các Models hiện tại
flask db migrate -m "Initial migration"

# Áp dụng migration vào database
flask db upgrade
```

### 4. Chạy Server
```bash
python run.py
```
Server sẽ chạy ở địa chỉ: `http://localhost:5000`

## 📖 Tài liệu API (API Documentation - Swagger)

Khi server đang chạy, bạn có thể xem danh sách toàn bộ API và thao tác thử trực tiếp thông qua giao diện **Swagger UI**:
👉 **[http://localhost:5000/apidocs/](http://localhost:5000/apidocs/)**

## 📂 Cấu trúc Thư mục (Project Structure)
```
IE221_HotelBookingAPI/
├── app/
│   ├── controllers/      # Logic xử lý nghiệp vụ
│   ├── models/           # Định nghĩa cấu trúc bảng CSDL (SQLAlchemy)
│   ├── schemas/          # Xác thực dữ liệu đầu vào và đầu ra (Marshmallow)
│   ├── views/            # Các tuyến đường API Endpoints (Blueprints)
│   ├── utils/            # Custom Decorators và Global Error Handlers
│   ├── config.py         # Thiết lập môi trường Development/Production
│   └── __init__.py       # Khởi tạo Flask app và các thư viện
├── migrations/           # Lịch sử thay đổi Database (Alembic)
├── venv/                 # Môi trường ảo Python
├── .env                  # Biến môi trường bảo mật (Không push lên Git)
├── .gitignore            # Các file rác loại trừ khỏi Git
├── requirements.txt      # Danh sách thư viện
├── run.py                # Script khởi động chính
└── schema.dbml           # Bản vẽ Database (ERD) dùng trên dbdiagram.io
```

## 👨‍💻 Tác giả (Author)
Đồ án thuộc về Sinh viên thực hiện môn [IE221] Kỹ thuật Lập trình Python.
