
def get_positive_number(label):
    while True:
        try:
            value = float(input(f"Введіть {label} (м): "))

            if not (value == value): 
                print("Помилка! Введено NaN.")
                continue

            if value == float("inf") or value == float("-inf"):
                print("Помилка! Нескінченність недопустима.")
                continue

            if value < 0.1 or value > 100:
                print("Помилка! Значення повинно бути від 0.1 до 100.")
                continue

            return value

        except ValueError:
            print("Помилка! Потрібно ввести числове значення.")


print("Площа прямокутної ділянки")

width = get_positive_number("ширину")
height = get_positive_number("висоту")

area = width * height

print(f"\nШирина: {width} м")
print(f"Висота: {height} м")
print(f"Площа прямокутної ділянки: {area:.3f} м²")
