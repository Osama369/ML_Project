from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> list[str]:
    '''
    This function will return a list of requirements
    
    '''
    requirements = [] # array of requirements
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace('\n', '') for req in requirements]  # remove new line characters
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements        
        

setup(
    
       name='my_package',
       version='0.1.0',
       author='Osama',   
       author_email='eng.usamaqureshi@gmail.com',
       packages=find_packages(),
       install_requires=get_requirements('requirements.txt'),
       
    
    
)    