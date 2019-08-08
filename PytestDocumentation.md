#Pytest Automation Framework

## Pytest Installation
Prerequistics : Python
* Download the latest version of the python from https://www.python.org/downloads/
* Install it and save it an folder
* set up the enviroment variables. For that go to the folder Python/Scripts and set the path in environment variable
Editor : Visual studio code
* Download the latest version of the visual studio code to your system and install it
* Open a new folder and create a python file inside it from the visual stuido editor
* By rightclicking run the python file
* On terminal type pip install pytest
* Once it is installed verify the installation by pytest --version

## Getting started with Pytest
* On visual studio code, Open a new folder and create a python file inside it.
* write the below code :
```python
import pytest
def test_widget_as_expected():
    assert True
```
* On terminal, in the folder location type the command 'pytest'
* The test result has displayed with how many passed functions and its percentage.
```powershell
platform win32 -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: C:\Work\PytestStudy
collected 1 item                                                                                                                     
test_widget.py .                                                                                                                    [100%]

======================================================== 1 passed in 0.05 seconds 
```
* Now write a failing function as well on the file
```python
import pytest
def test_widget_as_expected():
    assert True
def test_widget_fails():
    assert False
```

* The result shows the passed test case and the failed test case details
```powershell
platform win32 -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: C:\Work\PytestStudy
collected 2 items                                                                                                                  
test_widget.py .F                                                                                                                   [100%]

================================================================ FAILURES ================================================================
___________________________________________________________ test_widget_fails ____________________________________________________________

    def test_widget_fails():
>       assert False
E       assert False

test_widget.py:5: AssertionError
=================================================== 1 failed, 1 passed in 0.09 seconds 
```
When any items fails, pytest gives you the entirety of the code or the testcase that ran and it points to the exact line where it is failed.

* Run the command 'pytest -v'. It shows the items passed and failed with details
```powershell
platform win32 -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 -- c:\python37\python.exe
cachedir: .pytest_cache
rootdir: C:\Work\PytestStudy
collected 2 items                                                                                                                         

test_widget.py::test_widget_as_expected PASSED                                                                                      [ 50%]
test_widget.py::test_widget_fails FAILED                                                                                            [100%]

================================================================ FAILURES ================================================================
___________________________________________________________ test_widget_fails ____________________________________________________________

    def test_widget_fails():
>       assert False
E       assert False

test_widget.py:5: AssertionError
=================================================== 1 failed, 1 passed in 0.07 seconds ===================================================
```
* Suppose a third function is defined with another name, rather than strating with test or test_
```python
import pytest
def test_widget_as_expected():
    assert True
def test_widget_fails():
    assert False
def widget():
    assert True
```
When you ran the above, the third function is not collected. Because pytest treats a functions as test case if that has name test or test_ only. The same with the python files as wells. If the file name has test or test_ only pytest recognizes that. Inorder to customize our own test cases, we need to write the configuration in configuration file.
Follow the below steps to write the configuration file
1. Type the command 'New-Item pytest.ini' to create an ini file
2. In configuration file, we need to write the customized test suites
pytest.ini
```python
[pytest]
python_functions = test_* 
#star what we call a wildcard which means anything that starts with test underscore and some other stuff. 
# these functions are considered as test function
python_files = test_* #the files with name test_* are considered as test files
python_classes = *Tests # test classes have Tests at the end of the name
```

test_widget.py
```
import pytest
def test_widget_as_expected():
    assert True
def test_widget_fails():
    assert False
def test_widget():
    assert True
```
3. Now run the command pytest -v. The python file should be considered as the test file and the three functions should be considered as test functions. the result is
```powershell
PS C:\Work\PytestStudy> pytest -v
========================================================== test session starts ===========================================================
platform win32 -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 -- c:\python37\python.exe
cachedir: .pytest_cache
rootdir: C:\Work\PytestStudy, inifile: pytest.ini
collected 3 items                                                                                                                         

test_widget.py::test_widget_as_expected PASSED                                                                                      [ 33%]
test_widget.py::test_widget_fails FAILED                                                                                            [ 66%]
test_widget.py::test_widget PASSED                                                                                                  [100%]

================================================================ FAILURES ================================================================
___________________________________________________________ test_widget_fails ____________________________________________________________

    def test_widget_fails():
>       assert False
E       assert False

test_widget.py:5: AssertionError
=================================================== 1 failed, 2 passed in 0.08 seconds ===================================================
```
4. Now on pytest.ini change the configuration and run the command pytest -v

