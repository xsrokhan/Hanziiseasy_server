from flask import Flask, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/get_chars', methods=['GET'])
def get_chars():
    processed_chars = read_file("processed_chars.txt")
    return jsonify(processed_chars)


@app.route('/search_dict/<char>')
def get_words(char):
    processed_dict = read_file("processed_dict.txt")
    words = []
    for word in processed_dict:
        if (char in word['simplified'] and (len(word['simplified']) > 1 and len(word['simplified']) <= 5)):
            words.append(word)
    return jsonify(words)


def read_file(file_name):
    dict_list = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
          line = line.rstrip()
          line = json.loads(line)
          dict_list.append(line)
    return dict_list


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)














