# Set up python environment for autotests


**Python**:


1. Install python 3+

2. Initiate VirtualEnv for project:

> virtualenv venv

3. Activate "VirtualEnv":

> source venv/bin/activate

4. Install requirements:

> pip install -r requirements.txt

5. Use PyTest for default test runner:

> PyCharm - File - Settings - Tools - Python integrated tools 
> default test runner: pytest

**Run tests**:

-- For run one type of test:

> python -m pytest tests/test_***.py

-- For all tests:

> python -m pytest tests/