```python
[pytest]
python_functions = check_* 
python_files = check_*
python_classes = *Checks
```
This time, no tests ran as the system considers the files and functions with check_* only as the test files and functions
```powershell
PS C:\Work\PytestStudy> pytest -v
========================================================== test session starts ===========================================================
platform win32 -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 -- c:\python37\python.exe
cachedir: .pytest_cache
rootdir: C:\Work\PytestStudy, inifile: pytest.ini
collected 0 items                                                                                                                         

====================================================== no tests ran in 0.02 seconds ======================================================
```
5. Rename the test_widget.py to check_widget.py and make the below changes on the file
check_widget.py
```python
import pytest
def test_widget_as_expected():
    assert True
def check_widget_fails():
    assert False
def test_widget():
    assert True
```
6. Run the command pytest -v. The file is executed with only the second function as the test case
```powershell
PS C:\Work\PytestStudy> pytest -v
========================================================== test session starts ===========================================================
platform win32 -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 -- c:\python37\python.exe
cachedir: .pytest_cache
rootdir: C:\Work\PytestStudy, inifile: pytest.ini
collected 1 item                                                                                                                          

check_widget.py::check_widget_fails FAILED                                                                                          [100%]

================================================================ FAILURES ================================================================
___________________________________________________________ check_widget_fails ___________________________________________________________

    def check_widget_fails():
>       assert False
E       assert False

check_widget.py:5: AssertionError
```
Pytest is a very powerful tool, there are lot of things we can customize and allow us to do a lot of powerful things. We can write test cases and this would organize and completely eliminate the need for you to really manage your own test suites as long as you name your tests well and you put them in to files that are named well and you can use as many directories as you want.
For example I created another directory named 'Deepertests' and created a python file inside it with the name 'check_sub_widget.py' and wrote the below code
check_sub_widget.py
```python
import pytest
def check_sub_widget_as_expected():
    assert True
def check_sub_widget_fails():
    assert False
def test_widget():
    assert True
```
Now run the command pytest -v. Both the files check_widget.py and check_sub_widget.py are consideres as test files and the function with name starting as check_* are considered as valid test functions.

```powershell
PS C:\Work\PytestStudy> pytest -v
========================================================== test session starts ===========================================================
platform win32 -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 -- c:\python37\python.exe
cachedir: .pytest_cache
rootdir: C:\Work\PytestStudy, inifile: pytest.ini
collected 3 items                                                                                                                         

check_widget.py::check_widget_fails FAILED                                                                                          [ 33%]
Deepertests/check_sub_widget.py::check_sub_widget_as_expected PASSED                                                                [ 66%]
Deepertests/check_sub_widget.py::check_sub_widget_fails FAILED                                                                      [100%]

================================================================ FAILURES ================================================================
___________________________________________________________ check_widget_fails ___________________________________________________________

    def check_widget_fails():
>       assert False
E       assert False

check_widget.py:5: AssertionError
_________________________________________________________ check_sub_widget_fails _________________________________________________________

    def check_sub_widget_fails():
>       assert False
E       assert False

Deepertests\check_sub_widget.py:5: AssertionError
=================================================== 2 failed, 1 passed in 0.09 seconds ===================================================
```
Whateever directories or files or functions are present, when you type pytest, it runs all of them as customized in the configuration file. Thus we we can powerfully organize the test cases. We should not stick in to a class called smoke test or integration suite or regression suite . Suppose you have a test case 'r' to call on regression suite and 'i' to call on integration suite. To remove the test cases, we need to remove in all the places where it is called. Manually maintaining test suites are very difficult.
Pytest allows you to organize your tests by putting them in as many directories as you need to have. At the end of the day Pytest will find out the testcases as long as you follow the rules.    

