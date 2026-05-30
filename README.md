# 🏨 Hotel Booking REST API

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.3-black)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red)
![JWT](https://img.shields.io/badge/JWT-Authentication-orange)
![Swagger](https://img.shields.io/badge/Swagger-Flasgger-brightgreen)

Dự án cung cấp một hệ thống API RESTful mạnh mẽ phục vụ cho ứng dụng Đặt phòng Khách sạn, được xây dựng hoàn toàn bằng **Python, Flask** và kiến trúc **MVC**.

## 🌟 Tính năng chính

### Dành cho Khách hàng (User)
- **Tìm kiếm Khách sạn & Phòng**: Xem danh sách các khách sạn, tìm kiếm và lọc danh sách phòng trống chính xác theo ngày nhận/trả phòng.
- **Đặt phòng**: Thực hiện đặt phòng nhanh chóng, hệ thống tự động kiểm tra trùng lịch và tính toán tổng hóa đơn dựa theo số đêm lưu trú.
- **Quản lý Đặt phòng**: Xem lại lịch sử các phòng đã đặt của bản thân hoặc thực hiện thao tác hủy phòng.
- **Đánh giá & Bình luận**: Được quyền để lại đánh giá (từ 1-5 sao) và bình luận cho khách sạn (chỉ áp dụng nếu khách hàng đã từng hoàn tất việc đặt phòng tại đó).
- **Tài khoản cá nhân**: Đăng ký, đăng nhập an toàn để quản lý các thao tác đặt phòng.

### Dành cho Quản trị viên (Admin)
- **Quản lý Khách sạn**: Thêm mới, cập nhật thông tin chi tiết, hoặc xóa các khách sạn khỏi hệ thống.
- **Quản lý Phòng & Hạng phòng**: Thiết lập các hạng phòng (Standard, Deluxe...), cấu hình giá tiền và sức chứa. Thêm các phòng vật lý vào khách sạn.
- **Quản lý Tiện nghi**: Tạo danh sách các tiện nghi (WiFi, Hồ bơi, Spa...) và phân bổ chúng vào từng khách sạn cụ thể.
- **Quản lý Người dùng**: Kiểm soát danh sách toàn bộ thành viên, có quyền cấp quyền quản trị (admin) cho người khác hoặc xóa tài khoản.

## 🛠️ Công nghệ Sử dụng (Tech Stack)

- **Core**: Python, Flask
- **Database**: SQLite (dùng cho Development), Flask-SQLAlchemy, Flask-Migrate
- **Security**: Flask-JWT-Extended, Flask-Bcrypt, Flask-CORS
- **Validation**: Marshmallow, Flask-Marshmallow
- **API Documentation**: Flasgger

## 📂 Cấu trúc Thư mục (Project Structure)
```
IE221_HotelBookingAPI/
├── app/
│   ├── controllers/      # Logic xử lý nghiệp vụ
│   ├── models/           # Định nghĩa cấu trúc bảng CSDL (SQLAlchemy)
│   ├── schemas/          # Xác thực dữ liệu đầu vào và đầu ra (Marshmallow)
│   ├── views/            # Các tuyến đường API Endpoints (Blueprints)
│   ├── utils/            # Custom Decorators và Global Error Handlers
│   ├── config.py         
│   └── __init__.py       
├── migrations/           
├── venv/                 
├── .env                  
├── .gitignore            
├── requirements.txt      
├── run.py                
└── schema.dbml           
```

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
Tạo một file `.env` ở thư mục gốc của dự án và sao chép toàn bộ các cấu hình sau dán vào:
```env
FLASK_APP=run.py
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=super-secret-key-change-in-production
JWT_SECRET_KEY=jwt-super-secret-key-change-in-production
DATABASE_URI=sqlite:///hotel_booking.db
```

### 3. Khởi tạo Cơ sở dữ liệu (Database)
```bash
# Thiết lập các thư mục migrations
flask db init

# Tạo file migration dựa trên các Models hiện tại
flask db migrate -m "Initial migration"

# Áp dụng migration vào database
flask db upgrade

# Tạo dữ liệu mẫu (Khách sạn, Phòng, Tài khoản dùng thử)
python seed.py
```

### 4. Chạy Server
```bash
python run.py
```
Server sẽ chạy ở địa chỉ: `http://localhost:5000`

## 📖 Tài liệu API (API Documentation - Swagger)

Khi server đang chạy, có thể xem danh sách toàn bộ API và thao tác thử trực tiếp thông qua giao diện **Swagger UI**:
👉 **[http://localhost:5000/apidocs/](http://localhost:5000/apidocs/)**
