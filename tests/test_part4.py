"""
TestPylot Framework - Test Suite for part4.py
Tests for the functions in part4.py
"""


from tests.framework.test_framework import TestRunner, expect

# Import the module students will implement
try:
    from src import part4 as main
except ImportError:
    # If module doesn't exist, create a dummy for testing
    import sys
    from types import ModuleType
    trytoolz = ModuleType('main')
    sys.modules['main'] = trytoolz

# Get the global test runner
from tests.framework.test_framework import get_runner, create_runner
runner = get_runner() or create_runner()

@runner.describe("TryToolz Part Four - Dictionaries & Advanced Iteration")
def test_part4():

# create_dict
    @runner.subsuite("create_dict")
    def test_create_dict():
        @runner.it("should create dict from equal-length lists")
        def test_create_dict_basic():
            result = main.create_dict(["a", "b", "c"], [1, 2, 3])
            assert result == {"a": 1, "b": 2, "c": 3}

        @runner.it("should create empty dict from empty lists")
        def test_create_dict_empty():
            result = main.create_dict([], [])
            assert result == {}

        @runner.it("should handle single key-value pair")
        def test_create_dict_single():
            result = main.create_dict(["key"], [42])
            assert result == {"key": 42}

        @runner.it("should work with various value types")
        def test_create_dict_types():
            result = main.create_dict(["int", "str", "list"], [1, "hello", [1, 2]])
            assert result == {"int": 1, "str": "hello", "list": [1, 2]}

# get_value
    @runner.subsuite("get_value")
    def test_get_value():
        @runner.it("should retrieve value by key")
        def test_get_value_present():
            dct = {"a": 1, "b": 2, "c": 3}
            assert main.get_value(dct, "a") == 1
            assert main.get_value(dct, "b") == 2

        @runner.it("should return None for missing key")
        def test_get_value_missing():
            dct = {"a": 1, "b": 2}
            assert main.get_value(dct, "z") is None

        @runner.it("should work with various key types")
        def test_get_value_key_types():
            dct = {1: "one", "two": 2, (3, 4): "tuple"}
            assert main.get_value(dct, 1) == "one"
            assert main.get_value(dct, "two") == 2
            assert main.get_value(dct, (3, 4)) == "tuple"

# set_value
    @runner.subsuite("set_value")
    def test_set_value():
        @runner.it("should add new key-value pair")
        def test_set_value_new():
            dct = {"a": 1}
            result = main.set_value(dct, "b", 2)
            assert result == {"a": 1, "b": 2}

        @runner.it("should update existing key")
        def test_set_value_update():
            dct = {"a": 1, "b": 2}
            result = main.set_value(dct, "a", 10)
            assert result == {"a": 10, "b": 2}

        @runner.it("should work with empty dict")
        def test_set_value_empty():
            result = main.set_value({}, "key", "value")
            assert result == {"key": "value"}

# has_key
    @runner.subsuite("has_key")
    def test_has_key():
        @runner.it("should return True if key exists")
        def test_has_key_true():
            dct = {"a": 1, "b": 2, "c": 3}
            assert main.has_key(dct, "a") == True
            assert main.has_key(dct, "b") == True

        @runner.it("should return False if key missing")
        def test_has_key_false():
            dct = {"a": 1, "b": 2}
            assert main.has_key(dct, "z") == False
            assert main.has_key(dct, 1) == False

        @runner.it("should work with various key types")
        def test_has_key_types():
            dct = {1: "one", "two": 2, (3, 4): "tuple"}
            assert main.has_key(dct, 1) == True
            assert main.has_key(dct, (3, 4)) == True
            assert main.has_key(dct, "missing") == False

