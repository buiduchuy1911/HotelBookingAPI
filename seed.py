from app import create_app, db, bcrypt
from app.models.user import User
from app.models.hotel import Hotel
from app.models.room_type import RoomType
from app.models.room import Room
from app.models.amenity import Amenity, HotelAmenity

def seed_data():
    app = create_app()
    with app.app_context():
        print("Đang dọn dẹp và tạo dữ liệu mẫu...")

        # 1. Tạo Users
        if not User.query.filter_by(email="admin@hotel.com").first():
            hashed_pw = bcrypt.generate_password_hash("123456").decode('utf-8')
            admin = User(email="admin@hotel.com", password_hash=hashed_pw, full_name="Quản trị viên", role="admin")
            db.session.add(admin)
            
            user = User(email="user@hotel.com", password_hash=hashed_pw, full_name="Khách hàng VIP", role="registered")
            db.session.add(user)

        # 2. Tạo Amenities
        amenities_data = ["Free WiFi", "Swimming Pool", "Breakfast Included", "Gym", "Spa"]
        amenity_objs = []
        for name in amenities_data:
            am = Amenity.query.filter_by(name=name).first()
            if not am:
                am = Amenity(name=name, description=f"Tiện nghi {name}")
                db.session.add(am)
            amenity_objs.append(am)

        # 3. Tạo Room Types
        types_data = [
            {"name": "Standard", "max_occupancy": 2, "base_price": 500000, "description": "Phòng tiêu chuẩn cho 2 người"},
            {"name": "Deluxe", "max_occupancy": 3, "base_price": 1000000, "description": "Phòng rộng rãi, view đẹp"},
            {"name": "Suite", "max_occupancy": 4, "base_price": 2500000, "description": "Phòng tổng thống cao cấp"}
        ]
        type_objs = []
        for td in types_data:
            rt = RoomType.query.filter_by(name=td["name"]).first()
            if not rt:
                rt = RoomType(**td)
                db.session.add(rt)
            type_objs.append(rt)

        db.session.commit() # Commit để lấy ID

        # 4. Tạo Hotels
        hotels_data = [
            {"name": "Grand Palace Hotel", "address": "Quận 1, TP.HCM", "star_rating": 5, "description": "Khách sạn 5 sao sang trọng ngay trung tâm."},
            {"name": "Sea View Resort", "address": "Nha Trang, Khánh Hòa", "star_rating": 4, "description": "Resort gần biển yên tĩnh, lý tưởng cho nghỉ dưỡng."},
            {"name": "Mountain Retreat", "address": "Sapa, Lào Cai", "star_rating": 3, "description": "Khách sạn trên sườn núi thơ mộng, khí hậu mát mẻ quanh năm."}
        ]
        
        for hd in hotels_data:
            hotel = Hotel.query.filter_by(name=hd["name"]).first()
            if not hotel:
                hotel = Hotel(**hd)
                db.session.add(hotel)
                db.session.commit()
                
                # Thêm Amenities cho hotel
                # Khách sạn đầu lấy đủ tiện nghi, khách sạn sau lấy ít hơn
                for am in amenity_objs[:hd["star_rating"]]: 
                    if not HotelAmenity.query.filter_by(hotel_id=hotel.id, amenity_id=am.id).first():
                        db.session.add(HotelAmenity(hotel_id=hotel.id, amenity_id=am.id))
                
                # 5. Tạo Rooms cho Hotel
                room_number = 101
                for rt in type_objs:
                    # Tạo 2 phòng mỗi loại cho từng khách sạn
                    for _ in range(2): 
                        room_code = f"{hd['name'][:3].upper()}-{room_number}"
                        if not Room.query.filter_by(room_number=room_code, hotel_id=hotel.id).first():
                            room = Room(room_number=room_code, room_type_id=rt.id, hotel_id=hotel.id, is_available=True)
                            db.session.add(room)
                        room_number += 1
                        
                db.session.commit()

        print("🎉 Hoàn tất chèn dữ liệu mẫu thành công!")
        print("Tài khoản Admin: admin@hotel.com | Pass: 123456")
        print("Tài khoản User : user@hotel.com  | Pass: 123456")

if __name__ == '__main__':
    seed_data()
