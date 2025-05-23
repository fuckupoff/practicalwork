class MyClass:
    def __init__(self, name="NoName"):
        self._name = name
        print(f"Object {self._name} created")

    def __del__(self):
        print(f"Object {self._name} destroyed")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

while True:
    choice = input("Create object? (Yes/No): ").strip().capitalize()
    if choice == 'Yes':
        name = input("Enter object name: ")
        obj = MyClass(name)
        break
    elif choice == 'No':
        print("OK")
        break
    else:
        print("Invalid input")

while True:
    try:
        choice = int(input("1 - Edit object\n2 - Delete object\nAction: "))
        if choice == 1:
            new_name = input("Enter new object name: ")
            obj.name = new_name
            print(f"Object name changed to {obj.name}")
        elif choice == 2:
            del obj
            break
        else:
            print("Invalid choice")
    except ValueError:
        print("Please enter a number")