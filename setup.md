## Installation and setup of robot framework                               
1. Preconditions:                                                          
   * Python installation
   * Pip
   * configure PATH
   * make virtual environment

2. Installing robot framework with pip                                    
    * python -m pip install robotframework
    * python3 -m pip install  robotframework

   After the successful installation, you should be able to execute the created runner scripts (robot and rebot) with --version option and get both Robot Framework and interpreter versions as a result:

        $ robot --version
        Robot Framework 3.0 (Python 2.7.10 on linux2)

        $ rebot --version
        Rebot 3.0 (Python 2.7.10 on linux2)

3. Upgrade
   * pip install --upgrade robotframework

4. Using robot and rebot scripts

   Starting from Robot Framework 3.0, tests are executed using the robot script and results post-processed with the rebot script:

        robot tests.robot
        rebot output.xml                                                    
5. Installing required libraries                                           
    * pip install requests robotframework-selenium2library  
    * pip install --upgrade robotframework-pageobjectlibrary

6. Installation of IDE
    * Install pycharm
  
7. Import required libraries in the IDE
    * To add the project interpreter, Go to `Files` => `Settings` => `Project: <your_Project>` => `Project Interpreter` and then add the python version available in your project directory.
    * Also add the required libraries such as : `Selenium`, `robotframework-seleniumLibrary`, `robotframework-pageObjectLibrary`.

8. Make a robot file inside a test folder eg: `robotBDDExample/test/login.robot`
9. Go to : `https://github.com/JankariTech/robotBDDExample` for example test cases.
 