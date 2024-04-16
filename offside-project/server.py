from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect, url_for
app = Flask(__name__)

lessons = {
    "1": {
        "number": "1",
        "media": "youtube.com"
        },
    "2": {
        "number": "2",
        "media": "youtube.com"
        },
    "3": {
        "number": "3",
        "media": "youtube.com"
        },
    "4": {
        "number": "4",
        "media": "youtube.com"
        },
    "5": {
        "number": "5",
        "media": "youtube.com"
        },
    "6": {
        "number": "6",
        "media": "youtube.com"
        },
    "7": {
        "number": "7",
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



if __name__ == '__main__':
   app.run(debug = True)




