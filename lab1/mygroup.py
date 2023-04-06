groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [3, 4, 5]
    },
    {
        "name": "Анна",
        "surname": "Сидорова",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Сергей",
        "surname": "Смирнов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Алексей",
        "surname": "Борисов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [2, 4, 3]
    },
    {
        "name": "Дмитрий",
        "surname": "Овчинников",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [3, 5, 4]
    },
    {
        "name": "Алина",
        "surname": "Кузнецова",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 4]
    }
]


def filter_students(array, min_grade):
    filtered_array = []

    for student in array:
        marks = student['marks']
        average = sum(marks) / len(marks)
        if average >= min_grade:
            filtered_array.append(student)

    return filtered_array


min_grade = int(input('Введите средний балл: '))

filtered_array = filter_students(groupmates, min_grade)

for student in filtered_array:
    print(student)
