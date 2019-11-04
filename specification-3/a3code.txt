from flask import Flask
app = Flask(__name__)
from flask import render_template

# 1)Read through the textfile which corresponds with each assessments code, and store the code as a variable
# 2)Create website pages with content based on the variables within the return function, which are passed to the html
#   templates.
@app.route('/')
def home():
    return render_template('index.html',
                           title='Home',
                           general_page_description='Welcome to the homepage of our website for our project.'
                                                    'You can use the navigation bar to find code for each assessment',
                           code='')
@app.route('/assessment_one')
def assessment_one():
    code = open('a1code.txt', 'r+')
    displaycode = code.read()
    code.close()
    return render_template('index.html',
                           title='Assessment One',
                           general_page_description='This is the page for assessment one.',
                           code=displaycode,
                           documentation='This is documentation')

@app.route('/assessment_two')
def assessment_two():
    code = open('a2code.txt', 'r+')
    displaycode = code.read()
    code.close()
    return render_template('index.html',
                           title='Assessment Two',
                           general_page_description='This is the page for assessment two.',
                           code=displaycode)

@app.route('/assessment_three')
def assessment_three():
    code = open('a3code.txt', 'r+')
    displaycode = code.read()
    code.close()
    return render_template('index.html',
                           title='Assessment Three',
                           general_page_description='This is the page for assessment three.',
                           code=displaycode)

@app.route('/assessment_four')
def assessment_four():
    code = open('a4code.txt', 'r+')
    displaycode = code.read()
    code.close()
    return render_template('index.html',
                           title='Assessment Four',
                           general_page_description='This is the page for assessment four.',
                           code=displaycode)

#Run program
if __name__ == '__main__':
    app.run()
