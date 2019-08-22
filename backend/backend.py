from flask import Flask, request, jsonify
import sys
sys.path.append("/usr/local/lib/python2.7/dist-packages")
from flask_cors import CORS, cross_origin
import requests
import json
from transform.transform_methods import *

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, 
headers={'Access-Control-Request-Headers', 'Content-Type', 'Access-Control-Allow-Origin'})

#text_example = 'let Kilde = Csv.Documents(File.Contents("C:Userserik1DownloadsSampleCSVFile_2kb.csv"),[Delimiter=",", Columns=10, Encoding=1252, QuoteStyle=QuoteStyle.None]), #"Fjernede kolonner" = Table.RemoveColumns(Kilde, {"Column9"} in #"Text med store bokstaver"'
#text_example = 'let Kilde = Csv.Documents(File.Contents("C:Userserik1DownloadsSampleCSVFile_2kb.csv"),[Delimiter=",", Columns=10, Encoding=1252, QuoteStyle=QuoteStyle.None]), #"Fjernede kolonner" = Table.RemoveColumns(Kilde, {"Column9"}), #"Text med store bokstaver" = Table.TransformColumns(#"Fjernede kolonner", {{"Column2", Text.Upper, type text}}) in #"Text med store bokstaver"'
#text_example = 'let Kilde = Csv.Documents(File.Contents("C:Userserik1DownloadsSampleCSVFile_2kb.csv"),[Delimiter=",", Columns=10, Encoding=1252, QuoteStyle=QuoteStyle.None]), #"Fjernede kolonner" = Table.RemoveColumns(Kilde, {"Column9"}), #"Text med store bokstaver" = Table.TransformColumns(#"Fjernede kolonner", {{"Column2", Text.Upper, type text}}), #"Filtrerte rader" = Table.SelectRows(#"Text med store bokstaver", each ([Column1] <> "1")) in #"Text med store bokstaver"'
#text_example = 'let Kilde = Csv.Documents(File.Contents("C:Userserik1DownloadsSampleCSVFile_2kb.csv"),[Delimiter=",", Columns=10, Encoding=1252, QuoteStyle=QuoteStyle.None]), #"Fjernede kolonner" = Table.RemoveColumns(Kilde, {"Column9"}), #"Text med store bokstaver" = Table.TransformColumns(#"Fjernede kolonner", {{"Column2", Text.Upper, type text}}), #"Filtrerte rader" = Table.SelectRows(#"Text med store bokstaver", each ([Column1] <> "1")), #"Filtrerte rader1" = Table.SelectRows(#"Filtrerte rader", each [Column1] = "3") in #"Text med store bokstaver"'
#words = text_example.split()

#text_example = 'let    #"Filtrerte rader" = Table.SelectRows(Kilde, each [Column4] = "613") in   #"Filtrerte rader"'

@app.route('/query', methods=['POST'])
@cross_origin()
def query_func():
    response = request.json
    global query
    query = str(response["pbiInput"])
    print(query)
    return "Successfull"


@app.route('/dtl_transform', methods=['GET'])
def dtl_transform():
    global query
    query_resp = query
    #query_resp = text_example
    dtl_code = str()
    dtl_prefix = '    "type": "dtl", \n     "rules": { \n       "default": [ \n         ["copy","*"],'
    dtl_postfix = '] \n       {} \n     {} \n   {}'.format("]", "}", "}")
    #dtl_postfix = '\n          {}]}}'.format("]")
    words = query_resp.split()
    for i, word in enumerate(words):
        if word[:5] == "Table":
            command = word.split('.')[1].split('(')[0]
            if command == "RemoveColumns":
                dtl_code += RemoveColumns(i, words)
            if command == "TransformColumns":
                dtl_code += TransformColumns(i, words)
            if command == "SelectRows":
                dtl_code += TransformRows(i, words)

    if dtl_code == str():
        return ('You did not provide a proper code snippet. Please change your code snippet or ask for support.')

    dtl_code = dtl_prefix + dtl_code[:-2] + dtl_postfix
    #return "hei"#({'text': dtl_code})
    print('  "transform":{}\n {}'.format(" {", dtl_code))
    #return "hei"#({'text': dtl_code})
    return ('  "transform":{}\n {}'.format(" {", dtl_code))


if __name__ == '__main__':

	# This is used when running locally. Gunicorn is used to run the
	# application on Google App Engine. See entrypoint in app.yaml.
	app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)

