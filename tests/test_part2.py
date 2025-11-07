"""
TestPylot Framework - Test Suite for main.py
Tests for the example functions in main.py
"""


from tests.framework.test_framework import TestRunner, expect

# Import the module students will implement
try:
    from src import part2 as main
except ImportError:
    # If module doesn't exist, create a dummy for testing
    import sys
    from types import ModuleType
    trytoolz = ModuleType('main')
    sys.modules['main'] = trytoolz

# Get the global test runner
from tests.framework.test_framework import get_runner, create_runner
runner = get_runner() or create_runner()


@runner.describe("TryToolz Part Two - Comparisons")
def test_part2():

# is_equal
    @runner.subsuite("is_equal")
    def test_is_equal():
        @runner.it("should return True if two ints are equal")
        def test_is_int_equality():
            assert main.is_equal(1,1) == True
            assert main.is_equal(2,2) == True
            assert main.is_equal(42,42) == True
        @runner.it("should return False if two ints are not equal")
        def test_is_int_inequality():
            assert main.is_equal(1,2) == False
            assert main.is_equal(2,4) == False
            assert main.is_equal(42,24) == False
        @runner.it("should return True if two floats are equal")
        def test_is_float_equality():
            assert main.is_equal(1.3,1.3) == True
            assert main.is_equal(2.4,2.4) == True
            assert main.is_equal(42.42,42.42) == True
        @runner.it("should return False if two floats are not equal")
        def test_is_float_inequality():
            assert main.is_equal(1.1,1.3) == False
            assert main.is_equal(2.2,2.4) == False
            assert main.is_equal(42.14,42.42) == False

# greater_than
    @runner.subsuite("greater_than")
    def test_greater_than():
        @runner.it("should return True if a is greater than b for ints")
        def test_greater_than_true_int():
            assert main.greater_than(4,3) == True
            assert main.greater_than(7,5) == True
            assert main.greater_than(1000,-1) == True
            assert main.greater_than(-3,-10) == True
        @runner.it("should return False if a is less than b for ints")
        def test_greater_than_false_int ():
            assert main.greater_than(3,5) == False
            assert main.greater_than(10,200) == False
            assert main.greater_than(-3,5) == False
            assert main.greater_than(-10,-5) == False

        @runner.it("should return True if a is greater than b for floats")
        def test_greater_than_true_float():
            assert main.greater_than(4,3) == True
            assert main.greater_than(7,5) == True
            assert main.greater_than(1000,-1) == True
            assert main.greater_than(-3,-10) == True
        @runner.it("should return False if a is less than b for floats")
        def test_greater_than_false_float():
            assert main.greater_than(3.1,5.4) == False
            assert main.greater_than(10.2,278.4) == False
            assert main.greater_than(-3.1,5.6) == False
            assert main.greater_than(-10.47,-5.2) == False
 
# less_than
    @runner.subsuite("less_than")
    def test_less_than():
        @runner.it("should return True if a is less than b for ints")
        def test_less_than_true_int():
            assert main.less_than(3,5) == True
            assert main.less_than(10,200) == True
            assert main.less_than(-3,5) == True
            assert main.less_than(-10,-5) == True

            
        @runner.it("should return False if a is greater than b for ints")
        def test_less_than_false_int ():
            assert main.less_than(4,3) == False
            assert main.less_than(7,5) == False
            assert main.less_than(1000,-1) == False
            assert main.less_than(-3,-10) == False

        @runner.it("should return True if a is less than b for floats")
        def test_less_than_true_float():
            assert main.less_than(3.1,5.4) == True
            assert main.less_than(10.2,278.4) == True
            assert main.less_than(-3.1,5.6) == True
            assert main.less_than(-10.47,-5.2) == True

        @runner.it("should return False if a is greater than b for floats")
        def test_less_than_false_float():
            assert main.less_than(4,3) == False
            assert main.less_than(7,5) == False
            assert main.less_than(1000,-1) == False
            assert main.less_than(-3,-10) == False

# greater_than_or_equal_to
    @runner.subsuite("greater_than_or_equal_to")
    def test_greater_than_or_equal_to():
        @runner.it("should return True if a is greater than or equal b for ints")
        def test_greater_than_or_equal_to_true_int():
            assert main.greater_than_or_equal_to(4,3) == True
            assert main.greater_than_or_equal_to(4,4) == True
            assert main.greater_than_or_equal_to(7,5) == True
            assert main.greater_than_or_equal_to(1000,-1) == True
            assert main.greater_than_or_equal_to(-3,-10) == True
            assert main.greater_than_or_equal_to(10,10) == True
            assert main.greater_than_or_equal_to(42,42) == True
        @runner.it("should return False if a is less than b for ints")
        def test_greater_than_or_equal_to_false_int ():
            assert main.greater_than_or_equal_to(3,5) == False
            assert main.greater_than_or_equal_to(10,200) == False
            assert main.greater_than_or_equal_to(-3,5) == False
            assert main.greater_than_or_equal_to(-10,-5) == False
            

        @runner.it("should return True if a is greater than or equal to b for floats")
        def test_greater_than_or_equal_to_true_float():
            assert main.greater_than_or_equal_to(4,3) == True
            assert main.greater_than_or_equal_to(7,5) == True
            assert main.greater_than_or_equal_to(1000,-1) == True
            assert main.greater_than_or_equal_to(-3,-10) == True
        @runner.it("should return False if a is less than b for floats")
        def test_greater_than_or_equal_to_false_float():
            assert main.greater_than_or_equal_to(3.1,5.4) == False
            assert main.greater_than_or_equal_to(10.2,278.4) == False
            assert main.greater_than_or_equal_to(-3.1,5.6) == False
            assert main.greater_than_or_equal_to(-10.47,-5.2) == False

 
