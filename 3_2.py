class Worker:
    def __init__(self, name, surname, daily_rate, days_worked):
        self._name = name
        self._surname = surname
        self._daily_rate = daily_rate
        self._days_worked = days_worked

    def calculate_salary(self):
        return self._daily_rate * self._days_worked

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def get_daily_rate(self):
        return self._daily_rate

    def get_days_worked(self):
        return self._days_worked


workers = []

while True:
    print("\n1 - Add worker\n2 - Show salary\n3 - Display worker list\n4 - Exit")
    try:
        choice = int(input("Select action: "))
    except ValueError:
        print("Please enter a number between 1-4")
        continue

    if choice == 1:
        name = input("Name: ")
        surname = input("Surname: ")
        try:
            daily_rate = int(input("Daily rate: "))
            days_worked = int(input("Days worked: "))
            workers.append(Worker(name, surname, daily_rate, days_worked))
            print(f"Worker {name} {surname} added successfully!")
        except ValueError:
            print("Please enter valid numbers for rate and days")

    elif choice == 2:
        if not workers:
            print("No workers available!")
            continue

        print("\nWorker list:")
        for i, worker in enumerate(workers, 1):
            print(f"{i}. {worker.get_name()} {worker.get_surname()}")

        try:
            worker_num = int(input("Worker number: ")) - 1
            if 0 <= worker_num < len(workers):
                print(f"Salary: {workers[worker_num].calculate_salary()}")
            else:
                print("Invalid worker number!")
        except ValueError:
            print("Please enter a valid number!")

    elif choice == 3:
        if not workers:
            print("No workers available!")
            continue

        print("\nWorker details:")
        for i, worker in enumerate(workers, 1):
            print(f"{i}. {worker.get_name()} {worker.get_surname()} | "
                  f"Rate: {worker.get_daily_rate()} | "
                  f"Days: {worker.get_days_worked()}")

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please select 1-4")