from utils.file_handler import load_data, save_data
from services.student_service import StudentService
from services.room_service import RoomService
from services.booking_service import BookingService
from menu import show_menu

def main():
    data = load_data()

    student_service = StudentService(data)
    room_service = RoomService(data)
    booking_service = BookingService(student_service, room_service)

    while True:
        show_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            sid = input("Student ID: ")
            name = input("Name: ")
            student_service.add_student(sid, name)

        elif choice == "2":
            student_service.view_students()

        elif choice == "3":
            sid = input("Student ID to delete: ")
            student_service.delete_student(sid)

        elif choice == "4":
            rn = input("Room Number: ")
            cap = int(input("Capacity: "))
            room_service.add_room(rn, cap)

        elif choice == "5":
            room_service.view_rooms()

        elif choice == "6":
            sid = input("Student ID: ")
            rn = input("Room Number: ")
            booking_service.assign_room(sid, rn)

        elif choice == "7":
            booking_service.view_allocations()

        elif choice == "0":
            # Save data before exit
            save_data({
                "students": student_service.get_all(),
                "rooms": room_service.get_all()
            })
            print("Data saved. Goodbye 👋")
            break

        else:
            print("❗ Invalid choice")

if __name__ == "__main__":
    main()