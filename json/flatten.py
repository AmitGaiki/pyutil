from exception.json_exception import InvalidInstanceTypeException


# flattened list should return len of list, len of each of data types and a sample object of types list, dict or tuple
def flatten_list(input_list):
    if not isinstance(input_list, list):
        raise InvalidInstanceTypeException("Expected instance of list, found {type}".format(type=type(input_list).__name__))
    type_counts = {}
    objects = []
    for element in input_list:
        type_counts[type(element).__name__] = type_counts.get(type(element).__name__, 0) + 1
        if isinstance(element, dict):
            output = flatten_dict(element)
            if output not in objects: objects.append(output)
        elif isinstance(element, list):
            flatten_list(element)
        elif isinstance(element, tuple):
            flatten_tuple(element)

    return {
        'counts': type_counts,
        'objects': objects
    }


# flattened dictionary should give keys along with data types of each keys. if the type of value for some key is list, tuple or dict, it should flatten those
def flatten_dict(input_dict):

    if not isinstance(input_dict, dict):
        raise InvalidInstanceTypeException("Expected instance of dict, found {type}".format(type=type(input_dict).__name__))
    keyset = {}
    for key, value in input_dict.items():
        if isinstance(value, dict):
            keyset[key] = flatten_dict(value)
        elif isinstance(value, list):
            keyset[key] = flatten_list(value)
        elif isinstance(value, tuple):
            keyset[key] = flatten_tuple(value)
        else:
            keyset[key] = type(value).__name__

    return keyset


def flatten_tuple(input_tuple):
    if not isinstance(input_tuple, tuple):
        raise InvalidInstanceTypeException("Expected instance of tuple, found {type}".format(type=type(input_tuple).__name__))

    type_counts = {}
    for element in input_tuple:
        type_counts[type(element).__name__] = type_counts.get(type(element).__name__, 0) + 1
        if isinstance(element, dict):
            flatten_dict(element)
        elif isinstance(element, list):
            flatten_list(element)
        elif isinstance(element, tuple):
            flatten_tuple(element)

    return {
        'counts': type_counts
    }