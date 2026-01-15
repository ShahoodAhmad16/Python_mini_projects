student_name = input('Enter your name')
subjects = []
marks_list = []
for subject in range(1, 6):
    student_subjects = input(f'Please enter subject one {subject}')
    subjects.append(student_subjects)

for mark in subjects:
    marks = int(input(f'Pleas enter marks for {mark}'))
    marks_list.append(marks)


def calculate_total(marks):
    total = 0
    for t in marks:
        total += t
    return total


def calculate_average(marks):
    return calculate_total(marks_list)/len(marks_list)


def grades():
    average = calculate_average(marks_list)
    if average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'


def reposrt_card():
    return f''' Student Name: {student_name}
Total Marks: {calculate_total(marks_list)}
Average: {calculate_average(marks_list)}
Grades: {grades()}
'''


reportCard = reposrt_card()
print(reportCard)
