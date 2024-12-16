import time
from flask import Flask, Response

app = Flask(__name__)

# 生成流式数据
def generate_data():
    for i in range(10):
        yield f"data: data {i}\n\n"  # SSE 格式的数据
        time.sleep(1)

@app.route('/stream')
def stream():
    return Response(generate_data(), content_type='text/event-stream')  # 设置为 'text/event-stream'

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
