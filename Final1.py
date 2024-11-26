grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(type(grades))
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(type(students))

i = 0
while i < len(grades):
    grades[i] = round(sum(grades[i]) / len(grades[i]), 2)
    i += 1
print(grades)

people = sorted(students)
mark = dict(zip(people, grades))
print(mark)