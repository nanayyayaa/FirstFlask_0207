from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    biodata = None
    if request.method == 'POST':
        biodata = {
            'nama': request.form['nama'],
            'nim': request.form['nim'],
            'prodi': request.form['prodi'],
            'hobi': request.form['hobi'],
            'avatar': request.form['avatar']
        }
    return render_template('index.html', biodata=biodata)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')