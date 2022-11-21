from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/projetos')
def projetos():
    return render_template('projetos.html')


@app.route('/sobremim')
def sobremim():
    return render_template('sobremim.html')

@app.route('/projetoum')
def projetoum():
    return render_template('ProjetoPynk.html')

@app.route('/projetodois')
def projetodois():
    return render_template('projetounes.html')

@app.route('/projetotres')
def projetotres():
    return render_template('projetotecblog.html')

@app.route('/projetoquatro')
def projetoquatro():
    return render_template('projetodesign.html')


if __name__ == "__main__":
    app.run(debug=True)