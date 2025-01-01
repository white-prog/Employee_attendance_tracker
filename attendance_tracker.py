
def main():
    from datetime import date
    Attendance = []
    print("Employee Attendance Tracker")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")
    for i in range(3):
        print("")
    while True:
        for i in range(2):
            print("")
        inp = int(input("Choose an option: "))
        if inp == 1:
            name = input("Enter employee name: ")
            attendan = input(f"Is {name} present or absent? ")
            print(f"Attendance for {name} has been recorded.")
            Attendance.append((name,attendan))
        elif inp == 2:
            tdy = date.today()
            print(f"Today's attendance - ({str(tdy)})")
            for attend in Attendance:
                print(f"- {attend[0]} : {attend[1]}")
        elif inp == 3:
            print("Goodbye!")
            break
        else:
            print("Wrong input!")

if __name__ == "__main__":
    main()
            




