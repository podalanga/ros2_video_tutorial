from setuptools import find_packages, setup
import os
from glob import glob


package_name = 'py_launch_ex'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'launch'),glob('launch/*')) # this basically means install every launch files into /install/source/<pkg>/launch
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='podalanga',
    maintainer_email='joshuajohn.lvj@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = py_launch_ex.talker:main',
        ],
    },
)
