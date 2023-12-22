from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/calculamedia')
def calcular_med():
    return render_template('ccmed.html')

@app.route('/ccrec')
def CCRec():
    return render_template('ccrec.html')

if __name__ =='__main__':
    app.run(debug=True)