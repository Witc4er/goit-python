from setuptools import setup, find_packages

setup(
    name='clean_folder',
    vesion='1',
    description='Script for sort files in folder',
    packages=find_packages(),
    entry_points={'console_scripts': ['clean_folder = clean_folder.clean:main']},
    zip_safe=False,
    include_package_data=True
)