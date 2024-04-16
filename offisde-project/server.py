from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, redirect, url_for
app = Flask(__name__)


# ROUTES

@app.route('/')
def homepage():
   return render_template('homepage.html')   

@app.route('/lesson1')
def lesson1():
   return render_template('lesson1.html')   

@app.route('/lesson2')
def lesson2():
   return render_template('lesson2.html') 

@app.route('/lesson3')
def lesson3():
   return render_template('lesson3.html') 

@app.route('/lesson4')
def lesson4():
   return render_template('lesson4.html') 

@app.route('/lesson5')
def lesson5():
   return render_template('lesson5.html') 


@app.route('/lesson6')
def lesson6():
   return render_template('lesson6.html') 


@app.route('/lesson7')
def lesson7():
   return render_template('lesson7.html') 

# @app.route('/results', methods=['GET', 'POST'])
# def display_results():
#     if request.method == 'POST':
#         search_text = request.form['search']
#         return redirect(url_for('results', search=search_text))
#     else:
#         search_text = request.args.get('search')

#         search_result_data =  {key: value for key, value in data.items() if search_text.lower() in value['name'].lower()}
#         return render_template('display_results.html', search=search_text, data = search_result_data)
    

# @app.route('/view/<id>')
# def view_item(id):
#     # Assuming 'data' is your dictionary of items
#     item = next((item for item in data.values() if item['id'].lower() == id), None)

#     # print(item, " is a " , type(item))
    
#     return render_template('view.html', item=item, data = data)
    



if __name__ == '__main__':
   app.run(debug = True)




