"""
TestPylot Framework - Test Suite for part3.py
Tests for the functions in part3.py
"""


from tests.framework.test_framework import TestRunner, expect

# Import the module students will implement
try:
    from src import part3 as main
except ImportError:
    # If module doesn't exist, create a dummy for testing
    import sys
    from types import ModuleType
    trytoolz = ModuleType('main')
    sys.modules['main'] = trytoolz

# Get the global test runner
from tests.framework.test_framework import get_runner, create_runner
runner = get_runner() or create_runner()

@runner.describe("TryToolz Part Three - Lists & Strings")
def test_part3():

# length
    @runner.subsuite("length")
    def test_length():
        @runner.it("should return 0 for empty list")
        def test_length_empty_list():
            assert main.length([]) == 0

        @runner.it("should return 0 for empty string")
        def test_length_empty_string():
            assert main.length("") == 0

        @runner.it("should return correct length for list")
        def test_length_list():
            assert main.length([1, 2, 3]) == 3
            assert main.length([1]) == 1
            assert main.length([1, 2, 3, 4, 5]) == 5

        @runner.it("should return correct length for string")
        def test_length_string():
            assert main.length("hello") == 5
            assert main.length("a") == 1
            assert main.length("hello world") == 11

# get_first
    @runner.subsuite("get_first")
    def test_get_first():
        @runner.it("should return first element of list")
        def test_get_first_list():
            assert main.get_first([1, 2, 3]) == 1
            assert main.get_first([42]) == 42
            assert main.get_first(["a", "b", "c"]) == "a"

        @runner.it("should return first character of string")
        def test_get_first_string():
            assert main.get_first("hello") == "h"
            assert main.get_first("a") == "a"

# get_last
    @runner.subsuite("get_last")
    def test_get_last():
        @runner.it("should return last element of list")
        def test_get_last_list():
            assert main.get_last([1, 2, 3]) == 3
            assert main.get_last([42]) == 42
            assert main.get_last(["a", "b", "c"]) == "c"

        @runner.it("should return last character of string")
        def test_get_last_string():
            assert main.get_last("hello") == "o"
            assert main.get_last("a") == "a"

# get_at_index
    @runner.subsuite("get_at_index")
    def test_get_at_index():
        @runner.it("should return element at positive index")
        def test_get_at_index_positive():
            assert main.get_at_index([1, 2, 3], 0) == 1
            assert main.get_at_index([1, 2, 3], 1) == 2
            assert main.get_at_index([1, 2, 3], 2) == 3

        @runner.it("should return character at positive index in string")
        def test_get_at_index_string():
            assert main.get_at_index("hello", 0) == "h"
            assert main.get_at_index("hello", 4) == "o"

        @runner.it("should support negative indices")
        def test_get_at_index_negative():
            assert main.get_at_index([1, 2, 3], -1) == 3
            assert main.get_at_index([1, 2, 3], -2) == 2
            assert main.get_at_index("hello", -1) == "o"

# get_slice
    @runner.subsuite("get_slice")
    def test_get_slice():
        @runner.it("should slice list from start to end")
        def test_get_slice_list():
            assert main.get_slice([1, 2, 3, 4, 5], 1, 3) == [2, 3]
            assert main.get_slice([1, 2, 3, 4, 5], 0, 2) == [1, 2]
            assert main.get_slice([1, 2, 3, 4, 5], 3, 5) == [4, 5]

        @runner.it("should slice string from start to end")
        def test_get_slice_string():
            assert main.get_slice("hello", 1, 3) == "el"
            assert main.get_slice("hello", 0, 2) == "he"
            assert main.get_slice("hello", 3, 5) == "lo"

        @runner.it("should handle slice at boundaries")
        def test_get_slice_boundaries():
            assert main.get_slice([1, 2, 3], 0, 0) == []
            assert main.get_slice([1, 2, 3], 0, 3) == [1, 2, 3]

# append_item
    @runner.subsuite("append_item")
    def test_append_item():
        @runner.it("should append item to empty list")
        def test_append_empty():
            result = main.append_item([], 1)
            assert result == [1]

        @runner.it("should append item to non-empty list")
        def test_append_nonempty():
            result = main.append_item([1, 2], 3)
            assert result == [1, 2, 3]

        @runner.it("should work with different data types")
        def test_append_types():
            assert main.append_item([1, 2], 3) == [1, 2, 3]
            assert main.append_item(["a", "b"], "c") == ["a", "b", "c"]
            assert main.append_item([1], [2, 3]) == [1, [2, 3]]

# remove_item
    @runner.subsuite("remove_item")
    def test_remove_item():
        @runner.it("should remove item from list")
        def test_remove_present():
            result = main.remove_item([1, 2, 3], 2)
            assert result == [1, 3]

        @runner.it("should remove only first occurrence")
        def test_remove_first_only():
            result = main.remove_item([1, 2, 2, 3], 2)
            assert result == [1, 2, 3]

        @runner.it("should work with different data types")
        def test_remove_types():
            assert main.remove_item(["a", "b", "c"], "b") == ["a", "c"]
            assert main.remove_item([1, "a", 1], 1) == ["a", 1]

# count_item
    @runner.subsuite("count_item")
    def test_count_item():
        @runner.it("should count single occurrence")
        def test_count_single():
            assert main.count_item([1, 2, 3], 2) == 1

        @runner.it("should count multiple occurrences")
        def test_count_multiple():
            assert main.count_item([1, 2, 2, 3, 2], 2) == 3
            assert main.count_item(["a", "a", "b"], "a") == 2

        @runner.it("should return 0 when item not in list")
        def test_count_zero():
            assert main.count_item([1, 2, 3], 4) == 0

# reverse_sequence
    @runner.subsuite("reverse_sequence")
    def test_reverse_sequence():
        @runner.it("should reverse list")
        def test_reverse_list():
            assert main.reverse_sequence([1, 2, 3]) == [3, 2, 1]
            assert main.reverse_sequence([1]) == [1]
            assert main.reverse_sequence([]) == []

        @runner.it("should reverse string")
        def test_reverse_string():
            assert main.reverse_sequence("hello") == "olleh"
            assert main.reverse_sequence("a") == "a"
            assert main.reverse_sequence("") == ""

# join_items
    @runner.subsuite("join_items")
    def test_join_items():
        @runner.it("should join with separator")
        def test_join_basic():
            assert main.join_items(["a", "b", "c"], ",") == "a,b,c"
            assert main.join_items(["hello", "world"], " ") == "hello world"

        @runner.it("should handle single item")
        def test_join_single():
            assert main.join_items(["hello"], ",") == "hello"

        @runner.it("should handle empty list")
        def test_join_empty():
            assert main.join_items([], ",") == ""

        @runner.it("should work with different separators")
        def test_join_separators():
            assert main.join_items(["a", "b", "c"], "-") == "a-b-c"
            assert main.join_items(["a", "b", "c"], "") == "abc"
