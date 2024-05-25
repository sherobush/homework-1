import json
import os

questions_file = 'questions.json'
results_file = 'results.json'

# اقرأ الأسئلة والأجوبة من ملف JSON
with open(questions_file, 'r') as file:
    data = json.load(file)
    questions = [(item['question'], item['answer']) for item in data]

# اطرح الأسئلة على المستخدم وجمع الإجابات
username = input("أدخل اسم المستخدم: ").strip()
correct_answers = 0
for question, correct_answer in questions:
    user_answer = input(f"{question}? ").strip()
    if user_answer == correct_answer:
        correct_answers += 1
total_questions = len(questions)
print(f"{username}, لقد أجبت بشكل صحيح على {correct_answers} من أصل {total_questions} سؤال.")
# حفظ اسم المستخدم والنتيجة في ملف بصيغة JSON
result = {
    "name": username,
    "score": correct_answers,
    "of": total_questions
}

if not os.path.isfile(results_file):
    with open(results_file, 'w') as file:
        json.dump([result], file)
else:
    try:
        with open(results_file, 'r+') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []
            data.append(result)
            file.seek(0)
            json.dump(data, file)
    except FileNotFoundError:
        with open(results_file, 'w') as file:
            json.dump([result], file)