from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import requests
import json
import sys

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, 
headers={'Access-Control-Request-Headers', 'Content-Type', 'Access-Control-Allow-Origin'})

#text_example = 'let Kilde = Csv.Documents(File.Contents("C:Userserik1DownloadsSampleCSVFile_2kb.csv"),[Delimiter=",", Columns=10, Encoding=1252, QuoteStyle=QuoteStyle.None]), #"Fjernede kolonner" = Table.RemoveColumns(Kilde, {"Column1"}), #"Text med store bokstaver" = Table.TransformColumns(#"Fjernede kolonner", {{"Column2", Text.Upper, type text}}) in #"Tetx med store bokstaver"'
#words = text_example.split()

def transform(query):
	dtl_code = str()
	dtl_prefix = '"transform": {"type": "dtl","rules":{"default": [["copy", "*"],'
	dtl_postfix = ']}}'
	words = query.split()
	for i, word in enumerate(words):
		if word[:5] == "Table":
			command = word.split('.')[1].split('(')[0]
			if command == "RemoveColumns":
				property = words[i+1].split('"')[1]
				dtl_code += '["remove", %s],' %property
			if command == "TransformColumns":
				property = words[i+2].split('"')[1]
				dtl_code += '["remove", "%s"],' %property
				dtl_code += '["add", %s, ["upper", _S.%s]],' %(property, property)
	if dtl_code == str():
		print("No transformations detected!")
		sys.exit()
	return dtl_prefix + dtl_code[:-2] + dtl_postfix


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
	dtl_code = transform(query)
	return jsonify(dtl_code.json())


if __name__ == '__main__':

    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)

