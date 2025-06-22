import os
from setuptools import setup, find_packages

# Функция для чтения README.md, если он есть
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

setup(
    name='DarkChatAPI',  
    version='0.1.3',   
    author='vsp210', 
    author_email='vsp210@gmail.com', 
    description='Клиентская библиотека Python для API DarkChat',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/vsp210/DarkChatAPI', 
    packages=find_packages(where='.'),
    install_requires=[  
        'requests',
        'websocket-client', 
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat',
    ],
    python_requires='>=3.8',  
)
