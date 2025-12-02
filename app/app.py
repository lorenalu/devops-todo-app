from flask import Flask, jsonify, request
app = Flask(__name__)
TODOS = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(TODOS)

@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.json.get('todo')
    if todo:
        TODOS.append(todo)
        return jsonify({'message': 'Added!'}), 201
    return jsonify({'error': 'No todo provided'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)