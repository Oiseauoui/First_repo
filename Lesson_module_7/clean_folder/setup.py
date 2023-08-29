from setuptools import setup, find_packages

setup(name='clean_folder',
    version='0.0.1',
    # packages=['clean_folder'], 
    packages=find_packages(), 
    author="GO_IT", 
    description="clean folder from trash", 
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:main',
            'fill-files = clean_folder.files_generator:file_generator']
    },

    install_requires=[ 
        'numpy', 
        'Pillow'

    ],

)