from flask import Flask, render_template

app = Flask(__name__)
print(__name__)

@app.route('/') #root directory
def main_page():
    return render_template('index.html')
    #When we use render_template flask is automatically looking for 'templates' folder
    

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# @app.route('/favicon.ico')
# def blog():
#     return 'This will be my blog'