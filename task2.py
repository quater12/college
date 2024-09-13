a = "Hello, World!"
b = "Boryslaw"
c = "Humenuik"
d = 16

print("Тип змінної a:", type(a))
print("Тип змінної b:", type(b))
print("Тип змінної c:", type(c))
print("Тип змінної d:", type(d))

if type(b) == type(c):
    print("Ім'я і прізвище мають один і той же тип даних:", type(b))
else:
    print("Ім'я і прізвище мають різні типи даних.")

full_name = (b, c)

print("Ім'я і прізвище:", full_name)
if isinstance(d, int):
    print("Тип змінної d (вік) - це int.")
    other_types = [type(a), type(b), type(c)]
    for t in other_types:
        if t == type(d):
            print(f"Тип даних віку (int) збігається з типом {t}.")
        else:
            print(f"Тип даних віку (int) не збігається з типом {t}.")
else:
    print("Тип змінної d не є int.")
