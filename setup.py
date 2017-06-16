from setuptools import setup, find_packages

setup(
    name='django-resource',
    version='0.0.2',
    description="REST API's Resources for django",
    url='https://github.com/lamenezes/django-resource',
    download_url='https://github.com/lamenezes/django-resource/releases',
    license='MIT',
    author='Luiz Menezes',
    author_email='luiz.menezesf@gmail.com',
    long_description=open('README.rst').read(),
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
