from flask import Flask, render_template, request, jsonify
from predict import predict_next_chars as pnc

app = Flask(__name__)
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def update():
    story = request.json['story']
    next_chars = pnc(story)
    return jsonify(next_chars)

if __name__ == '__main__':
    app.run(debug=True)
