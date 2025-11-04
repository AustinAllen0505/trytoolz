# TestPylot Framework

A browser-based Python testing framework for educational projects and coding challenges.

## What is TestPylot?

TestPylot is a simple, browser-friendly framework for creating Python coding exercises. It provides:

- **Browser-based test runner** - No installation needed, runs entirely in the browser using PyScript/Pyodide
- **Custom test framework** - Similar to Mocha.js, designed specifically for Python learners
- **Beautiful test UI** - Color-coded results, collapsible test suites, detailed error messages
- **Hot reload** - Changes to your code are reflected immediately when you refresh the page

## Getting Started

### Prerequisites

- A modern web browser (Chrome, Firefox, Safari, or Edge)
- A text editor or IDE (VS Code, PyCharm, etc.)
- Optional: Python 3.7+ for local testing

### Running the Tests

1. **Open the test runner in your browser:**

   Simply open `SpecRunner.html` in your web browser.

   If opening directly doesn't work, start a local server:
   ```bash
   python3 -m http.server 8000
   ```
   Then navigate to: `http://localhost:8000/SpecRunner.html`

2. **Watch the tests run!**

   The page will show all tests with green checkmarks (passing) or red X marks (failing).

3. **Implement the functions:**

   Edit `src/main.py` and implement the required functions. Each function includes:
   - A function signature
   - A detailed docstring explaining what it should do
   - Examples of expected behavior

4. **See your progress:**

   Save your changes and refresh the browser. Watch the tests turn green as you implement each function correctly!

## Project Structure

```
framework/
├── SpecRunner.html         # Browser-based test runner (open this!)
├── README.md              # This file
├── src/
│   ├── __init__.py        # Package initialization
│   └── main.py            # Your implementations go here
├── tests/
│   ├── test_framework.py  # Custom test framework (don't modify)
│   └── test_main.py       # Tests for main.py functions
└── lib/
    └── styles.css         # Test runner styling
```

## Writing Tests

TestPylot uses a decorator-based test framework similar to Mocha.js. Here's how to structure tests:

### Basic Test Structure

```python
from tests.test_framework import create_runner, expect
import src.main as main

runner = create_runner()

@runner.describe("My Test Suite")
def test_suite():

    @runner.subsuite("my_function")
    def test_my_function():

        @runner.it("should do something specific")
        def test_something():
            result = main.my_function(1, 2)
            assert result == 3
```

### Test Organization

- **`@runner.describe(title)`** - Create a test suite (appears as main heading)
- **`@runner.subsuite(name)`** - Group tests by function (appears as collapsible section)
- **`@runner.it(description)`** - Individual test case (green checkmark if passes, red X if fails)

### Making Assertions

Use Python's `assert` statement:

```python
@runner.it("should return sum")
def test_sum():
    assert main.sum(2, 3) == 5
    assert main.sum() == 0
```

Or use the chainable `expect()` API:

```python
from tests.test_framework import expect

@runner.it("should multiply")
def test_multiply():
    expect(main.multiply(2, 3)).to_equal(6)
    expect(main.multiply(-2, 3)).to_equal(-6)
```

### Available Assertions

- `expect(value).to_equal(expected)` - Equality check
- `expect(value).to_be(expected)` - Identity check (is)
- `expect(value).to_be_truthy()` - Check if truthy
- `expect(value).to_be_falsy()` - Check if falsy
- `expect(value).to_be_none()` - Check if None
- `expect(value).to_not_be_none()` - Check if not None
- `expect(value).to_contain(item)` - Check membership (in)
- `expect(value).to_have_length(n)` - Check length
- `expect(value).to_be_instance_of(cls)` - Check type
- `expect(func).to_raise(exception_type)` - Check exception

## Writing Implementations

Edit `src/main.py` to implement your functions:

```python
def my_function(a, b):
    """
    Brief description of what this function does.

    Args:
        a: First argument
        b: Second argument

    Returns:
        The result of some operation

    Examples:
        >>> my_function(2, 3)
        5
    """
    return a + b
```

### Example: sum() and multiply()

The framework includes example functions:

**`sum(*args)` - IMPLEMENTED (tests pass)**
```python
def sum(*args):
    """Sum all arguments."""
    total = 0
    for num in args:
        total += num
    return total
```

