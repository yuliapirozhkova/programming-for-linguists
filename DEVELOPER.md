# How to setup an environment for this repository

## Install Python interpreter to your system

To successfully develop on this repository you need to install Python to yor machine.
You should download python installer from [the official site](https://www.python.org/downloads/).
This project was developed and tested using [python3.9.1](https://www.python.org/downloads/release/python-391/)  

After downloading the installer, run the installation using default parameters.

The next steps:
1. [Create a new virtual python environment](#new-venv) 
2. [Create the PyCharm configuration](#pycharm-config) 

## <a name="new-venv"></a>Create a new virtual python environment

It is highly recommended to use a virtual environment to work with this project.

1. To create the virtual environment you have to install the python `virtualenv` package.
    Open a terminal (command prompt) in the project directory and run the following command:
    ```shell script
        python -m pip install virtualenv
    ```

2. Create the python virtual environment on the project folder:
   ```shell script
        python -m virtualenv venv
   ```
   The pyrhon virtual environment will be created on the `<project_root>\venv` folder.
   There is The Python executor in the `<project_root>\venv\bin` folder.

3. To activate the python virtual environment run the following command:
   ```shell script
        <project_root>\venv\Scripts\activate.bat
   ```
     
## <a name="pycharm-config"></a>Create the PyCharm configuration
