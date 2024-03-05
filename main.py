from flask import Flask, render_template, request
from animalgpt.prediction import Prediction

app = Flask(__name__)


# Load the fine-tuned model and tokenizer
prediction = Prediction()
# Initialize conversation history
conversation_history = ""

@app.route('/', methods=['GET', 'POST'])
def index():
    global conversation_history

    if request.method == 'POST':
        user_input = request.form['user_input']

        if user_input:
            # Combine user input with conversation history
            input_text = user_input

            # Generate response
            response = prediction.predict(input_text)

            return render_template('index.html', user_input=user_input, response=response, conversation_history=conversation_history)

    return render_template('index.html', user_input="", response="", conversation_history=conversation_history)


if __name__ == "__main__":
    app.run()