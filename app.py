from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/ML_FEATURES_APPLIED')
def ML_FEATURES_APPLIED():
    return render_template("FeaturesApplied.html")

if __name__ == '__main__':
    app.run(debug=True)

