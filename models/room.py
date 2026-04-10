class Room:
    def __init__(self, room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity
        self.occupants = []

    def add_student(self, student_id):
        if len(self.occupants) < self.capacity:
            self.occupants.append(student_id)
            return True
        return False

    def remove_student(self, student_id):
        if student_id in self.occupants:
            self.occupants.remove(student_id)

    def to_dict(self):
        return {
            "room_number": self.room_number,
            "capacity": self.capacity,
            "occupants": self.occupants
        }

    @staticmethod
    def from_dict(data):
        room = Room(data["room_number"], data["capacity"])
        room.occupants = data.get("occupants", [])
        return room

    def __str__(self):
        return f"Room {self.room_number} | {len(self.occupants)}/{self.capacity} occupied"