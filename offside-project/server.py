from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect, url_for
app = Flask(__name__)


lessons = {
    "1": {
        "number": "1",
        "media": "https://i.ibb.co/TKhYwTP/Screenshot-2024-04-16-at-22-54-52.png",
        "title": "The Definition",
        "description": "A player is in an offside position when an attacking player is nearer to the opponent’s goal line than both the ball and the second to last opponent."
        },
    "2": {
        "number": "2",
        "media": "youtube.com",
        "title": "The Basics",
        "description": "Only the team with possession of the ball can be offside. Offside can only occur on the attacking side of the field."
        },
    "3": {
        "number": "3",
        "media": "youtube.com",
        "title": "",
        "description": ""
        },
    "4": {
        "number": "4",
        "media": "youtube.com",
        "title": "",
        "description": ""
        },
    "5": {
        "number": "5",
        "media": "youtube.com",
        "title": "",
        "description": ""
        },
    "6": {
        "number": "6",
        "media": "youtube.com",
        "title": "",
        "description": ""
        },
    "7": {
        "number": "7",
        "media": "youtube.com",
        "title": "",
        "description": ""
        }
    }

learning_questions = {
   "1": {
      "number": "1",
      "media": "https://vimeo.com/935697965?share=copy"
   }
}
questions = {
    "1": {
        "Qnumber": "1",
        "media": "youtube.com"
        },
    "2": {
        "Qnumber": "2",
        "media": "youtube.com"
        },
    "3": {
        "Qnumber": "3",
        "media": "youtube.com"
        },
    "4": {
        "Qnumber": "4",
        "media": "youtube.com"
        },
    "5": {
        "Qnumber": "5",
        "media": "youtube.com"
        }
    }


# ROUTES
@app.route('/')
def homepage():
   return render_template('homepage.html')   

@app.route('/lesson/<number>')
def view_lesson(number):
   for item in lessons.values():
       if item['number'] == number:
           return render_template('lesson.html', item = item, lessons=lessons)
   return render_template('lesson.html')

@app.route('/quizStart')
def quiz_start():
   return render_template('quizStart.html')   

@app.route('/question/<Qnumber>')
def view_question(Qnumber):
   for item in questions.values():
       if item['Qnumber'] == Qnumber:
           return render_template('question.html', item = item, questions=questions)
   return render_template('question.html')   



if __name__ == '__main__':
   app.run(debug = True)