**`multiply(*args)` - STUB (tests fail)**
```python
def multiply(*args):
    """Multiply all arguments together."""
    pass
```

Your task: Implement the `multiply()` function to make its tests pass!

## Test Framework API

### Creating a Runner

```python
from tests.test_framework import create_runner

# Create a new runner for this test module
runner = create_runner()
```

### Organizing Tests

```python
@runner.describe("Feature Name")
def test_feature():
    # All tests in this function belong to "Feature Name" suite

    @runner.subsuite("function_name")
    def test_function():
        # All tests here are grouped under "function_name"

        @runner.it("does something")
        def test_behavior():
            # This is an individual test case
            assert True
```

### Getting Results

```python
# After tests run, get results as a dictionary
results = runner.get_results()
print(f"Passed: {results['passed']}")
print(f"Failed: {results['failed']}")
print(f"Total: {results['total']}")
```

## Tips and Tricks

### Reading Test Output

When a test fails, you'll see:
- **Test description** - What it was testing
- **Error message** - What went wrong
- **Stack trace** - Where the error occurred

Use this information to debug your implementation!

### Understanding the Test UI

- **Green checkmark (✓)** - Test passed
- **Red X (✗)** - Test failed
- **Collapsible sections** - Click to expand/collapse test suites
- **Progress bar** - Visual representation of pass rate
- **Pass count** - Shows X/Y passing in each suite

### Hot Reload

When you modify `src/main.py` or `tests/test_main.py`:
1. Save the file
2. Refresh the browser (F5 or Cmd+R)
3. The page will auto-clear its cache and load the latest code

### Local Testing

You can also import and test your code locally:

```python
# In Python shell
from src.main import sum, multiply

print(sum(1, 2, 3))      # Should print: 6
print(multiply(2, 3, 4)) # Should print: 24
```

## Extending the Framework

### Adding More Functions

1. Add function signatures to `src/main.py`
2. Add tests to `tests/test_main.py`
3. Implement functions to pass tests
4. Refresh browser to see results

### Adding More Test Modules

If you want to split tests across files:

1. Create `src/module1.py` and `src/module2.py`
2. Create `tests/test_module1.py` and `tests/test_module2.py`
3. Update `SpecRunner.html` to fetch the new files:
   ```html
   [[fetch]]
   files = ["src/__init__.py", "src/main.py", "src/module1.py", "src/module2.py", "tests/__init__.py", "tests/test_framework.py", "tests/test_main.py", "tests/test_module1.py", "tests/test_module2.py"]
   ```
4. Import and run the new test modules in the `<script type="py">` block

## Debugging

### Test failing with AttributeError?
```
AttributeError: module 'main' has no attribute 'my_function'
```
→ You haven't defined that function yet, or there's a syntax error preventing the file from loading.

### Test failing with AssertionError?
```
AssertionError: Expected 5, but got 6
```
→ Your function is returning the wrong result. Check your logic!

### Import errors?
```
ImportError: cannot import name 'my_function' from 'src.main'
```
→ Make sure your function is defined at the module level (not inside another function).

## Technical Details

### How It Works

1. **PyScript** loads and runs Python code in the browser using Pyodide (Python compiled to WebAssembly)
2. The custom test framework decorators register tests without running them
3. `runner.run()` executes all registered tests
4. Results are rendered as HTML with color-coded status
5. JavaScript enables collapse/expand functionality

### Browser Caching

The test runner automatically clears Python's cache on page load, ensuring your latest changes are always tested. This is transparent to you!

## Resources

### Test Framework Documentation

- The custom test framework is in `tests/test_framework.py`
- Review it to understand how tests are registered and executed
- You can extend it with additional assertion methods if needed

### PyScript

- [PyScript Docs](https://docs.pyscript.net/)
- Learn how Python runs in the browser

## Philosophy

TestPylot emphasizes:

- **Simplicity** - Minimal dependencies, browser-native
- **Clarity** - Tests are readable and descriptive
- **Accessibility** - No complex setup required
- **Learning** - Designed for educational purposes

---

**Ready to start?** 

You could:
- Explore: open `src/main.py` and implement the `multiply()` function to make its tests pass
- Replace the `src/main.py` with your own code and put your tests in `tests/test_main.py`

**Happy coding!** 🐍✨
