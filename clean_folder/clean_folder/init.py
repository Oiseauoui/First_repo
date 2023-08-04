from setuptools import setup, find_packages

setup(
    name="clean_folder",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "clean-folder = clean_folder.clean:clean_folder",
        ],
    },
)

#In the setup.py file, we specify the package name, version, and packages to include. 
# The entry_points section is crucial to creating the console script. 
# It tells setuptools to create a console script named "clean-folder" 
# that will call the clean_folder function from the clean_folder.clean module.