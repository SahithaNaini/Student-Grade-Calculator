def calculate_average_score(student_scores):
    total_score = sum(student_scores.values())
    average_score = total_score / len(student_scores)
    return average_score


def find_student_with_highest_score(student_scores):
    highest_score = max(student_scores.values())
    highest_score_students = [student for student, score in student_scores.items() if score == highest_score]
    return highest_score_students


def main():
    student_scores = {}
    num_students = int(input("Enter the number of students: "))

    for i in range(num_students):
        name = input("Enter the name of student {}: ".format(i+1))
        score = float(input("Enter the score of student {}: ".format(i+1)))
        student_scores[name] = score

    average_score = calculate_average_score(student_scores)
    print("Average score: {:.2f}".format(average_score))

    highest_score_students = find_student_with_highest_score(student_scores)
    if len(highest_score_students) == 1:
        print("Student with the highest score: {}".format(highest_score_students[0]))
    else:
        print("Students with the highest score:")
        for student in highest_score_students:
            print(student)


if __name__ == "__main__":
    main()
