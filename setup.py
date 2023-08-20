import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='drcrypt',
    version="0.0.1",
    author='DrDataYE',
    author_email='drdstaye@gmail.com',
    description='Encryption and Decryption Text.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DrDataYE/DrCrypt',
    package_dir={"":"src"},
    packages=setuptools.find_packages("src"),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
	    'Programming Language :: Python :: 3.10',
	    'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License'],
)

