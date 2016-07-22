import json
import pandas


def decrease_dict_levels(nested_dict):
    # returns flattened dict with tuples as keys
    resulting_dict = {}
    list_of_levels = [[nested_dict.items()]]
    previous_parent_keys = [tuple()]
    for level in list_of_levels:
        new_level = list()
        parent_keys = list()
        subdict_counter = 0
        for subdict in level:
            for key, value in subdict:
                if isinstance(value, dict):
                    parent_keys.append(previous_parent_keys[subdict_counter] + (key,))
                    new_level.append(value.items())
                else:
                    resulting_dict[previous_parent_keys[subdict_counter] + (key,)] = value
            subdict_counter = subdict_counter + 1
        if new_level != list():
            list_of_levels.append(new_level)
        previous_parent_keys = parent_keys
    return resulting_dict


def convert_json2multidf(path_to_json, create_multiindex=True):
    with open(path_to_json, 'r') as json_data:
        result = pandas.DataFrame(decrease_dict_levels(json.loads(line)) for line in  json_data)
    return result


if __name__ == '__main__':
    
    json_file = 'data/fake_data.json'

    with open(json_file, 'r') as d:
        for line in d:
            result = decrease_dict_levels(json.loads(line))

    print convert_json2multidf(json_file)
