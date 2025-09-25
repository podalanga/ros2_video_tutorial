from setuptools import find_packages, setup

package_name = 'new_format_msg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='podalanga',
    maintainer_email='podalanga@email.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "listener=new_format_msg.sub:main",
            "talker=new_format_msg.pub:main",
            'service=new_format_msg.srv:main',
            'client=new_format_msg.cli:main',
        ],
    },
)
