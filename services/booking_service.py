class BookingService:
    def __init__(self, student_service, room_service):
        self.student_service = student_service
        self.room_service = room_service

    def assign_room(self, student_id, room_number):
        if not self.student_service.exists(student_id):
            print("❗ Student not found")
            return

        room = self.room_service.get_room(room_number)
        if not room:
            print("❗ Room not found")
            return

        if room.add_student(student_id):
            print("✅ Room assigned successfully")
        else:
            print("❗ Room is full")

    def view_allocations(self):
        for room in self.room_service.rooms:
            print(f"\nRoom {room.room_number}:")
            if not room.occupants:
                print("  No students")
            else:
                for s_id in room.occupants:
                    print(f"  Student ID: {s_id}")