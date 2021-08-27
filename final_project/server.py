from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench(text:str):
    textToTranslate = request.args.get('textToTranslate')
    fr = translator.english_to_french(textToTranslate)
    return json.dumps(fr)

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    en =  translator.french_to_english(textToTranslate)
    return json.dumps(en)

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
