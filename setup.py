from setuptools import setup

exec (open('dash_webcam/version.py').read())

setup(
    name='dash_webcam',
    version=__version__,
    author='plotly',
    packages=['dash_webcam'],
    include_package_data=True,
    license='MIT',
    description='Dash UI component suite',
    install_requires=[]
)
