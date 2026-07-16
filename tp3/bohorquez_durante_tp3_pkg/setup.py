from setuptools import find_packages, setup

package_name = 'bohorquez_durante_tp3_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/tp3.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    description='TP3: nodo que consulta la TF base_link -> tool0 e imprime la matriz SE(3).',
    license='MIT',
    entry_points={
        'console_scripts': [
            'base_tool_tf = bohorquez_durante_tp3_pkg.base_tool_tf:main',
        ],
    },
)
