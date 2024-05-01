from flask import Flask
from flask import render_template
from flask import session
from flask import Response, request, jsonify, redirect, url_for
app = Flask(__name__)

app.secret_key = 'secret'

lessons = {
    "1": {
        "number": "1",
        "media": "https://i.ibb.co/TKhYwTP/Screenshot-2024-04-16-at-22-54-52.png",
        "title": "The Definition",
        "description": "A player is in an offside position when an attacking player is nearer to the opponent’s goal line than both the ball and the second to last opponent.",
        "learningQuestionId" : "",
        },
    "2": {
        "number": "2",
        "media": "https://i.ibb.co/NyQZcCf/Screenshot-2024-04-16-at-11-22-25-PM.png",
        "title": "The Basics",
        "description": "Only the team with possession of the ball can be offside. Offside can only occur on the attacking side of the field.",
        "learningQuestionId" : "1",
        },
    "3": {
        "number": "3",
        "media": "https://i.ibb.co/4jSdLbn/Screenshot-2024-04-16-at-11-10-03-PM.png",
        "title": "Nuance #1: Active Involvement Required",
        "description": "Being in an offside position is NOT an infraction in itself. It’s only an infraction if the attacking player is offside AND is actively involved in the play.",
        "learningQuestionId" : "2",
        },
    "4": {
        "number": "4",
        "media": "https://i.ibb.co/jk5bcj9/Screenshot-2024-04-16-at-11-15-05-PM.png",
        "title": "Nuance #2: Behind The Ball",
        "description": "If the ball is behind the second to last player, it becomes itself the offside line and cannot be played to a player in front. ",
        "learningQuestionId" : "3",
        },
    "5": {
        "number": "5",
        "media": "https://i.ibb.co/NZJTD1v/Screenshot-2024-04-16-at-11-19-57-PM.png",
        "title": "Nuance #3: Arms And Hands Don’t Count!",
        "description": "The offside gets called if any part of the body, not including the arms and hands is in front of the offside line.",
        "learningQuestionId" : "",
        },
    "6": {
        "number": "6",
        "media": "https://i.ibb.co/Ryhjhn7/Screenshot-2024-04-16-at-11-25-27-PM.png",
        "title": "Nuance #4: At the Time of Passing",
        "description": "We determine whether or not the player is offside based on the exact moment when the ball is PASSED. A player can be offside when receiving the ball but not when the ball is passed.",
        "learningQuestionId" : "",
        },
    "7": {
        "number": "7",
        "media": "https://player.vimeo.com/video/938401528?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479",
        "title": "Exceptions to the rule",
        "description": "An offside is not called in the 3 following scenarios: goal kick, corner kick, throw in",
        "learningQuestionId" : "4",
        }
    }


questions = {
    "1": {
        "Qnumber": "1",
        "type": "quiz", 
        "content": "Is the following goal offside?", 
        "options": [{"text":"Yes", "correct":1, "explanation":"The Manchester City is indeed offside when the ball is PASSED by his teammate."},
                     {"text":"No", "correct":0, "explanation":"The Manchester City player is offside at the moment the ball was passed, so this is incorrect."}], 
        "media": "https://player.vimeo.com/video/938413075?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" 
        },
    "2": {
        "Qnumber": "2",
        "type": "quiz", 
        "content": "Why is the following goal offside?", 
        "options": [{"text":"Mbappe (#7) was in front of the ball", "correct":0, "explanation":"This only applies if the passer is in front of the last defender"}, 
                    {"text":"Mbappe (#7) received the ball behind the last defender", "correct":0, "explanation":"Where the attacker receives the ball doesn’t matter. Nuance #5"}, 
                    {"text":"Mbappe (#7) did not touch the ball in front of the goalkeeper","correct":0, "explanation":"This is not a rule"},
                    {"text":"Mbappe (#7) received the ball in front of the second to last player","correct":1, "explanation":"This is the definition of the offside rule. Correct!"}], 
        "media": "https://player.vimeo.com/video/938404474?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"
        },
    "3": {
        "Qnumber": "3",
        "type": "quiz", 
        "content": "Is the following goal offside?", 
        "options": [{"text":"Yes, because Messi (#10) is standing in front of the second to last defender when the ball is passed", "correct":0, "explanation":"This is not sufficient for an off-side call, nuance #1 active involvement is required"}, 
                    {"text":"Yes, because Messi (#10) is interfering with the play while standing in front of the second to last defender", "correct": 0, "explanation":"There was no active involvement"}, 
                    {"text":"No, because the Pedro (#7) is standing behind the ball when the ball is passed and Messi (#10) does not interfere with the play", "correct": 1, "explanation":"Correct!"},
                    {"text":"No, because although Messi (#10) is standing in an offside position when the ball is passed, he is unaware it is being passed", "correct": 0, "explanation":"This is not a rule"}], 
        "media": "https://player.vimeo.com/video/938410042?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479"
        }
    }

