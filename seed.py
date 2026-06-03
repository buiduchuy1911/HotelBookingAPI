from app import create_app, db, bcrypt
from app.models.user import User
from app.models.hotel import Hotel
from app.models.room_type import RoomType
from app.models.room import Room
from app.models.amenity import Amenity, HotelAmenity

app = create_app()

with app.app_context():
    print("Đang dọn dẹp dữ liệu cũ...")
    db.drop_all()
    db.create_all()

    print("Đang tạo tài khoản...")
    # Tạo Admin
    admin = User(email='admin@hotel.com', full_name='Quản trị viên', role='admin')
    admin.password_hash = bcrypt.generate_password_hash('123456').decode('utf-8')
    
    # Tạo User
    user1 = User(email='user@hotel.com', full_name='Khách hàng', role='registered')
    user1.password_hash = bcrypt.generate_password_hash('123456').decode('utf-8')

    db.session.add_all([admin, user1])
    db.session.commit()

    print("Đang tạo tiện nghi (Amenities)...")
    wifi = Amenity(name='Free WiFi', description='Internet tốc độ cao miễn phí')
    pool = Amenity(name='Hồ bơi vô cực', description='Hồ bơi ngoài trời nhìn ra biển')
    spa = Amenity(name='Spa & Massage', description='Dịch vụ thư giãn cao cấp')
    gym = Amenity(name='Phòng Gym', description='Phòng tập hiện đại 24/7')
    
    db.session.add_all([wifi, pool, spa, gym])
    db.session.commit()

    print("Đang tạo danh sách khách sạn...")
    hotel1 = Hotel(
        name='The Grand Plaza', 
        address='123 Nguyễn Huệ, Quận 1, TP.HCM', 
        description='Khách sạn 5 sao sang trọng bậc nhất nằm ngay trung tâm thành phố.', 
        star_rating=5
    )
    
    hotel2 = Hotel(
        name='Ocean View Resort', 
        address='45 Trần Phú, Nha Trang', 
        description='Khu nghỉ dưỡng tuyệt đẹp với góc nhìn thẳng ra bờ biển Nha Trang.', 
        star_rating=4
    )

    hotel3 = Hotel(
        name='Sapa Mountain Retreat', 
        address='01 Fansipan, Sapa', 
        description='Không gian yên tĩnh, ấm cúng giữa lòng sương mù.', 
        star_rating=4
    )
    
    db.session.add_all([hotel1, hotel2, hotel3])
    db.session.commit() # Commit để lấy ID cho khách sạn

    print("Đang liên kết Khách sạn & Tiện nghi...")
    hotel_amenities = [
        # Hotel 1 có đủ 4 tiện nghi
        HotelAmenity(hotel_id=hotel1.id, amenity_id=wifi.id),
        HotelAmenity(hotel_id=hotel1.id, amenity_id=pool.id),
        HotelAmenity(hotel_id=hotel1.id, amenity_id=spa.id),
        HotelAmenity(hotel_id=hotel1.id, amenity_id=gym.id),
        
        # Hotel 2 có 2 tiện nghi
        HotelAmenity(hotel_id=hotel2.id, amenity_id=wifi.id),
        HotelAmenity(hotel_id=hotel2.id, amenity_id=pool.id),
        
        # Hotel 3 có 2 tiện nghi
        HotelAmenity(hotel_id=hotel3.id, amenity_id=wifi.id),
        HotelAmenity(hotel_id=hotel3.id, amenity_id=spa.id),
    ]
    db.session.add_all(hotel_amenities)
    db.session.commit()

    print("Đang cấu hình hạng phòng (Room Types)...")
    standard = RoomType(name='Standard', max_occupancy=2, base_price=500000, description='Phòng tiêu chuẩn ấm cúng cho 2 người')
    deluxe = RoomType(name='Deluxe', max_occupancy=3, base_price=1000000, description='Phòng rộng rãi có ban công')
    suite = RoomType(name='Suite', max_occupancy=4, base_price=2500000, description='Phòng cao cấp nhất với phòng khách riêng biệt')
    
    db.session.add_all([standard, deluxe, suite])
    db.session.commit()

    print("Đang tạo danh sách các phòng vật lý...")
    rooms = []
    
    # Khách sạn 1 (The Grand Plaza)
    rooms.append(Room(room_number='101', hotel_id=hotel1.id, room_type_id=standard.id, is_available=True))
    rooms.append(Room(room_number='102', hotel_id=hotel1.id, room_type_id=standard.id, is_available=True))
    rooms.append(Room(room_number='201', hotel_id=hotel1.id, room_type_id=deluxe.id, is_available=True))
    rooms.append(Room(room_number='301', hotel_id=hotel1.id, room_type_id=suite.id, is_available=True))
    
    # Khách sạn 2 (Ocean View)
    rooms.append(Room(room_number='A01', hotel_id=hotel2.id, room_type_id=standard.id, is_available=True))
    rooms.append(Room(room_number='A02', hotel_id=hotel2.id, room_type_id=deluxe.id, is_available=True))
    rooms.append(Room(room_number='VIP', hotel_id=hotel2.id, room_type_id=suite.id, is_available=True))

    # Khách sạn 3 (Sapa)
    rooms.append(Room(room_number='S01', hotel_id=hotel3.id, room_type_id=standard.id, is_available=True))
    rooms.append(Room(room_number='S02', hotel_id=hotel3.id, room_type_id=deluxe.id, is_available=True))

    db.session.add_all(rooms)
    db.session.commit()

    print("="*50)
    print("Khởi tạo dữ liệu mẫu thành công")
    print("Tài khoản Quản trị: admin@hotel.com | Mật khẩu: 123456")
    print("Tài khoản Khách:   user@hotel.com  | Mật khẩu: 123456")
    print("="*50)
