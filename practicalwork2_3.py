class Numbers:
    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def info(self):
        return (f"First number: {self.first_num},\nSecond number: {self.second_num},\n"
                f"Sum of numbers: {self.calculate_sum()},\nMaximum number: {self.find_max()}")

    def update_first_num(self, new_first_num):
        self.first_num = new_first_num

    def update_second_num(self, new_second_num):
        self.second_num = new_second_num

    def calculate_sum(self):
        return self.first_num + self.second_num

    def find_max(self):
        return max(self.first_num, self.second_num)

first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))

numbers = Numbers(first_num, second_num)

while True:
    choice = int(input("1 - Show numbers\n2 - Modify numbers\n3 - Exit\n"))
    if choice == 1:
        print(numbers.info())
    elif choice == 2:
        choice_2 = int(input("1 - First number\n2 - Second number\n3 - Back: "))
        if choice_2 == 1:
            new_first_num = int(input("Enter new first number: "))
            numbers.update_first_num(new_first_num)
        elif choice_2 == 2:
            new_second_num = int(input("Enter new second number: "))
            numbers.update_second_num(new_second_num)
        elif choice_2 == 3:
            continue
        else:
            print("Invalid choice")
    elif choice == 3:
        break
    else:
        print("Invalid choice.")