Refer more about Pytest here : https://docs.pytest.org/en/3.0.1/getting-started.html

## Test Searching in Pytest
* Make a directory structure in visual studio code as below:
Parent directory - Tests
sub directory - Sportscar
Inside Sportscar , 3 child directories - body, engine and entertainment.

For creating directories, you can use visual code editor or by using command line type 'mkdir directoryname'

* The configuration file pytest.ini contains the below code
```python
[pytest]
python_functions = test_* 
python_files = test_* 
python_classes = *Tests 
```

* Creates files inside the directory. You can create it from the visual studio explorer or through command line by typing the command 'New-Item filename.py'
under the dir 
body - test_body.py
```python
def test_body_function_as_expected():
    assert True
```
engine - test_engine.py
```python
def test_engine_function_as_expected():
    assert True
```
entertainment - test_entertainment.py
```python
def test_entertainment_function_as_expected():
    assert True
```

* Now run pytest from the main directory. It collects the functions from all the files inside the directory as per the configuration

```powershell
PS C:\Work\PytestStudy\Tests> pytest -v
========================================================== test session starts ===========================================================
platform win32 -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 -- c:\python37\python.exe
cachedir: .pytest_cache
rootdir: C:\Work\PytestStudy, inifile: pytest.ini
collected 3 items                                                                                                                         

sportscar\body\test_body.py::test_body_function_as_expected PASSED                                                                  [ 33%]
sportscar\engine\test_engine.py::test_engine_function_as_expected PASSED                                                            [ 66%]
sportscar\entertainment\test_entertainment.py::test_entertainment_function_as_expected PASSED                                       [100%]
```

### Markers
Markers allow you to mark a test function or test class with custom metadata.
Suppose if the project structure has thousands of tests and you want to run only a few, and dont want run the entire test suit. This is where test search comes in handy and this is where we use markers. 
Markers are ways of marking tests so that we can delineate what we want to run and when.

test_engine.py
```python
#import marker
from pytest import mark

@mark.engine
def test_engine_function_as_expected():
    assert True
```
Here we have marked the function, so that we can run only the marked functions by typing the command  'pytest -m engine'. Only the marked files will run.

```powershell
S C:\Work\PytestStudy\Tests> pytest -m engine
========================================================== test session starts ===========================================================
platform win32 -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: C:\Work\PytestStudy, inifile: pytest.ini
collected 3 items / 2 deselected / 1 selected                                                                                             

sportscar\engine\test_engine.py .                                                                                                   [100%]

============================================================ warnings summary ============================================================
c:\python37\lib\site-packages\_pytest\mark\structures.py:332
  c:\python37\lib\site-packages\_pytest\mark\structures.py:332: PytestUnknownMarkWarning: Unknown pytest.mark.engine - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/latest/mark.html
    PytestUnknownMarkWarning,

-- Docs: https://docs.pytest.org/en/latest/warnings.html
=========================================== 1 passed, 2 deselected, 1 warnings in 0.05 seconds ===========================================
```
### Use of Markers in Pytest
By calling Markers you can define the test suits. For example, if you mark a few test cases as smoke and other few as regression, on running smoke, the smoke suite is executed and on running regression the regression suite is executed
Example : The functions inside test_body and test_engine are marked as smoke test case. The function inside test_entertainment is marked as regression test case
test_body.py
```python
from pytest import mark

@mark.smoke
@mark.body
def test_body_function_as_expected():
    assert True
```

test_engine.py
```python
from pytest import mark

@mark.smoke
@mark.engine
def test_engine_function_as_expected():
    assert True
```

test_entertainment.py
```python
from pytest import mark

@mark.regression
@mark.entertainment
def test_entertainment_function_as_expected():
    assert True
```

Now run the smoke test suite
type 'pytest -m smoke'. The smoke test cases will be executed
```powershell
PS C:\Work\PytestStudy\Tests> pytest -m smoke
========================================================== test session starts ===========================================================
platform win32 -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: C:\Work\PytestStudy, inifile: pytest.ini
collected 3 items / 1 deselected / 2 selected                                                                                             

sportscar\body\test_body.py .                                                                                                       [ 50%]
sportscar\engine\test_engine.py .                                                                                                   [100%]
```

