import csv
import random
import json

students = {}
subjects = ["Art", "Math", "History", "Literature", "Science"]
grades = ["A", "B", "C", "F"]

with open("names.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        students[row[0]] = {"subjects": {}}
        for i in range(5):
            students[row[0]]["subjects"][subjects[i]] = "Not Enrolled"

        students[row[0]]["subjects"][random.choice(subjects)] = random.choice(grades)

        for i in range(4):
            r_choice = random.choice(subjects)
            if students[row[0]]["subjects"][r_choice] == "Not Enrolled":
                students[row[0]]["subjects"][r_choice] = random.choice(grades)

print(students)
print()

js = json.dumps(students)

with open("students.json", 'w') as json_file:
    json_file.write(js)

# Received help from this source:
# https://stackoverflow.com/questions/29400631/python-writing-nested-dictionary-to-csv
fields = ["Name", "Art", "Math", "History", "Literature", "Science"]

with open("students.csv", 'w') as stu_csv:
    dict_writer = csv.DictWriter(stu_csv, fields)
    dict_writer.writeheader()
    for i in students:
        dict_writer.writerow({field: students[i]["subjects"].get(field) or i for field in fields})

# OLD CODE
#
# students = []
# subjects = ["Art", "Math", "History", "Literature", "Science"]
# grades = ["A", "B", "C", "F"]
#
# with open("names.txt") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     line_count = 0
#     line_num = 1
#     for row in csv_reader:
#         # print(line_num, row)
#         line_num += 1
#         students.append({"name": row[0]})
#         students[line_count]["subjects"] = {}
#         students[line_count]["subjects"][(random.choice(subjects))] = random.choice(grades)
#
#         for i in range(4):
#             r_choice = random.choice(subjects)
#             if r_choice not in students[line_count]["subjects"]:
#                 students[line_count]["subjects"][r_choice] = random.choice(grades)
#
#         line_count += 1
# print(students)
# print()
#
# js = json.dumps(students)
#
# with open("students.json", 'w') as json_file:
#     json_file.write(js)
#
# keys = students[0].keys()
# with open("students.csv", 'w') as stu_csv:
#     dict_writer = csv.DictWriter(stu_csv, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(students)
