from dotenv import load_dotenv
load_dotenv("animal.env")

from flask import Flask, render_template, request, jsonify, session

import pandas as pd
import time
import numpy as np
import uuid
from animal_gpt.predict.core import Prediction

from  animal_gpt.utils.bq_class import BQ
from  animal_gpt.utils.config import (
    default_logs_db
)
from animal_gpt.utils.logger import log

app = Flask(__name__)

model_path = "dkandpalz/animalGPT1"
predict = Prediction(model_path)
conversation_history = ""
collect_info = {}
app.secret_key = 'your_secret_key_here'


@app.route('/', methods=['GET', 'POST'])
def index():
    global conversation_history

    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            user_input = data.get('user_input')
        else:
            user_input = request.form.get('user_input')

        if user_input:
            # Combine user input with conversation history
            input_text = user_input

            # Generate response
            output, probabilities, predicted_prompt = predict.create_prediction(input_text)
            session['collect_info'] = {
                "probabilities": str(probabilities), 
                "predicted_prompt": predicted_prompt,
                "output": output,
                "input": input_text
            }
            print(f"collect_info: {session['collect_info']}")
            return jsonify({'response': output})
        else:
            return jsonify({'response': ""})

    return render_template('index.html', user_input=collect_info.get('input_text'), response=collect_info.get('input_text'), conversation_history=conversation_history)

@app.route('/thumbs_feedback', methods=['POST'])
def thumbs_feedback():
    # Handle thumbs-up and thumbs-down feedback here
    thumbs_value = request.json.get('thumbs_value', '0')  # Default to '0' if not provided
    collect_info = session.get('collect_info', {})

    # Log the thumbs-up/thumbs-down feedback (you can add this to the log as needed)
    print(f"Received thumbs feedback for user input '{collect_info.get('input')}': {thumbs_value}")
    print(f"Received probabilities, predicted_prompt for user input '{float(collect_info.get('probabilities'))}': '{collect_info.get('predicted_prompt')}'")
    return jsonify({'status': 'success'})


if __name__ == "__main__":
    app.run()
