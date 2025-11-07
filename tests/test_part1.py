"""
TestPylot Framework - Test Suite for main.py
Tests for the example functions in main.py
"""


from tests.framework.test_framework import TestRunner, expect

# Import the module students will implement
try:
    from src import part1 as main
except ImportError:
    # If module doesn't exist, create a dummy for testing
    import sys
    from types import ModuleType
    trytoolz = ModuleType('main')
    sys.modules['main'] = trytoolz

# Get the global test runner
from tests.framework.test_framework import get_runner, create_runner
runner = get_runner() or create_runner()


@runner.describe("TryToolz Part One - Working with Variables")
def test_part1():

# data_type(value)
    @runner.subsuite("data_type")
    def test_data_type():
        @runner.it("should work with ints")
        def test_data_type_int():
            assert main.data_type(10) == "int"
        @runner.it("should work with floats")
        def test_data_type_float():
            assert main.data_type(10.5) == "float"
        @runner.it("should work with strings")
        def test_data_type_string():
            assert main.data_type("hello") == "str"
        @runner.it("should work with booleans")
        def test_data_type_bool():
            assert main.data_type(True) == "bool"
        @runner.it("should work with dictionaries")
        def test_data_type_dict():
            assert main.data_type({}) == "dict"
        @runner.it("should work with lists")
        def test_data_type_list():
            assert main.data_type([1,2,3]) == "list"
        @runner.it("should work with ranges")
        def test_data_type_range():
            assert main.data_type(range(10) ) == "range"
        @runner.it("should work with tuples")
        def test_data_type_tuple():
            assert main.data_type((1,2,3)) == "tuple"
        @runner.it("should work with sets")
        def test_data_type_set():
            assert main.data_type({1,2,3}) == "set"

# add(a, b)
    @runner.subsuite("add")
    def test_add():
        @runner.it("should work with positive ints")
        def test_add_positive_ints():
            assert main.add(2, 3) == 5
        @runner.it("should work with negative ints")
        def test_add_negative_ints():
            assert main.add(5, -4) == 1
        @runner.it("should work with positive floats")
        def test_add_positive_floats():
            assert main.add(2.5, 3.5) == 6.0
        @runner.it("should work with negative floats")
        def test_add_negative_floats():
            assert main.add(5.5, -4.5) == 1
            assert main.add(-5.5, 4.5) == -1
            assert main.add(-5.5, -4.5) == -10


# subtract(a, b)
    @runner.subsuite("subtract")
    def test_subtract():
        @runner.it("should work with positive ints")
        def test_subtract_positive_ints():
            assert main.subtract(3,2) == 1
        @runner.it("should work with negative ints")
        def test_subtract_negative_ints():
            assert main.subtract(3, -2) == 5
            assert main.subtract(-3, 2) == -5
            assert main.subtract(-3, -2) == -1
        @runner.it("should work with positive floats")
        def test_subtract_positive_floats():
            assert main.subtract(3.5,2.1) == 1.4
        @runner.it("should work with negative floats")
        def test_subtract_negative_floats():
            assert main.subtract(3.5, -2.1) == 5.6
            assert main.subtract(-3.5, 2.1) == -5.6
            assert main.subtract(-3.5, -2.1) == -1.4

# multiply(a, b)
    @runner.subsuite("multiply")
    def test_multiply():
        @runner.it("should work with positive ints")
        def test_multiply_positive_ints():
            assert main.multiply(2,3) == 6
        @runner.it("should work with negative ints")
        def test_multiply_negative_ints():
            assert main.multiply(2,-4) == -8
            assert main.multiply(-2,4) == -8
            assert main.multiply(-2,-4) == 8

        @runner.it("should work with positive floats")
        def test_multiply_positive_floats():
            assert main.multiply(6.6,3.5) == 23.099999999999998
        @runner.it("should work with negative floats")
        def test_multiply_negative_floats():
            assert main.multiply(2.2,-4.5) == -9.9
            assert main.multiply(-2.2,4.5) == -9.9
            assert main.multiply(-2.2,-4.5) == 9.9