Now run the regression test suite. Type 'pytest -m regression'
```powershell
PS C:\Work\PytestStudy\Tests> pytest -m regression
========================================================== test session starts ===========================================================
platform win32 -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: C:\Work\PytestStudy, inifile: pytest.ini
collected 3 items / 2 deselected / 1 selected                                                                                             

sportscar\entertainment\test_entertainment.py . 
```

If you want to remove any of the test from the smoke suite or so, just go and remove the mark tag from that test case. When you run again, that test case won't be considered under smoke suite.

### Mixing and Matching of the markers
1. Suppose in your test suite, there are several test cases which are marked both as Smoke and Functional test cases. If you want to run both, use 'and' operator.
test_body.py
```python
from pytest import mark

@mark.smoke
@mark.body
@mark.functional
def test_body_function_as_expected():
    assert True
```
test_engine.py
```python
#import marker
from pytest import mark

@mark.smoke
@mark.engine
@mark.functional
def test_engine_function_as_expected():
    assert True
```
test_body and test_engine, belongs to both smoke and functional test case category. Instead of running individually type the command  - pytest -m "smoke and functional". All the test cases marked as both smoke and functional will be executed.

```powershell
PS C:\Work\PytestStudy> pytest -m "smoke and functional"
========================================================== test session starts ===========================================================
platform win32 -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: C:\Work\PytestStudy, inifile: pytest.ini
collected 3 items / 1 deselected / 2 selected                                                                                             

Tests\sportscar\body\test_body.py .                                                                                                 [ 50%]
Tests\sportscar\engine\test_engine.py .        
```

2. Suppose you want to run test cases marked as smoke or functional or edge.
Type the command "pytest -m "smoke or functional or edge"
Here test_body is a smoke test case, test_engine is a functional test case and test_entertainment is an edge test case.
test_body.py
```python
from pytest import mark

@mark.smoke
@mark.body
def test_body_function_as_expected():
    assert True
```
test_engine.py
```
#import marker
from pytest import mark

@mark.engine
@mark.functional
def test_engine_function_as_expected():
    assert True
```
test_entertainment.py
```python
from pytest import mark

@mark.edge
@mark.entertainment
def test_entertainment_function_as_expected():
    assert True
```

```powershell
S C:\Work\PytestStudy> pytest -m "smoke or functional or edge"
========================================================== test session starts ===========================================================
platform win32 -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: C:\Work\PytestStudy, inifile: pytest.ini
collected 3 items                                                                                                                         

Tests\sportscar\body\test_body.py .                                                                                                 [ 33%]
Tests\sportscar\engine\test_engine.py .                                                                                             [ 66%]
Tests\sportscar\entertainment\test_entertainment.py .                                                                               [100%]
```
3. Suppose if you want to run, everything except the edge test case.
Type the command :  pytest -m "not edge". It runs all the test cases except, the ones which are marked as edge.

### Marking whole class or modules
You may use pytest.mark decorators with classes to apply markers to all of its test methods.
This is equivalent to directly applying the decorator to the all the test functions inside the class.
This is applicable if you have a bunch of test cases with same markers, put those inside a class and call the marker at the class level.

test_body.py
```python
from pytest import mark

@mark.smoke
@mark.body
class BodyTests:

    def test_body_function_as_expected(self):
        assert True
    def test_body_color(self):
        assert True
    def test_body_bumper(self):
        assert True
```
Run as pytest -m body, it run the whole class and its functions.

```powershell
PS C:\Work\PytestStudy> pytest -m body
========================================================== test session starts ===========================================================
platform win32 -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: C:\Work\PytestStudy, inifile: pytest.ini
collected 5 items / 2 deselected / 3 selected                                                                                             

Tests\sportscar\body\test_body.py ...    
```

