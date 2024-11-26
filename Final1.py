grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(type(grades))
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(type(students))

grades[0] = round(sum([5, 3, 3, 5, 4]) / len ([5, 3, 3, 5, 4]), 2)
grades[1] = round(sum([2, 2, 2, 3]) / len([2, 2, 2, 3]), 2)
grades[2] = round(sum([4, 5, 5, 2]) / len([4, 5, 5, 2]), 2)
grades[3] = round(sum([4, 4, 3]) / len([4, 4, 3]), 2)
grades[4] = round(sum([5, 5, 5, 4, 5]) / len([5, 5, 5, 4, 5]), 2)
print(grades)

students = list({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
print(type(students))
students.sort(key=None, reverse=False)
print(students)

mark = dict(zip(students, grades))
print(mark)