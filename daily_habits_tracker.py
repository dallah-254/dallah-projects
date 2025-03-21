habits = []

def add_habit():
    print("type stop to stop adding habits")
    while True:
        habit = input("Enter a habit you want to track: ")
        habits.append(habit)
        if habit.lower() == "stop":
            habits.pop()
            break  

add_habit()

print("my habits are ", habits)
print("habit added successfully")
           
        