```powershell
PS C:\Work\PytestStudy> pytest -m "not edge"
========================================================== test session starts ===========================================================
platform win32 -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
rootdir: C:\Work\PytestStudy, inifile: pytest.ini
collected 3 items / 1 deselected / 2 selected                                                                                             

Tests\sportscar\body\test_body.py .                                                                                                 [ 50%]
Tests\sportscar\engine\test_engine.py .  
```
### Registering markers
By registering markers you can see which markers exist for your test suite. So that you can look at them later if you forget what they are.
Registering markers for your test suite is simple. On configuration file, give the details of the markers you have used in the test suite.
```python
[pytest]
python_functions = test_* 
python_files = test_* 
python_classes = *Tests 

markers = 
    smoke : All critical smoke Tests
    functional : All test cases covering the functionality
    edge : A few edge cases
    body : For all body test cases
```

To run the registered markers, type as 'pytest --markers'.
```powershell
PS C:\Work\PytestStudy> pytest --markers
@pytest.mark.smoke : All critical smoke Tests

@pytest.mark.functional : All test cases covering the functionality

@pytest.mark.edge : A few edge cases

@pytest.mark.body : For all body test cases
```
It is recommended to explicitly register markers so that there is one place in your test suite defining your markers

Refer more about markers here - https://docs.pytest.org/en/latest/example/markers.html

## Test Fixtures
Fixtures are one of the most powerful feature in Pytest.
To demostrate what is fixtures and why are fixtures good, take an example of the test suite with 3 test functions(amazon, flipkart and myntra) inside the directory OnlineMarkets. Let's assume that each test case need a browser window to pop up.In each test case, we need to open the chrome browser and navigate to the specified URL. For that we need to import selenium, the webdriver object and get the url, in each test case. And mark all the three test cases as UI test cases. When you run the code as pytest -m UI, you expect to see three browser window to pop up one at a time,as we are not running it concurrently. It means our test is passed and everything went where it is supposed to go.
test_amazon.py
```python
from pytest import mark
from selenium import webdriver

@mark.UI
def test_amazon_function():
    browser=webdriver.Chrome()
    browser.get("https://www.amazon.in/")
    assert True
```
test_flipkart.py
```python
from pytest import mark
from selenium import webdriver

@mark.UI
def test_flipkart_function():
    browser=webdriver.Chrome()
    browser.get("https://www.flipkart.com/")
    assert True
```
test_myntra.py
```python
from pytest import mark
from selenium import webdriver

@mark.UI
def test_myntra_function():
    browser=webdriver.Chrome()
    browser.get("https://www.myntra.com/")
    assert True
```
Run as pytest -m UI. The above three UI test cases will run and three browsers amazon, flipkart and myntra opens one by one.
But what is the problem?
* Need to type the same stuff(import selenium and webdriver object), on three test cases.
We could probably do it once and not have it to pop up everytime. Here is the use of the fixture.
For this, we are going to create a file called 'conftest file' like configuration file(pytest.ini) to create the fixtures. Any fixtures we create in conftest fileis accessible anywhere inside that directory and any directory below it. 

### How to create fixtures?
Create a conftest.py in the same directory or above the test suit resides to create the fixture. 
* Import the fixture, selenium webdriver. 
* Define the decorartor fixture with the scope to function.Fixtures can be scoped to function,module or a class.If you scope the fixture to function level, it means that is the lowest scope you can get and you get one per the function which tends to be a test case as we usually have a test case per function.
* Write a function to call the chrome browser.We created a fixture called chrome browser in the content, that means I get the chrome browser anywhere that I want in any test case that in that directory or below. So I don't want to import it in each files or so.
* Any function that calls this within that function you are just going to get the same object back.

contest.py
```python
from pytest import fixture
from selenium import webdriver

@fixture(scope="function")
def chrome_browser():
    browser = webdriver.Chrome()
    return browser
```
### Conftest.py : Sharing fixture functions
 During implementing your tests you realize that you want to use a fixture function from multiple test files you can move it to a conftest.py file. You don’t need to import the fixture you want to use in a test, it automatically gets discovered by pytest. The discovery of fixture functions starts at test classes, then test modules, then conftest.py files and finally builtin and third party plugins.

### How to Share Data Written in Fixtures?
Fixture allows to write at one time, and if you ever have to change, change in one place.
The main reason the fixture is efficient is because it basically gives the same object no matter how many times we call it.

