import setuptools

setuptools.setup(name='boilerplot',
                 version='0.1.0',
                 description='Matplotlib boilerplate for publications',
                 long_description=open('README.md').read().strip(),
                 author='Luca Fehlings',
                 author_email='fehlings97@gmail.com',
                 url='https://github.com/fehlings/boilerplot',
                 packages=['boilerplot'],
                 install_requires=['matplotlib'],
                 license='MIT')