learning_questions = {
    "1": {
        "learningQuestionId": "1",
        "lessonNumber": "2",
        "content": "Is this offside?", 
        "options": [
            {"text": "Yes", "correct": 0, "explanation": "Incorrect.As mentioned in the basics: offside can only occur on the attacking side of the field. However, here the player is on the defending half of the field when the pass is made, so he is not offside."},
            {"text": "No", "correct": 1, "explanation": "Correct!As mentioned in the basics: offside can only occur on the attacking side of the field. However, here the player is on the defending half of the field when the pass is made, so he is not offside."}
        ], 
        "media": "https://www.youtube.com/embed/unQrPpo7ghs",
        "explanationMedia": "https://www.youtube.com/embed/69kg9DCjaPc"
    },
    "2": {
        "learningQuestionId": "2",
        "lessonNumber": "3", 
        "content": "Is this offside?", 
        "options": [
            {"text": "Yes", "correct": 0, "explanation": "Incorrect! Here, the offside player is not actively involved. This means the play as a whole is not offside."},
            {"text": "No", "correct": 1, "explanation": "Correct. As mentioned in nuance #1: Its offside if the player is actively involved! The offside player is not actively involved in the play, thus the play is not offside."}
        ],
        "media": "https://www.youtube.com/embed/BBZUwqiIDLM",
        "explanationMedia": "https://www.youtube.com/embed/64B26Rd9Q0U"
    },
    "3": {
        "learningQuestionId": "3",
        "lessonNumber": "4", 
        "content": "Is this offside?", 
        "options": [
            {"text": "Yes", "correct": 1, "explanation": "Correct! Once the player runs past the last defender, the ball becomes the offside line. Taking into account this new offside line, the last pass was offside."},
            {"text": "No", "correct": 0, "explanation": "Incorrect. Once the player runs past the last defender, the ball becomes the offside line. Taking into account this new offside line, the last pass was offside."}
        ],
        "media": "https://www.youtube.com/embed/1EylGU81Xas",
        "explanationMedia": "https://www.youtube.com/embed/qnbN9OggRuc"
    },
    "4": {
        "learningQuestionId": "4",
        "lessonNumber": "7", 
        "content": "Is this offside?", 
        "options": [
            {"text": "Yes", "correct": 0, "explanation": "Incorrect. While the player is indeed offside when the 'pass' is made, it comes from a throw-in! Thus, the offside rule is not applicable and the goal is valid!"},
            {"text": "No", "correct": 1, "explanation": "Correct! While the player is indeed offside when the 'pass' is made, it comes from a throw-in! Thus, the offside rule is not applicable and the goal is valid!"}
        ],
        "media": "https://www.youtube.com/embed/o5QkD71XdWE",
        "explanationMedia": "https://www.youtube.com/embed/O0dq70FsItQ"
    }
}


# ROUTES
@app.route('/')
def homepage():
   return render_template('homepage.html')   

@app.route('/lesson/<number>')
def view_lesson(number):
    lesson = lessons.get(number)
    if lesson:
        return render_template('lesson.html', item=lesson, lessons=lessons)
    else:
        return redirect(url_for('homepage'))

@app.route('/quizStart')
def quiz_start():
   return render_template('quizStart.html')   

@app.route('/learning_question/<Qnumber>')
def view_learning_question(Qnumber):
    question = learning_questions.get(Qnumber)
    if question:
        return render_template('learning_question.html', item=question, learning_questions=learning_questions)
    else:
        return redirect(url_for('quiz_start'))

@app.route('/question/<Qnumber>')
def view_question(Qnumber):
    question = questions.get(Qnumber)
    if question:
        return render_template('question.html', item=question, questions=questions)
    else:
        return redirect(url_for('quiz_start'))
    
@app.route('/quizresults')
def quiz_results():
    return render_template('quizresults.html')

################################

# SESSION ROUTES

@app.route('/init_score')
def init_score():
    session['score'] = 0
    return 'Score initialized'

@app.route('/increment_score')
def increment_score():
    session['score'] += 1
    return 'Score incremented'

@app.route('/get_score')
def get_score():
    return str(session.get('score', 0))

################################


if __name__ == '__main__':
   app.run(debug = True, port=4000)