The below three functions call fixture function as an argument.
test_amazon.py
```python
import pytest
from pytest import mark

@mark.UI
def test_amazon_function(chrome_browser):
    chrome_browser.get("https://www.amazon.in/")
    assert True
```
test_flipcart.py
```python
import pytest
from pytest import mark

@mark.UI
def test_flipkart_function(chrome_browser):
    chrome_browser.get("https://www.flipkart.com/")
    assert True
```
test_myntra.py
```python
import pytest
from pytest import mark

@mark.UI
def test_myntra_function(chrome_browser):
    chrome_browser.get("https://www.myntra.com/")
    assert True
```
Now run the command pytest -m UI, these three functions will be executed and since they call fixture function each time, the corresponding URL gets opened in the chrome browser.

### Scope of the fixtures
#### Scoping to function level
We can scope the fixture functionality to module level, session level, class level or function level.
The above examples demonstarted how we can scope to function level. Function level is the lowest scope you can get and that means you get one per function which tends to be a test case. In the above example, if you run, you can see the chrome browser pop-ups three times, while hitting the corresponding URL. Suppose if you want to open up the chromebrowser once, but need to call multiple URL's multiple times.
conftest.py
```python
from pytest import fixture
from selenium import webdriver

@fixture(scope="function")
def chrome_browser():
    browser = webdriver.Chrome()
    return browser
```

test_online_shopping.py
```python
from pytest import mark
import time

@mark.onlineshopping
def test_online_shopping(chrome_browser):
    first_browser = chrome_browser
    first_browser.get("https://www.amazon.in/")
    time.sleep(5)
    second_browser = chrome_browser
    second_browser.get("https://www.flipkart.com/")
    time.sleep(5)
    third_browser = chrome_browser
    third_browser.get("https://www.myntra.com/")
    assert True
```
Here i gave first browser as chrome browser, the second browser again as chrome browser and so on. When you run as 'pytest -m onlineshopping', it does not give you three browsers, instead gives you one browser, by hitting the three URL's one by one. You can call the fixture as many times as you want. It just takes same place in the memory, same object in the same webdriver. It actually does not even go through all the code again. It just keeps returning the same one. Then why you are getting the same browser each time? Because you can't go any lower than functions and the reason the fixture is efficent is it basically gives the same object no matter how many times you call it.

#### Scopping to session level  
If you scope to session level, a fixture function is applicable for the entire test session.
In the below program, fixture scope is defined to the session. And inside the function, a chromebrowser is called. When other functions use this fixture function as argument, it does not open a chrome browser for each function. Instead the chrome browser is open only once, and based on the test functions the corresponding URL's are hitted one by one. That means one browser for every test.
Here we have only one browser so the same browser handles all three tests.

conftest.py
```python
from pytest import fixture
from selenium import webdriver

@fixture(scope="session")
def chrome_browser():
    browser = webdriver.Chrome()
    return browser
```
test_amazon.py
```python
import pytest
from pytest import mark

@mark.UI
def test_amazon_function(chrome_browser):
    chrome_browser.get("https://www.amazon.in/")
    assert True
```
test_flipkart.py
```python
import pytest
from pytest import mark

@mark.UI
def test_flipkart_function(chrome_browser):
    chrome_browser.get("https://www.flipkart.com/")
    assert True
```
test_myntra.py
```python
import pytest
from pytest import mark

@mark.UI
def test_myntra_function(chrome_browser):
    chrome_browser.get("https://www.myntra.com/")
    assert True
```
Run as 'pytest -m UI'
Result : One chrome browser pop-up and handled the three tests on the same browser.

Fixtures allow you to setup the things in one place so that on future, if any change, you can go ahead and change in one place.

### Demostrate the difference of fixture scope and fixture session
The fixture can handle its own teardown. To demostrate it
Suppose we have three test functions as below,

