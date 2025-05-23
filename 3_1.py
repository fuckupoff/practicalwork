class Worker:
    def __init__(self, name, surname, daily_rate, days_worked):
        self.name = name
        self.surname = surname
        self.daily_rate = daily_rate
        self.days_worked = days_worked

    def calculate_salary(self):
        return self.daily_rate * self.days_worked


workers = []

while True:
    print("\n1 - Add worker\n2 - Show salary\n3 - Exit")
    choice = int(input("Action: "))

    if choice == 1:
        name = input("Name: ")
        surname = input("Surname: ")
        daily_rate = int(input("Daily rate: "))
        days_worked = int(input("Days worked: "))
        workers.append(Worker(name, surname, daily_rate, days_worked))
        print(f"{name} {surname} added successfully!")

    elif choice == 2:
        if not workers:
            print("No workers available!")
            continue

        print("\nWorker list:")
        for i, worker in enumerate(workers, 1):
            print(f"{i}. {worker.name} {worker.surname}")

        try:
            worker_num = int(input("Worker number: ")) - 1
            if 0 <= worker_num < len(workers):
                salary = workers[worker_num].calculate_salary()
                print(f"Salary: {salary}")
            else:
                print("Invalid worker number!")
        except ValueError:
            print("Please enter a valid number!")

    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please select 1, 2 or 3")