# get_keys
    @runner.subsuite("get_keys")
    def test_get_keys():
        @runner.it("should return all keys from dict")
        def test_get_keys_basic():
            dct = {"a": 1, "b": 2, "c": 3}
            keys = main.get_keys(dct)
            assert set(keys) == {"a", "b", "c"}

        @runner.it("should return empty list for empty dict")
        def test_get_keys_empty():
            keys = main.get_keys({})
            assert keys == []

        @runner.it("should work with various key types")
        def test_get_keys_types():
            dct = {1: "one", "two": 2}
            keys = main.get_keys(dct)
            assert set(keys) == {1, "two"}

# get_values
    @runner.subsuite("get_values")
    def test_get_values():
        @runner.it("should return all values from dict")
        def test_get_values_basic():
            dct = {"a": 1, "b": 2, "c": 3}
            values = main.get_values(dct)
            assert set(values) == {1, 2, 3}

        @runner.it("should return empty list for empty dict")
        def test_get_values_empty():
            values = main.get_values({})
            assert values == []

        @runner.it("should handle duplicate values")
        def test_get_values_duplicates():
            dct = {"a": 1, "b": 1, "c": 2}
            values = main.get_values(dct)
            assert values.count(1) == 2
            assert values.count(2) == 1

# count_keys
    @runner.subsuite("count_keys")
    def test_count_keys():
        @runner.it("should return number of key-value pairs")
        def test_count_keys_basic():
            assert main.count_keys({"a": 1, "b": 2, "c": 3}) == 3

        @runner.it("should return 0 for empty dict")
        def test_count_keys_empty():
            assert main.count_keys({}) == 0

        @runner.it("should count single pair")
        def test_count_keys_single():
            assert main.count_keys({"key": "value"}) == 1

# remove_key
    @runner.subsuite("remove_key")
    def test_remove_key():
        @runner.it("should remove key-value pair")
        def test_remove_key_present():
            dct = {"a": 1, "b": 2, "c": 3}
            result = main.remove_key(dct, "b")
            assert result == {"a": 1, "c": 3}

        @runner.it("should work when only one pair exists")
        def test_remove_key_single():
            result = main.remove_key({"a": 1}, "a")
            assert result == {}

        @runner.it("should handle missing key gracefully")
        def test_remove_key_missing():
            dct = {"a": 1, "b": 2}
            result = main.remove_key(dct, "z")
            assert result == {"a": 1, "b": 2}

# iterate_list
    @runner.subsuite("iterate_list")
    def test_iterate_list():
        @runner.it("should apply callback to each element")
        def test_iterate_basic():
            result = main.iterate_list([1, 2, 3], lambda x: x * 2)
            assert result == [2, 4, 6]

        @runner.it("should work with empty list")
        def test_iterate_empty():
            result = main.iterate_list([], lambda x: x * 2)
            assert result == []

        @runner.it("should work with different callbacks")
        def test_iterate_callbacks():
            # Square callback
            result = main.iterate_list([1, 2, 3], lambda x: x ** 2)
            assert result == [1, 4, 9]

            # String conversion callback
            result = main.iterate_list([1, 2, 3], lambda x: str(x))
            assert result == ["1", "2", "3"]

        @runner.it("should work with string list")
        def test_iterate_strings():
            result = main.iterate_list(["hello", "world"], lambda s: s.upper())
            assert result == ["HELLO", "WORLD"]

# find_item
    @runner.subsuite("find_item")
    def test_find_item():
        @runner.it("should find first matching item")
        def test_find_basic():
            result = main.find_item([1, 2, 3, 4, 5], lambda x: x > 3)
            assert result == 4

        @runner.it("should return None if no match found")
        def test_find_no_match():
            result = main.find_item([1, 2, 3], lambda x: x > 10)
            assert result is None

        @runner.it("should return first match only")
        def test_find_first_only():
            result = main.find_item([1, 2, 3, 4, 5], lambda x: x > 2)
            assert result == 3

        @runner.it("should work with empty list")
        def test_find_empty():
            result = main.find_item([], lambda x: x > 0)
            assert result is None

        @runner.it("should work with string list")
        def test_find_strings():
            result = main.find_item(["apple", "banana", "cherry"], lambda s: len(s) > 5)
            assert result == "banana"
