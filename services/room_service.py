from models.room import Room

class RoomService:
    def __init__(self, data):
        self.rooms = [Room.from_dict(r) for r in data.get("rooms", [])]

    def add_room(self, room_number, capacity):
        if any(r.room_number == room_number for r in self.rooms):
            print("❗ Room already exists")
            return
        self.rooms.append(Room(room_number, capacity))
        print("✅ Room added successfully")

    def view_rooms(self):
        if not self.rooms:
            print("No rooms found")
            return
        for r in self.rooms:
            print(r)

    def get_room(self, room_number):
        for r in self.rooms:
            if r.room_number == room_number:
                return r
        return None

    def get_all(self):
        return [r.to_dict() for r in self.rooms]