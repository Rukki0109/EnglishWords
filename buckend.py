from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  # CORSポリシーを許可する

# サンプル単語リスト
words = [
    {"word": "example", "meaning": "an instance serving as a model"},
    {"word": "study", "meaning": "devote time to learning"},
    {"word": "language", "meaning": "method of human communication"},
    {"word": "customer", "meaning": "client, buyer"},
    {"word": "servant", "meaning": "employee, helper"},
    {"word": "display", "meaning": "exhibit, show, presentation"},
    {"word": "president", "meaning": "chief executive, head of state"},
    {"word": "delivery", "meaning": "distribution, dispatch"},
    {"word": "interview", "meaning": "meeting, consultation"},
    {"word": "receipt", "meaning": "proof of purchase, acknowledgment"},
    {"word": "engineer", "meaning": "designer, planner"},
    {"word": "dealer", "meaning": "trader, merchant"},
    {"word": "path", "meaning": "trail, route, way"},
    {"word": "credit card", "meaning": "payment card"},
    {"word": "court", "meaning": "tribunal, judiciary"},
    {"word": "copyright", "meaning": "intellectual property rights"},
    {"word": "consultant", "meaning": "advisor, expert"},
    {"word": "composer", "meaning": "writer of music"},
    {"word": "secretary", "meaning": "administrative assistant, clerk"},
    {"word": "seminar", "meaning": "conference, symposium"},
    {"word": "laborer", "meaning": "worker, manual worker"},
    {"word": "message", "meaning": "communication, statement"},
    {"word": "journalist", "meaning": "reporter, correspondent"},
    {"word": "employer", "meaning": "boss, manager"},
    {"word": "lawyer", "meaning": "attorney, counsel"},
    {"word": "architect", "meaning": "one who designs buildings"},
    {"word": "nurse", "meaning": "healthcare professional"},
    {"word": "teacher", "meaning": "educator, instructor"},
    {"word": "scientist", "meaning": "expert in science"},
    {"word": "musician", "meaning": "person who plays a musical instrument"},
    {"word": "artist", "meaning": "creative individual"},
    {"word": "chef", "meaning": "professional cook"},
    {"word": "engineer", "meaning": "professional in engineering"},
    {"word": "writer", "meaning": "one who writes"},
    {"word": "pilot", "meaning": "one who operates the flight controls of an aircraft"},
    {"word": "athlete", "meaning": "person skilled in sports"},
    {"word": "actor", "meaning": "performer in film or theater"},
    {"word": "politician", "meaning": "person involved in politics"},
    {"word": "photographer", "meaning": "one who takes photographs professionally"},
    {"word": "designer", "meaning": "one who designs"},
    {"word": "entrepreneur", "meaning": "one who starts a business"},
    {"word": "veterinarian", "meaning": "animal doctor"},
    # 他の単語を続けて追加...
]

@app.route('/words', methods=['GET', 'POST'])
def handle_words():
    if request.method == 'GET':
        # 単語リストを取得
        return jsonify(words)
    elif request.method == 'POST':
        # 新しい単語を追加
        word_data = request.json
        words.append(word_data)
        return jsonify(word_data), 201

@app.route('/words/<int:index>', methods=['PUT', 'DELETE'])
def handle_word(index):
    if index >= len(words) or index < 0:
        abort(404)  # 該当する単語がなければ404エラー

    if request.method == 'PUT':
        # 単語を更新
        word_data = request.json
        words[index] = word_data
        return jsonify(word_data)

    elif request.method == 'DELETE':
        # 単語を削除
        word = words.pop(index)
        return jsonify(word)

    return '', 204  # PUT/DELETE以外の場合は204 No Contentを返す

@app.route('/get-word', methods=['GET'])
def get_word():
    return jsonify(random.choice(words))

if __name__ == '__main__':
    app.run(debug=True)

