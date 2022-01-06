from setuptools import find_packages, setup

setup(
    name='repostud',
    version='0.0.1',
    author='oumao',
    author_email='evansotis2015@gmail.com',
    description='Student-Lecturer Interaction Platform',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/oumao/repostud',
    project_urls={
        "Bug Tracker": "https://github.com/oumao/repostud/issues",
    },
    zip_safe=False,
    install_requires=[
        'flask',
        'flask-restful'
    ],
    python_requires='>=3.6'
)