def RemoveColumns(i, words):
    property = words[i+1].split('"')[1]
    return '["remove","%s"],' %property

def TransformColumns(i, words):
    property = words[i+2].split('"')[1]
    return '["add","%s",["upper","%s"]],' % (property, property)#'["remove", "%s"], ["add", "%s", ["upper", "_S.%s"]],' %(property, property, property)

def TransformRows(i, words):
	prefix = '\n         '
	filter_string = '\n          '
	j = 0
	while j < 1000:
		if words[i+j] == "each":
			property = words[i+j+1].split("[")[1].split("]")[0]
			if words[i+j+2] == "<>":
				value = find_string(i+j+3, words)
				if find_datatype(value) == "string":
					return '{}["filter",{}["neq","_S.{}","{}"]{}],'.format(prefix, filter_string, property, value, prefix)
				else:
					return '{}["filter",{}["neq","_S.{}",{}]{}],'.format(prefix, filter_string, property, value, prefix)
			if words[i+j+2] == "=":
				value = find_string(i+j+3, words)
				if find_datatype(value) == "string":
					return '{}["filter",{}["eq","_S.{}","{}"]{}],'.format(prefix, filter_string, property, value, prefix)
				else:
					return '{}["filter",{}["eq","_S.{}",{}]{}],'.format(prefix, filter_string, property, value, prefix)
		j += 1
	return None


def find_datatype(value):
	numbers = [str(i) for i in range(10)]
	found_letter = False
	found_period = False
	if len(value.split()) != 1:
		return "string"
	for sign in value:
		if sign == ".":
			found_period = True
			continue
		if sign not in numbers:
			found_letter = True
	if found_letter:
		return "string"
	if found_period:
		return "float"
	return "int"

def find_string(k, words):
	value_found = False
	l = k
	while not value_found:
		if ")" in words[l]:
			#print((" ").join(words[k:l+1]))
			#ss
			value = (" ").join(words[k:l+1]).split('"')[1]
			break
		l += 1
	return value


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
