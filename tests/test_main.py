"""
TestPylot Framework - Test Suite for main.py
Tests for the example functions in main.py
"""

from tests.test_framework import create_runner, expect
import src.main as main

runner = create_runner()


@runner.describe("TestPylot Example Functions")
def test_main():

    @runner.subsuite("sum")
    def test_sum():
        @runner.it("should return 0 for no arguments")
        def test_sum_empty():
            assert main.sum() == 0

        @runner.it("should return the single argument")
        def test_sum_single():
            assert main.sum(5) == 5

        @runner.it("should add two numbers")
        def test_sum_two():
            assert main.sum(2, 3) == 5

        @runner.it("should add multiple numbers")
        def test_sum_multiple():
            assert main.sum(1, 2, 3, 4, 5) == 15

        @runner.it("should handle negative numbers")
        def test_sum_negative():
            assert main.sum(-1, -2, 3) == 0

    @runner.subsuite("multiply")
    def test_multiply():
        @runner.it("should multiply two numbers")
        def test_multiply_two():
            expect(main.multiply(2, 3)).to_equal(6)

        @runner.it("should multiply multiple numbers")
        def test_multiply_multiple():
            expect(main.multiply(2, 3, 4)).to_equal(24)

        @runner.it("should return the single argument")
        def test_multiply_single():
            expect(main.multiply(5)).to_equal(5)

        @runner.it("should handle negative numbers")
        def test_multiply_negative():
            expect(main.multiply(-2, 3)).to_equal(-6)
