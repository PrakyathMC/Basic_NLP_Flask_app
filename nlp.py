from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    response = generate_pleasantry_response(user_message)
    return jsonify({'response': response})

def generate_pleasantry_response(input_text):
    input_text = input_text.lower()
    if 'hello' in input_text or 'hi' in input_text:
        return 'Hello there! How can I assist you today?'
    elif 'how are you' in input_text:
        return "I'm fine, thank you! How are you?"
    elif 'goodbye' in input_text or 'bye' in input_text:
        return 'Goodbye! Have a great day!'
    else:
        return "That's nice. Tell me more!"

if __name__ == '__main__':
    app.run(debug=True)
