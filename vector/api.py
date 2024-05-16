from flask import Flask, request, jsonify
from base import answer_question

app = Flask(__name__)

@app.route('/qa', methods=['POST'])
def qa():
    # 获取 POST 请求中的数据
    data = request.json
    question = data['question']
    answer = answer_question(question)
    # 返回答案
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True,port=5001)
    print('Server running on port 5001...')
