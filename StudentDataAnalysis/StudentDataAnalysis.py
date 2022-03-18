def calculate_highest_in_maths(student_list):
    highest_score_in_Maths = 0
    highest_score_in_Maths_name = ' '
    for student in student_list:
        if (student.get('Maths') > highest_score_in_Maths):
            highest_score_in_Maths = student.get('Maths')
            highest_score_in_Maths_name = student.get('name')

    print(f"The highest scorer in Maths is {highest_score_in_Maths} by {highest_score_in_Maths_name}")

def calculate_highest_in_Science(student_list):
    highest_score_in_Science = 0
    highest_score_in_Science_name = ' '
    for student in student_list:
        if (student.get('Science') > highest_score_in_Science):
            highest_score_in_Science = student.get('Science')
            highest_score_in_Science_name = student.get('name')

    print(f"The highest scorer in Science is {highest_score_in_Science} by {highest_score_in_Science_name}")

def calculate_highest_in_Social(student_list):
    highest_score_in_Social = 0
    highest_score_in_Social_name = ' '
    for student in student_list:
        if (student.get('Social') > highest_score_in_Social):
            highest_score_in_Social = student.get('Social')
            highest_score_in_Social_name = student.get('name')

    print(f"The highest scorer in Social is {highest_score_in_Social} by {highest_score_in_Social_name}")



student_1 = {
    'Maths' : 45,
    'Social' : 75,
    'Science' : 96,
    'name': 'Tanmay'
}

student_2 = {
    'Maths' : 74,
    'Social' : 83,
    'Science' : 100,
    'name': 'Dheeraj'
}

student_3 = {
    'Maths' : 98,
    'Social' : 61,
    'Science' : 20,
    'name': 'Sooraj'
}

student_list = [student_1,student_2,student_3]

calculate_highest_in_maths(student_list)
calculate_highest_in_Science(student_list)
calculate_highest_in_Social(student_list)



