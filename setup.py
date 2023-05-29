from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Datanaut',
    version='0.1.0',
    description='A portfolio of machine learning projects',
    url='https://github.com/Brad-Edwards/datanaut',
    author='Brad Edwards',
    author_email='j.bradley.edwards@gmail.com',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    keywords='machine learning, deep learning',
    install_requires=requirements
)
