from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    description='We are creating ML basic projects here.',
    author='Enish',
    author_email='anishpandey@indrenicollege.edu.np',
    # REPLACE WITH YOUR OWN GITHUB PROJECT LINK
    url='https://github.com/Enish-Pandey/ML-Projects',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages(),
)