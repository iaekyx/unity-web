from flask import Flask, render_template
from flask_bootstrap import Bootstrap4

app = Flask(__name__)
# 创建bootstrap 对象
bootstrap = Bootstrap4(app)

@app.route('/index')
def index():
    return render_template('uploads.html')

if __name__ == '__main__':
    app.run(debug=True)
