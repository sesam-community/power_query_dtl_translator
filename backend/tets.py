from flask import Flask, request, jsonify
import requests
import json

app           = Flask(__name__)


text_example = 'let Kilde = Csv.Documents(File.Contents("C:\Users\erik1\Doownloads\SampleCSVFile_2kb.csv"),[Delimiter=",", Columns=10, Encoding=1252, QuoteStyle=QuoteStyle.None]), #"Fjernede kolonner" = Table.RemoveColumns(Kilde, {"Columns1"}), '


@app.route('/transform', methods=['GET', 'POST'])
def transform(text):


if __name__ == '__main__':

    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)

