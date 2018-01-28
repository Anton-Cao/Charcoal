from flask import Flask, render_template, request, jsonify
from predict import predict_next_chars as pnc
from predict import generate_story as gs

app = Flask(__name__)
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/rec', methods=['GET'])
def update():
    story = request.args.get('story')
    next_chars = pnc(story)
    return jsonify(next_chars)

@app.route('/story', methods=['GET'])
def story():
    seed = request.args.get('seed')
    length = int(request.args.get('length'))
    creativity = int(request.args.get('creativity'))
    length = min(length, 500)
    creativity = min(creativity, 5)
    return gs(seed, length, creativity)

if __name__ == '__main__':
    app.run(debug=True)
