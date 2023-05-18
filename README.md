# TeachingAssistantApp
Using Flask framework and SQLite to build a website supporting faculties to hire teaching assistants, UML component diagrams used to draw the models relationship and MVC structure and applied some automated testing(UNIT)

---
September 2021 
Final version - includes tests

Requirements.txt is updated in Aug 2022

Includes all tests (unittest, pytest, selenium)

------------------------
## Running the application
-----------------------

### To run this example:
- Start the application with the following command:
    ```
    python smile.py
    ```

### To run the tests:
- run the tests for Model (unittest)
    ``` 
    python -m unittest -v tests\test_models.py 
    ```
- run the tests for routes (pytest)
    ```
    python -m pytest -v tests\test_routes.py
    ```
- run the selenium tests
    * Download the Chrome webdriver for your Chrome browser version (https://chromedriver.chromium.org/downloads); extract and copy it under `C:\Webdriver` folder.
    * Run the SmileApp in a terminal window: 
        ```
        python smile.py
        ```
    * Run the selenium tests
    ```
        python tests\test_selenium.py
    ```
