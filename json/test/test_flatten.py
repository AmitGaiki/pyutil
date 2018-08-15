import unittest
from json import flatten
from exception.json_exception import InvalidInstanceTypeException

class TestFlatten(unittest.TestCase):

    def test_flatten_list_raises_if_input_is_not_list(self):
        with self.assertRaises(InvalidInstanceTypeException):
            flatten.flatten_list('a')

    def test_flatten_list_returns_correct_counts_for_types(self):
        sample_list = ['a', 1, 2, 3, {}, (), [], [], 'asdf', None]
        output = flatten.flatten_list(sample_list)
        self.assertEqual(output.get('counts', {}).get('str'), 2)
        self.assertEqual(output.get('counts', {}).get('int'), 3)
        self.assertEqual(output.get('counts', {}).get('dict'), 1)
        self.assertEqual(output.get('counts', {}).get('list'), 2)
        self.assertEqual(output.get('counts', {}).get('tuple'), 1)
        self.assertEqual(output.get('counts', {}).get('NoneType'), 1)

    def test_flatten_list_flattens_dicts(self):
        sample_list = [
            {'a': 'a', 'b': 1, 'c': False, 'd': None},
            {'a': 'b', 'b': 2, 'c': False, 'd': None},
            {'a': 'c', 'b': 4, 'c': False, 'd': None},
            {'a': 'd', 'b': 3, 'c': False, 'd': None},
            {'a': 'd', 'b': 3},
        ]
        output = flatten.flatten_list(sample_list)
        self.assertEqual(output.get('counts', {}).get('dict'), 5)
        self.assertEqual(len(output.get('objects', [])), 2)
        self.assertEqual(output.get('objects')[0].get('a'), 'str')
        self.assertEqual(output.get('objects')[0].get('b'), 'int')
        self.assertEqual(output.get('objects')[0].get('c'), 'bool')
        self.assertEqual(output.get('objects')[0].get('d'), 'NoneType')
        self.assertEqual(output.get('objects')[1].get('a'), 'str')
        self.assertEqual(output.get('objects')[1].get('b'), 'int')





    def test_flatten_dict_raises_if_input_is_not_dict(self):
        with self.assertRaises(InvalidInstanceTypeException):
            flatten.flatten_list('a')

    def test_flatten_dict_returns_flattened_dictionary_for_basic_types(self):
        sample_dict = {'a': 'a', 'b': 1, 'c': False, 'd': None}
        output = flatten.flatten_dict(sample_dict)
        self.assertEqual(output.get('a'), 'str')
        self.assertEqual(output.get('b'), 'int')
        self.assertEqual(output.get('c'), 'bool')
        self.assertEqual(output.get('d'), 'NoneType')