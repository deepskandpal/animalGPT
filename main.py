from flask import Flask, render_template, request
from transformers import AutoTokenizer, AutoModelForCausalLM


app = Flask(__name__)


# Load the fine-tuned model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("dkandpalz/animalGPT2")
model = AutoModelForCausalLM.from_pretrained("dkandpalz/animalGPT2")

# Set the model to evaluation mode
model.eval()
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
            response = generate_text(input_text)


            return render_template('index.html', user_input=user_input, response=response, conversation_history=conversation_history)

    return render_template('index.html', user_input="", response="", conversation_history=conversation_history)

def generate_text(input_text):
    inputs = tokenizer(input_text, return_tensors="pt")
    generated_response = model.generate(**inputs, max_new_tokens=100, do_sample=True, top_p=0.92, top_k=0,num_beams=5,no_repeat_ngram_size=2,num_return_sequences=5,)
    output = tokenizer.decode(generated_response[0], skip_special_tokens=True)
    return output

if __name__ == "__main__":
    app.run(debug=True,port=9810)
