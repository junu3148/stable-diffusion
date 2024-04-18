from flask import Flask, request, jsonify
import subprocess
import shlex

app = Flask(__name__)

@app.route('/generate-image', methods=['POST'])
def generate_image():
    data = request.json
    prompt = data.get('prompt')
    print(prompt)
    
    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    try:
        # 리스트 형식으로 명령어와 인자를 분리하여 쉘 인젝션 방지
        command = ["python", "scripts/txt2img.py", "--prompt", prompt, "--plms"]
        # subprocess를 이용해 txt2img.py 스크립트를 실행합니다.
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        # 성공적으로 실행되면, 스크립트의 stdout을 반환합니다.
        return jsonify({'result': result.stdout})
    except subprocess.CalledProcessError as e:
        # 스크립트 실행 중 에러가 발생한 경우, stderr을 반환합니다.
        return jsonify({'error': e.stderr}), 500

if __name__ == '__main__':
    app.run(debug=True)
