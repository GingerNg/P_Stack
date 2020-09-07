import json

###################
# set
###################


def set_value_by_key(input_json, key, value):
    """[根据key更新value todo]

    Args:
        input_json ([type]): [description]
        key ([type]): [description]
        value ([type]): [description]
    """
    if isinstance(input_json, dict):
        if key in input_json.keys():
            input_json[key] = value
            # key_value = input_json.get(key)
            print("replaced")
            # return
        else:
            for json_result in input_json.values():
                set_value_by_key(json_result, key, value)
    elif isinstance(input_json, list):
        for json_result in input_json:
            set_value_by_key(json_result, key, value)
    # else:
    #     return
    return

###################
# get
###################


def get_value_by_key(input_json, key):
    """[从json中根据key获取value]

    Args:
        input_json ([type]): [description]
        key ([type]): [description]

    Returns:
        [type]: [description]
    """
    key_value = ''
    if isinstance(input_json, dict):
        if key in input_json.keys():
            key_value = input_json.get(key)
        else:
            for json_result in input_json.values():
                key_value = get_value_by_key(json_result, key)
                if key_value != '' and key_value != None:
                    break
    elif isinstance(input_json, list):
        for json_array in input_json:
            key_value = get_value_by_key(json_array, key)
            if key_value != '' and key_value != None:
                break
    if key_value != '' and key_value != None:
        return key_value


def get_values_by_key(input_json, key):
    """[从json中根据key获取所有的value]

    Args:
        input_json ([type]): [description]
        key ([type]): [description]

    Returns:
        [type]: [description]
    """
    key_values = []
    if isinstance(input_json, dict):
        for k, v in input_json.items():
            if k == key:
                key_values.append(input_json.get(key))
            else:
                key_values += get_values_by_key(v, key)
        # return key_values
    elif isinstance(input_json, list):
        for json_array in input_json:
            key_values += get_values_by_key(json_array, key)
        # return key_values
    # print(key_values)
    return key_values


def get_dict_by_kv(input_json, key, value):
    key_values = []
    if isinstance(input_json, dict):
        for k, v in input_json.items():
            if k == key and v == value:
                key_values.append(input_json)
            else:
                key_values += get_dict_by_kv(v, key, value)
        # return key_values
    elif isinstance(input_json, list):
        for json_array in input_json:
            key_values += get_dict_by_kv(json_array, key, value)
        # return key_values
    # print(key_values)
    return key_values


def extract_contents(input_json):
    textList = get_values_by_key(j_data, key="textList")
    contents = []
    for text_item in textList:
        contents.append("".join(get_values_by_key(text_item, key="content")))
    return contents


j_data = json.loads(
    open("/home/ginger/Projects/Learning/P_Stack/basic/PPT自动排版技术分享会_姚庆源_20200810_第二稿.pptx_22.json").read())
# results = get_values_by_key(j_data, key="TypeName")
# results = get_dict_by_kv(j_data, key="TypeName", value="UDMPlugin.UDMColor")
# results = get_dict_by_kv(j_data, key="TypeName", value="UDMPlugin.UDMColor")
# results = get_values_by_key(j_data, key="content")
# print(results)
# results = get_values_by_key(j_data, key="color")
# print(results)
# textList = get_values_by_key(j_data, key="textList")
# print(len(textList))
# text_item = textList[0]
# set_value_by_key(text_item, key="color", value={"AssemblyName": "UDMPlugin",
#                                                 "TypeName": "UDMPlugin.UDMColor",
#                                                 "r": "100",
#                                                 "g": "0",
#                                                 "b": "0",
#                                                 "a": "255"
#                                                 })
# print(text_item)

# print(results)
print(extract_contents(j_data))
results = get_values_by_key(j_data, key="textBulletProperties")
for res in results:
    print(res)
