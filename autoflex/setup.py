from setuptools import setup, find_packages

setup(
    name='autoflex',                
    version='1.0.0',
    description='Web and System Automation Testing Framework',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Zhiyuan Li',
    author_email='zhiyuanjeremy@gmail.com',
    url='https://github.com/LZYEIL/AutoFlex',
    packages=find_packages(),       
    install_requires=[              
        'selenium>=4.24.0',
        'pyautogui>=0.9.54',
        'pynput>=1.8.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
