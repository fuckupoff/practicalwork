class Counter:
    def __init__(self, value=0):
        self._value = value

    def increment(self):
        self._value += 1

    def decrement(self):
        self._value -= 1

    @property
    def current_value(self):
        return self._value

initial_value = int(input("Enter initial counter value (0 = default): "))
if initial_value == 0:
    counter = Counter()
else:
    counter = Counter(initial_value)

while True:
    choice = int(input("1 - Increment by 1\n2 - Decrement by 1\n3 - Status\n4 - Exit\nAction: "))
    if choice == 1:
        counter.increment()
        print("Counter increased by 1")
    elif choice == 2:
        counter.decrement()
        print("Counter decreased by 1")
    elif choice == 3:
        print(f"Current value: {counter.current_value}")
    elif choice == 4:
        break