test_amazon.py
```python
import pytest
from pytest import mark

@mark.UI
def test_amazon_function(chrome_browser):
    chrome_browser.get("https://www.amazon.in/")
    assert True
```
test_flipkart.py
```python
import pytest
from pytest import mark

@mark.UI
def test_flipkart_function(chrome_browser):
    chrome_browser.get("https://www.flipkart.com/")
    assert True
```
test_myntra.py
```python
import pytest
from pytest import mark

@mark.UI
def test_myntra_function(chrome_browser):
    chrome_browser.get("https://www.myntra.com/")
    assert True
```
Inconftest.py file, we have created fixture in function level and using the yield function we are returning the browser. In the bottom a message to print.
Note : the difference between yield and return function
The yield statement suspends function’s execution and sends a value back to caller, but retains enough state to enable function to resume where it is left off. When resumed, the function continues execution immediately after the last yield run. This allows its code to produce a series of values over time, rather them computing them at once and sending them back like a list.

Return sends a specified value back to its caller whereas Yield can produce a sequence of values. We should use yield when we want to iterate over a sequence, but don’t want to store the entire sequence in memory.

Yield are used in Python generators. A generator function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function.

conftest.py
```python
from pytest import fixture
from selenium import webdriver

@fixture(scope="function")
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser
    #Teardown
    print("I am tearing down the browser..")
```
Run the command : pytest -m UI -s -v 
-s to print all the prints
-v to print the verboses

Result : The chrome browser is popup 3 times for each the test case. You can see the teardown message, each time the browser is poped-up.
```powershell
PS C:\Work\PytestStudy\FixtureExamples> pytest -m UI -s -v
========================================================== test session starts ===========================================================
platform win32 -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 -- c:\python37\python.exe
cachedir: .pytest_cache
rootdir: C:\Work\PytestStudy, inifile: pytest.ini
collected 4 items / 1 deselected / 3 selected                                                                                             

OnlineMarkets\Amazon\test_amazon.py::test_amazon_function
DevTools listening on ws://127.0.0.1:64030/devtools/browser/695ed588-e627-4e71-8cc8-176beec5d814
PASSEDI am tearing down the browser..

OnlineMarkets\FlipCart\test_flipcart.py::test_flipkart_function
DevTools listening on ws://127.0.0.1:64066/devtools/browser/e56a48f7-b6cb-4b37-b609-216aabdd5920

ASSEDI am tearing down the browser..

OnlineMarkets\Myntra\test_myntra.py::test_myntra_function
DevTools listening on ws://127.0.0.1:64121/devtools/browser/eef64882-e413-4b36-b1c1-e5dec0d14dd7
[6328:7568:0806/145736.922:ERROR:ssl_client_socket_impl.cc(943)] handshake failed; returned -1, SSL error code 1, net_error -101
[6328:7568:0806/145737.370:ERROR:ssl_client_socket_impl.cc(943)] handshake failed; returned -1, SSL error code 1, net_error -101
PASSEDI am tearing down the browser..
```

Now in conftest.py file, scope the fixture to session level, with no changes in any code.
Run the command pytest -m UI -s -v
You can see the chrome browser is poped-up only once, and all the three tests are handled in the same browser. Also the teardown message is printed only once at the end.

```powershell
PS C:\Work\PytestStudy\FixtureExamples> pytest -m UI -s -v
========================================================== test session starts ===========================================================
platform win32 -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 -- c:\python37\python.exe
cachedir: .pytest_cache
rootdir: C:\Work\PytestStudy, inifile: pytest.ini
collected 4 items / 1 deselected / 3 selected                                                                                             
OnlineMarkets\Amazon\test_amazon.py::test_amazon_function
PASSED
OnlineMarkets\FlipCart\test_flipcart.py::test_flipkart_function 
PASSED
OnlineMarkets\Myntra\test_myntra.py::test_myntra_function
 PASSED
 I am tearing down the browser..
========================================== 3 passed, 1 deselected, 3 warnings in 27.50 seconds ===========================================
````
Refer https://docs.pytest.org/en/latest/fixture.html for more details on fixtures.

## Reporting Test Results and Tracking Test History
* For reporting test result, the librray in place in pytest is pytest-html
* Type the below command to install this
```powershell
pip install pytest-html
```
* Once installed, type the command the below command  to see the list whether pytest-html is installed or not.
```powershell
pip list
```
* If you want the result in a html file give the command

