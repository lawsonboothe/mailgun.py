from setuptools import setup, find_packages

setup(

    name='mailgun',

    version='0.1',

    author='Mailgun Inc.',

    author_email='admin@mailgunhq.com',

    description='Python wrapper for Mailgun REST API',

    url='http://mailgun.net',

    packages=find_packages(),

    install_requires=['pyactiveresource==1.0.1'],

)
