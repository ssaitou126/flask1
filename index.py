from flask import Flask, render_template

app = Flask(__name__, static_folder='./templates/images')

a=30
b=4

@app.route('/')
def index():
    city = '滝沢'
    calc=a+b
    return render_template('index.html',name="斉藤さん",city=city,calc=calc)

@app.route('/sub1')
def sub1():
    return render_template('sub1.html')



if __name__ == '__main__':
    app.run()