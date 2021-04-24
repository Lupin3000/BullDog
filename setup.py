from setuptools import setup

setup(
    name='BullDog',
    version='0.0.1',
    url='https://softwaretester.info',
    license='GNU Library or Lesser General Public License (LGPL)',
    author='Lupin3000',
    description='Python3 USB OTG Keyboard',
    python_requires='>=3.7',
    platforms='Linux',
    packages=['BullDog'],
    keywords='usb otg hid keyboard',
    entry_points={
        'console_scripts': [
            'bulldog = BullDog.__main__:main'
        ]
    },
    classifiers=[
        "Topic :: Utilities",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)"
        "Environment :: Console"
    ]
)
