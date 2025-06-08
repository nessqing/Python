from flask import Flask
app  = Flask(__name__)

@app.route('/')
def index():
    return "首頁"

@app.route('/product')
def product():
    return "產"

if __name__=='__main__':
    app.run(use_reloader=True)