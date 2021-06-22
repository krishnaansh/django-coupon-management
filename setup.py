import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-coupon-management',
    version='0.3.2',
    packages=['coupon_management'],
    include_package_data=True,
    license='MIT License',
    description='A Django app that makes the use of coupon management and easy to handle',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/krishnaansh/django-coupon-management',
    author='Krishna',
    author_email='krishnaansh997@gmail.com',
    download_url='https://github.com/krishnaansh/django-coupon-management/archive/refs/tags/v0.3.2.zip',
    keywords =['django', 'coupon', 'management', 'coupon manage', 'promotion'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ]
)
