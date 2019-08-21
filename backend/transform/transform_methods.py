def RemoveColumns(i, words):
    property = words[i+1].split('"')[1]
    return '["remove", "%s"],' %property

def TransformColumns(i, words):
    property = words[i+2].split('"')[1]
    return '["remove", "%s"], ["add", "%s", ["upper", "_S.%s"]],' %(property, property, property)

def TransformRows(i, words):
	return None


"""
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
"""
