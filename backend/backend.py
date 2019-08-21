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

#text_example = 'let Kilde = Csv.Documents(File.Contents("C:Userserik1DownloadsSampleCSVFile_2kb.csv"),[Delimiter=",", Columns=10, Encoding=1252, QuoteStyle=QuoteStyle.None]), #"Fjernede kolonner" = Table.RemoveColumns(Kilde, {"Column1"}), #"Text med store bokstaver" = Table.TransformColumns(#"Fjernede kolonner", {{"Column2", Text.Upper, type text}}), #"Filtrerte dader" = Table.SelectRows(#"Text med store bokstaver", each ([column2] <> "G.E. LONGER-LIFE INDOOR RECESSED FLOODLIGHT BULBS")), #"Filtrerte rader1" = Table.SelectRows(#"Filtrerte rader", each [Column2] = "SSN") in #"Text med store bokstaver"'
#words = text_example.split()



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
    dtl_prefix = '"transform": {"type": "dtl","rules":{"default": [["copy", "*"],'
    dtl_postfix = ']]}}'
    words = query_resp.split()
    for i, word in enumerate(words):
        if word[:5] == "Table":
            command = word.split('.')[1].split('(')[0]
            if command == "RemoveColumns":
                dtl_code += RemoveColumns(i, words)
            if command == "TransformColumns":
                dtl_code += TransformColumns(i, words)
            #if command == "SelectRows":
            #    print(words[i+1])
            #    ss
            #    dtl_code += TransformRows(i, words)

    if dtl_code == str():
        print("No transformations detected!")
        sys.exit()
    dtl_code = dtl_prefix + dtl_code[:-2] + dtl_postfix
    #print({'text': dtl_code})
    #return "hei"#({'text': dtl_code})
    return ({'text': dtl_code})


if __name__ == '__main__':

	# This is used when running locally. Gunicorn is used to run the
	# application on Google App Engine. See entrypoint in app.yaml.
	app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
