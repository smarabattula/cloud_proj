from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    if request.method == 'POST':
        # Process the input text (you can add text-to-image generation logic here)
        input_text = request.form['inputText']

        # For now, let's just pass the input text to the result template
        return render_template('result.html', input_text=input_text)

if __name__ == '__main__':
    app.run(host = "0.0.0.0",debug=True)
