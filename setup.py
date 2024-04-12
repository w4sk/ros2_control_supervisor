from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ros2_control_supervisor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='uclab',
    maintainer_email='guiguidubian@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sample_node = ros2_control_supervisor.sample_node:main',
            'lifecycle_node = ros2_control_supervisor.lifecycle_node:main',
            'controller_supervisor = ros2_control_supervisor.controller_supervisor:main'
        ],
    },
)
