from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def main():
    question_bank = [Question(x['question'], x['correct_answer'])
                     for x in question_data]
    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()
    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")


if __name__ == '__main__':
    main()
