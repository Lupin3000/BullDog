from setuptools import setup

setup(
    name='BullDog',
    version='0.0.1',
    packages=['BullDog'],
    url='https://softwaretester.info',
    license='',
    author='Steffen Lorenz',
    description='Python USB OTG Keyboard',
    entry_points={
        'console_scripts': [
            'bulldog = BullDog.__main__:main'
        ]
    },
    classifiers=[
        "Topic :: Utilities",
        "Programming Language :: Python :: 3",
        "Environment :: Console"
    ]
)
