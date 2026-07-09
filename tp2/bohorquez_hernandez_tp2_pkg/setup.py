from setuptools import find_packages, setup

package_name = 'bohorquez_hernandez_tp2_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch',
            ['launch/contador.launch.py', 'launch/republicador.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Maria Bohorquez',
    maintainer_email='gabriellabohorquez@gmail.com',
    description='TP2: contador con servicio (ej1) y republicador con action (ej2).',
    license='MIT',
    entry_points={
        'console_scripts': [
            'contador = bohorquez_hernandez_tp2_pkg.contador_node:main',
            'monitor = bohorquez_hernandez_tp2_pkg.monitor_node:main',
            'republicador_server = bohorquez_hernandez_tp2_pkg.republicador_server:main',
            'republicador_client = bohorquez_hernandez_tp2_pkg.republicador_client:main',
        ],
    },
)
