# Westwing Assessment
A solution to the technical assessment sent from West Wing
## Tools and Framework Used.
* Language: Python
* Language version: 3.7.7
* Selenium
* brew
* Webdriver: Chrome
* Framework: Behave
* Framework version: 1.2.6
* IDE: Pycharm (Professional Edition)
* OS: macOS (Catalina 10.15.5)
## Installation and usage.
Installation and usage can be done via the terminal or used through the Pycharm IDE.
## Using the Terminal
* Open terminal
* Install python by running _**"brew install python3"**_
* Install behave and selenium by running _**"pip3 install behave selenium"**_
* Install chromedriver by running _**"brew cask install chromedriver"**_
* Navigate to the folder cloned from git.
* run >behave ./features/addToCart.feature
## Using the IDE
## Create a Python Virtual environment.
So you can have an isolated working directory of the Python environment so
as to keep the global Python free of installed dependencies. This ensures 
that the environment created only affects the project. This means the 
environment forms our project working directory.
> **STEPS:**
> * Open terminal
> * Check if **virtualenv** is installed on the system: virtualenv --version.
> * If it is not installed, install using _"pip3 install virtualenv"_.
> * If it is installed, go ahead and create a directory where the virtual
> environment will be located.
> * Navigate to the directory and create the new virtual environment. 
>by using the command _"virtualenv <name_of_environment>"_
> * Install selenium with _"pip install selenium"_
> * Install behave with _"pip install behave"_
> * Copy this project into the environment
> * Activate the virtual environment by using 
>_source <name_of_environment>/bin/activate_
**NB:** To deactivate, just type _**deactivate**_ and hit enter
## Pycharm IDE
* Install Pycharm (Professional Edition).
* Open and navigate to the folder where this project has been copied 
and open it.
* Click the **Run** Tab and click add/edit configuration.
* Click the **+** and select **Behave**
* Name the config
* On the **Feature files or folders**, navigate to the Features folder of 
this project.
* Ensure the virtualenv is being used as the interpreter.
* Click **Apply** and **OK**.
## Project Execution
>Navigate into the Features folder and run _**"behave"**_

## What does this script do?

The Script launches the Westwing site and clicks ona category, selects a product from the category, then adds it to cart.
The Scripts validates that the product is added to cart and the cart icon is increased by the quantity added.
This process is repeated for two other products from different product categories.
