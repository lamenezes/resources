from setuptools import setup, find_packages

with open('README.rst') as f:
    README = '\n' + f.read()

setup(
    name='resources',
    version='0.0.1',
    description="Resource centered REST API clients",
    url='https://github.com/lamenezes/resource',
    download_url='https://github.com/lamenezes/resource/releases',
    license='MIT',
    author='Luiz Menezes',
    author_email='luiz.menezesf@gmail.com',
    long_description=README,
    packages=find_packages(exclude=['tests*']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
    ],
    keywords='django resource api model microservices client request lazy',
)
