from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['item']
        print(data)
        return render_template('index.html', items=[data])
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)