# less_than_or_equal_to
    @runner.subsuite("less_than_or_equal_to")
    def test_less_than_or_equal_to():
        @runner.it("should return True if a is less than or equal to b for ints")
        def test_less_than_or_equal_to_true_int():
            assert main.less_than_or_equal_to(3,5) == True
            assert main.less_than_or_equal_to(10,200) == True
            assert main.less_than_or_equal_to(-3,5) == True
            assert main.less_than_or_equal_to(-10,-5) == True

            
        @runner.it("should return False if a is less than or equal to b for ints")
        def test_less_than_or_equal_to_false_int ():
            assert main.less_than_or_equal_to(4,3) == False
            assert main.less_than_or_equal_to(7,5) == False
            assert main.less_than_or_equal_to(1000,-1) == False
            assert main.less_than_or_equal_to(-3,-10) == False

        @runner.it("should return True if a is less than or equal to b for floats")
        def test_less_than_or_equal_to_true_float():
            assert main.less_than_or_equal_to(3.1,5.4) == True
            assert main.less_than_or_equal_to(10.2,278.4) == True
            assert main.less_than_or_equal_to(-3.1,5.6) == True
            assert main.less_than_or_equal_to(-10.47,-5.2) == True

        @runner.it("should return False if a is less than or equal to b for floats")
        def test_less_than_or_equal_to_false_float():
            assert main.less_than_or_equal_to(4,3) == False
            assert main.less_than_or_equal_to(7,5) == False
            assert main.less_than_or_equal_to(1000,-1) == False
            assert main.less_than_or_equal_to(-3,-10) == False

# falsy_or_truthy
    @runner.subsuite("falsy_or_truthy")
    def test_falsy_or_truthy():
        @runner.it("should return 'truthy' for truthy values")
        def test_falsy_or_truthy_truthy():
            assert main.falsy_or_truthy(True) == "truthy"
            assert main.falsy_or_truthy(1) == "truthy"
            assert main.falsy_or_truthy("hello") == "truthy"
            assert main.falsy_or_truthy([1, 2, 3]) == "truthy"
            assert main.falsy_or_truthy({"key": "value"}) == "truthy"
            assert main.falsy_or_truthy(-1) == "truthy"
            assert main.falsy_or_truthy(3.14) == "truthy"

        @runner.it("should return 'falsy' for falsy values")
        def test_falsy_or_truthy_falsy():
            assert main.falsy_or_truthy(False) == "falsy"
            assert main.falsy_or_truthy(0) == "falsy"
            assert main.falsy_or_truthy("") == "falsy"
            assert main.falsy_or_truthy([]) == "falsy"
            assert main.falsy_or_truthy({}) == "falsy"
            assert main.falsy_or_truthy(None) == "falsy"

        @runner.it("should return 'falsy' for 0.0 (float zero)")
        def test_falsy_or_truthy_float_zero():
            assert main.falsy_or_truthy(0.0) == "falsy"

# both
    @runner.subsuite("both")
    def test_both():
        @runner.it("should return True if both values are truthy")
        def test_both_true():
            assert main.both(True, True) == True
            assert main.both(1, 2) == True
            assert main.both("hello", "world") == True
            assert main.both([1], [2]) == True
            assert main.both(5, 10) == True

        @runner.it("should return False if first value is falsy")
        def test_both_first_falsy():
            assert main.both(False, True) == False
            assert main.both(0, 1) == False
            assert main.both("", "hello") == False
            assert main.both([], [1]) == False
            assert main.both(None, 5) == False

        @runner.it("should return False if second value is falsy")
        def test_both_second_falsy():
            assert main.both(True, False) == False
            assert main.both(1, 0) == False
            assert main.both("hello", "") == False
            assert main.both([1], []) == False
            assert main.both(5, None) == False

        @runner.it("should return False if both values are falsy")
        def test_both_both_falsy():
            assert main.both(False, False) == False
            assert main.both(0, 0) == False
            assert main.both("", "") == False
            assert main.both([], []) == False
            assert main.both(None, None) == False

# either
    @runner.subsuite("either")
    def test_either():
        @runner.it("should return True if both values are truthy")
        def test_either_both_true():
            assert main.either(True, True) == True
            assert main.either(1, 2) == True
            assert main.either("hello", "world") == True
            assert main.either([1], [2]) == True

        @runner.it("should return True if first value is truthy")
        def test_either_first_true():
            assert main.either(True, False) == True
            assert main.either(1, 0) == True
            assert main.either("hello", "") == True
            assert main.either([1], []) == True
            assert main.either(5, None) == True

        @runner.it("should return True if second value is truthy")
        def test_either_second_true():
            assert main.either(False, True) == True
            assert main.either(0, 1) == True
            assert main.either("", "hello") == True
            assert main.either([], [1]) == True
            assert main.either(None, 5) == True

        @runner.it("should return False if both values are falsy")
        def test_either_both_falsy():
            assert main.either(False, False) == False
            assert main.either(0, 0) == False
            assert main.either("", "") == False
            assert main.either([], []) == False
            assert main.either(None, None) == False
