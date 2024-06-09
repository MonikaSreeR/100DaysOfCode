from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_bank=[]
for dict1 in question_data:  
  Question_bank.append(Question(dict1["text"],dict1["answer"]))


Quiz = QuizBrain(Question_bank)
while Quiz.still_has_questions():
  Quiz.new_question()
score = Quiz.score
q_number =Quiz.question_number

print("You completed the quiz!")
print(f"Your final score is {score}/{q_number}")

#question_model.py
class Question:
  def __init__(self,text,answer):
    self.text = text
    self.answer = answer
#data.py
question_data = [
  {"text": "A slug's blood is green.", "answer": "True"},
  {"text": "The loudest animal is the African Elephant.", "answer": "False"},
  {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
  {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
  {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
  {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
  {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
  {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
  {"text": "Google was originally called 'Backrub'.", "answer": "True"},
  {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
  {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
  {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]
Quiz_brain.py
class QuizBrain:
  def __init__(self,question_list):
    self.question_number =0
    self.question_list = question_list
    self.score =0

  def check_answer(self,user_answer, answer):
    return user_answer.lower()==answer.lower()

  def new_question(self):
    question = self.question_list[self.question_number]
    text = question.text
    answer = question.answer  
    self.question_number+=1
    user_answer = input(f"Q.{self.question_number}. {text} (True/False): ")    
    result = self.check_answer(user_answer, answer)
    if result:
      self.score+=1
      print(f"You got it right! Your score is {self.score}/{self.question_number}")
    else:
      print(f"You got it wrong! The answer is {answer} and your score is {self.score}/{self.question_number}")    
    print()     
    
  def still_has_questions(self):
    return self.question_number < len(self.question_list)

    
