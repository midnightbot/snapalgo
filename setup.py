from setuptools import setup, find_packages
 
setup(
  name='snapalgo',
  version='0.0.6.3',
  description='Various Coding algorithms',
  long_description='Code generating code',
  url='https://github.com/midnightbot/snapalgo',  
  author='Anish Adnani',
  author_email='anishadnani00@gmail.com',
  license='MIT', 
  keywords=['python', 'coding', 'template', 'algo', 'algorithms'],
  packages=find_packages(),
  install_requires=['pyperclip'] ,
  classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)