#  Задание №5
results = [
    ("Али", 5),
    ("Мадина", 3),
    ("Тимур", 4),
    ("Сабина", 2),
    ("Дилшод", 5),
    ("Камила", 4),
    ("Бекзод", 2),
    ("Нигора", 5)
]

total = 0
fives = []
twos = 0
grades = set()
counts = {}

for name, grade in results:
    total += grade

    if grade == 5:
        fives.append(name)

    if grade == 2:
        twos += 1

    grades.add(grade)

    if grade in counts:
        counts[grade] += 1
    else:
        counts[grade] = 1

average = total / len(results)

print("Средний балл:", average)
print("Оценка 5:", fives)
print("Получили 2:", twos)
print("Разные оценки:", grades)
print("Количество оценок:", counts)