group = [
    {
        'character': ['Igor', 'Danilov', 'male', 'experienced'],
        'home_work': [5, 4, 4, 3, 5, 5, 4, 5, 5, 4],
        'exam': 5
    },
    {
        'character': ['Igor', 'Danilov', 'male', 'experienced'],
        'home_work': [3, 4, 3, 4, 3, 3, 3, 5, 2, 4],
        'exam': 3
    },
    {
        'character': ['Mihail', 'Donskoy', 'male', 'inexperienced'],
        'home_work': [5, 3, 4, 3, 5, 4, 4, 4, 5, 3],
        'exam': 4
    },
    {
        'character': ['Lev', 'Korolev', 'male', 'experienced'],
        'home_work': [5, 4, 5, 5, 5, 5, 4, 5, 5, 4],
        'exam': 5
    },
    {
        'character': ['Erna', 'Shaider', 'female', 'experienced'],
        'home_work': [5, 2, 3, 3, 5, 5, 4, 5, 5, 4],
        'exam': 5
    },
    {
        'character': ['Karen', 'Spark', 'female', 'inexperienced'],
        'home_work': [2, 3, 4, 5, 5, 5, 4, 4, 5, 4],
        'exam': 4
    },
    {
        'character': ['Tupac', 'Shakur', 'male', 'inexperienced'],
        'home_work': [2, 3, 3, 3, 4, 4, 3, 4, 4, 3],
        'exam': 3
    },
]


def average_score_hw(feature, text, exp):
    total_score = 0
    the_number = 0
    for student in group:
        if student['character'][2] == feature and student['character'][3] == exp:
            total_score += sum(student['home_work']) / len(student['home_work'])
            the_number += 1
    print(text, round(total_score / the_number, 2))
    action_choise()


def average_score_exam(feature, text, exp):
    total_score = 0
    the_number = 0
    for student in group:
        if student['character'][2] == feature:
            total_score += student['exam']
            the_number += 1
    print(text, round(total_score / the_number, 2))
    action_choise()


def best_students():
    final_scores = []
    best_students = []

    for student in group:
        final_score = round((0.6 * (sum(student['home_work']) / len(student['home_work'])) + 0.4 * (student['exam'])),
                            2)
        final_scores.append(final_score)
    m = max(final_scores)

    q = 0
    while m in final_scores:
        x = final_scores.index(m) + q
        best_student = (str(group[x]['character'][0] + group[x]['character'][1]))
        best_students.append(best_student)
        final_scores.remove(m)
        q += 1

    if len(best_students) == 1:
        print('Лучший студент: {} с интегральной оценкой {}'.format(best_students[0], m))
    else:
        print('Лучшие студенты:', end=' ')
        for s in best_students:
            print(s, end=' ')
            print('с интегральной оценкой {}'.format(m))
    action_choise()


def action_choise():
    print('выберете действие:')
    action_choise = input()

    if action_choise.lower() == 'x':
        feature = 'male' or 'female'
        exp = 'experienced' or 'inexperienced'
        text = 'Средняя оценка за домашние задания по группе:'
        average_score_hw(feature, text, exp)
    elif action_choise.lower() == 'y':
        feature = 'male' or 'female'
        exp = 'experienced' or 'inexperienced'
        text = 'Средняя оценка за экзамен:'
        average_score_exam(feature, text, exp)
    elif action_choise.lower() == 'a':
        feature = 'male'
        exp = 'experienced' or 'inexperienced'
        text = 'Средняя оценка за домашние задания у мужчин:'
        average_score_hw(feature, text, exp)
    elif action_choise.lower() == 'b':
        feature = 'male'
        exp = 'experienced' or 'inexperienced'
        text = 'Средняя оценка за экзамен у мужчин:'
        average_score_exam(feature, text, exp)
    elif action_choise.lower() == 'c':
        feature = 'female'
        exp = 'experienced' or 'inexperienced'
        text = 'Средняя оценка за домашние задания у женщин:'
        average_score_hw(feature, text, exp)
    elif action_choise.lower() == 'd':
        feature = 'female'
        exp = 'experienced' or 'inexperienced'
        text = 'Средняя оценка за экзамен у женщин:'
        average_score_exam(feature, text, exp)
    elif action_choise.lower() == 'e':
        feature = 'male' or 'female'
        exp = 'experienced'
        text = 'Средняя оценка за домашние задания у студентов с опытом:'
        average_score_hw(feature, text, exp)
    elif action_choise.lower() == 'f':
        feature = 'male' or 'female'
        exp = 'experienced'
        text = 'Средняя оценка за экзамен у студентов с опытом:'
        average_score_exam(feature, text, exp)
    elif action_choise.lower() == 'g':
        feature = 'male' or 'female'
        exp = 'inexperienced'
        text = 'Средняя оценка за домашние задания у студентов без опыта:'
        average_score_hw(feature, text, exp)
    elif action_choise.lower() == 'h':
        feature = 'male' or 'female'
        exp = 'inexperienced'
        text = 'Средняя оценка за экзамен у студентов без опыта:'
        average_score_exam(feature, text, exp)
    elif action_choise.lower() == 'i':
        best_students()


print('Здравствуйте!')
action_choise()
