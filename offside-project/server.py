from flask import Flask
from flask import render_template
# from flask_talisman import Talisman
from flask import Response, request, jsonify, redirect, url_for
app = Flask(__name__)

# talisman = Talisman(app, content_security_policy={
#     'default-src': [
#         '\'self\'',
#         'https://player.vimeo.com',
#         # Other domains your site needs access to
#     ],
#     'script-src': [
#         '\'self\'',
#         'https://player.vimeo.com',  # Allow scripts from Vimeo
#         # Additional script sources
#     ]
# })

# maxi comment for test purposes

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
        "learningQuestionId" : "",
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
        "media": "https://player.vimeo.com/935697965?share=copy",
        "title": "Exceptions to the rule",
        "description": "An offside is not called in the 3 following scenarios: goal kick, corner kick, throw in",
        "learningQuestionId" : "3",
        }
    }


questions = {
    "1": {
        "Qnumber": "1",
        "type": "quiz", 
        "content": "Is the following goal offside?", 
        "options": ["Yes", "No"], 
        "media": "https://player.vimeo.com/935697965?share=copy", 
        "answer": "Yes", 
        "explanation": ["Yes: The Manchester City is indeed offside when the ball is PASSED by his teammate. Review Nuance #5.", "Incorrect"]
        },
    "2": {
        "Qnumber": "2",
        "type": "quiz", 
        "content": "Why is the following goal offside?", 
        "options": ["Mbappe was in front of the ball", "Mbappe received the ball behind the last defender", "Mbappe did not touch the ball in front of the goalkeeper", "Mbappe received the ball in front of the second to last player"], 
        "media": "https://player.vimeo.com/935697965?share=copy", 
        "answer": "Mbappe received the ball in front of the second to last player", 
        "explanation": ["This only applies if the passer is in front of the last defender", "Where the attacker receives the ball doesn’t matter. Nuance #5", "This is not a rule", "Correct!"]
        },
    "3": {
        "Qnumber": "3",
        "type": "quiz", 
        "content": "Is the following goal offside?", 
        "options": ["Yes, because Messi is standing in front of the second to last defender when the ball is passed ", "Yes, because Messi is interfering with the play while standing in front of the second to last defender", "No, because the Pedro is standing behind the ball when the ball is passed and Messi does not interfere with the play", "No, because although Messi is standing in an offside position when the ball is passed, he is unaware it is being passed"], 
        "media": "https://player.vimeo.com/935697965?share=copy", 
        "answer": "No, because the Pedro is standing behind the ball when the ball is passed and Messi does not interfere with the play", 
        "explanation": ["This is not sufficient for an off-side call, nuance #1 active involvement is required", "There was no active involvement", "Correct!", "This is not a rule"]
        }
    }

learning_questions = {
            "1": {
                "learningQuestionId": "1",
                "lessonNumber": "2",
                "content": "Is this offiside?", 
                "options": ["Yes", "No"], 
                "media": "https://player.vimeo.com/935697965?share=copy", 
                "answer": "No", 
                "explanation": ["Incorrect", "Correct! As mentioned in the basics: offside can only occur on the attacking side of the field. However, here Torres is on the defending half of the field when the pass is made!"]
                },
            "2": {
                "learningQuestionId": "2",
                "lessonNumber": "3", 
                "content": "Is this offiside?", 
                "options": ["Yes", "No"], 
                "media": "https://player.vimeo.com/935697965?share=copy", 
                "answer": "Yes", 
                "explanation": ["Correct! As mentioned in nuance #1: It’s offside if the player is actively involved! Here, Griezmann is offside when the pass is made and even though he doesn’t directly get the ball, he was actively involved in the play and in an offside position when the ball was passed!", "Incorrect"]
                },
            "3": {
                "learningQuestionId": "3",
                "lessonNumber": "7", 
                "content": "Is this offside?", 
                "options": ["Yes", "No"],
                "media": "https://player.vimeo.com/935697965?share=copy", 
                "answer": "No", 
                "explanation": ["Incorrect", "The correct answer is NO! While Suarez is indeed offside when the “pass” is made, it comes from a throw-in!  Thus, the offside rule is not applicable and the goal is valid!"]
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
    score = request.args.get('score', default=0, type=int)
    return render_template('quizresults.html', score=score)


if __name__ == '__main__':
   app.run(debug = True, port=4000)




