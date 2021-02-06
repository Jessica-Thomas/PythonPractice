# course = {'teacher':'Ashley', 'title':'Introducing Dictionaries', 'level':'Beginner'}

# # for item in course:
# #     print(item)

# # for item in course:
# #     print(course[item])    

# # print(course.items())

# # for item in course.items():
# #     print(item)

# for key, value in course.items():
#     print(key, value)



def print_teacher(name, job, topic):
    print(name)
    print(job)
    print(topic)
    
# print_teacher('Ashley', 'Instructor', 'Python')

# print_teacher(name='Ashley', job='Instructor', topic='Python')

def print_teacher(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


print_teacher(name='Ashley', job='Instructor', topic='Python')
