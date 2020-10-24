print('')

greeting = 'Hello'
name = 'Niklas'
message = f'{greeting}, {name}. Welcome!'
print(message)

print('')

num = 3.14
print(type(num))

print('')

print(3 + 3)

print('')

print(18 % 3)

print('')

print(round(3.75, ))

print('')

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Chemestry', 'PE', 'German']
courses.extend(courses_2)
print(courses)

print('')

courses = ['History', 'Math', 'Physics', 'CompSci']
# nums = [1, 5, 3, 4, 2]
sorted_courses = sorted(courses)
# print(nums)
print(sorted_courses)

print('')

courses = ['History', 'Math', 'Physics', 'CompSci']
for index, course in enumerate(courses, start=1):
    print(index, course)

print('')

courses = ['History', 'Math', 'Physics', 'CompSci']
course_str = ' - '.join(courses)
print(course_str)

print('')

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
print(list_1)
print(list_2)
list_1[0] = 'Art'
print(list_1)
print(list_2)

# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1
# print(tuple_1)
# print(tuple_2)
# tuple_1[0]= 'Art'
# print(tuple_1)
# print(tuple_2)

print('')

cs_courses = {'History', 'Math', 'Physics', 'CombSci', 'Math'}
print(cs_courses)
print('Math' in cs_courses)
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

print('')

student = {'name': 'Niklas', 'age': '21', 'courses': 'Hackerseminar'}
print(student)
print(student['name'])
student.update({'name': 'Nils', 'age': '24'})
print(student)
for key, value in student.items():
    print(key, value)
