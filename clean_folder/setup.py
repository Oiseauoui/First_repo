# clean_folder/setup.py

from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='0.0.2',
    author= 'Shishik',
    description='clean_script',
    url='https://github.com/Oiseauoui/First_repo/tree/main/clean_folder',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:main'  #point entering
        ]
    }
    
)