# divide(a, b)
    @runner.subsuite("divide")
    def test_divide():
        @runner.it("should work with positive ints")
        def test_divide_positive_ints():
            assert main.divide(3,2) == 1.5
        @runner.it("should work with negative ints")
        def test_divide_negative_ints():
            assert main.divide(2,-4) == -0.5
            assert main.divide(-2,4) == -0.5
            assert main.divide(-2,-4) == 0.5

        @runner.it("should work with positive floats")
        def test_divide_positive_floats():
            assert main.divide(2.1,3.5) == 0.6
        @runner.it("should work with negative floats")
        def test_divide_negative_floats():
            assert main.divide(2.2,-4.5) == -0.48888888888888893
            assert main.divide(-2.2,4.5) == -0.48888888888888893
            assert main.divide(-2.2,-4.5) == 0.48888888888888893

# floor_divide(a,b)
    @runner.subsuite("floor_divide")
    def test_floor_divide():
        @runner.it("should work with positive ints")
        def test_floor_divide_positive_ints():
            assert main.floor_divide(3,2) == 1
        @runner.it("should work with negative ints")
        def test_floor_divide_negative_ints():
            assert main.floor_divide(2,-4) == -1
            assert main.floor_divide(-2,4) == -1
            assert main.floor_divide(-2,-4) == 0

        @runner.it("should work with positive floats")
        def test_floor_divide_positive_floats():
            assert main.floor_divide(2.1,3.5) == 0
        @runner.it("should work with negative floats")
        def test_floor_divide_negative_floats():
            assert main.floor_divide(2.2,-4.5) == -1
            assert main.floor_divide(-2.2,4.5) == -1
            assert main.floor_divide(-2.2,-4.5) == 0


# get_remainder(a, b)
    @runner.subsuite("get_remainder")
    def test_get_remainder():
        @runner.it("should work with positive ints")
        def test_get_remainder_positive_ints():
            assert main.get_remainder(4,2) == 0
            assert main.get_remainder(5,2) == 1           
        @runner.it("should work with negative ints")
        def test_get_remainder_negative_ints():
            assert main.get_remainder(-4,2) == 0
            assert main.get_remainder(4,-2) == 0
            assert main.get_remainder(-4,-2) == 0

            assert main.get_remainder(-5,2) == 1 
            assert main.get_remainder(5,-2) == -1
            assert main.get_remainder(-5,-2) == -1
        @runner.it("should work with positive floats")
        def test_get_remainder_positive_floats():
            assert main.get_remainder(4.5,2) == 0.5
            assert main.get_remainder(4.5,2.1) == 0.2999999999999998
        @runner.it("should work with negative floats")
        def test_get_remainder_negative_floats():
            assert main.get_remainder(-4.5,2) == 1.5
            assert main.get_remainder(4.5,-2) == -1.5
            assert main.get_remainder(-4.5,-2) == -0.5
            assert main.get_remainder(4,-2.5) == -1.0
            assert main.get_remainder(4.5,-2.5) == -0.5
            assert main.get_remainder(-4.5,-2.5) == -2.0


# increment(a)
    @runner.subsuite("increment")
    def test_increment():
        @runner.it("should work with positive ints")
        def test_increment_positive_ints():
            assert main.increment(5) == 6
            assert main.increment(0) == 1
        @runner.it("should work with negative ints")
        def test_increment_negative_ints():
            assert main.increment(-5) == -4
            assert main.increment(-4) == -3

# decrement(a)
    @runner.subsuite("decrement")
    def test_decrement():
        @runner.it("should work with positive ints")
        def test_decrement_positive_ints():
            assert main.decrement(5) == 4
            assert main.decrement(1) == 0
        @runner.it("should work with negative ints")
        def test_decrement_negative_ints():
            assert main.decrement(-5) == -6
            assert main.decrement(-4) == -5

# exponent(a, b)
    @runner.subsuite("exponent")
    def test_exponent():
        @runner.it("should work with positive ints")
        def test_exponent_positive_ints():
            assert main.exponent(2,3) == 8
            assert main.exponent(3,3) == 27
        @runner.it("should work with negative ints")
        def test_exponent_negative_ints():
            assert main.exponent(2,-2) == 0.25
        @runner.it("should work with positive floats")
        def test_exponent_positive_floats():
            assert main.exponent(2, 0.5) == pow(2, 0.5)
            assert main.exponent(2, -0.5) == pow(2, -0.5)
        @runner.it("should work with negative floats")
        def test_exponent_negative_floats():
            assert main.exponent(-2, 0.5) == pow(-2, 0.5)
            assert main.exponent(2, -0.5) == pow(2, -0.5) 