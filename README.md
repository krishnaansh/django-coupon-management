# django-coupon-management
##  A Django app that makes the use of coupons a simple task!

![PyPI v0.3](https://img.shields.io/badge/PyPI-v0.3-blue.svg)
![MIT License](https://img.shields.io/badge/License-MIT-lightgray.svg)
![Docs](https://img.shields.io/badge/docs-meh-orange.svg)

django-simple-coupons is a simple Django app to create and use promotional coupons in your website.

### Downloading

django-coupon-management is available on The Python Package Index (PyPI). You can simply use ***pip*** to install it:

```bash
$ pip install django-coupon-management
```

### Installing

1 - Add ```coupon_management``` inside INSTALLED_APPS in settings.py:

```python
INSTALLED_APPS = [
        ...
        'coupon_management',
]
```

2 - (Optional) If you want to use more than 12 chars (default) for your coupon code, add ```DSC_COUPON_CODE_LENGTH``` variable in settings.py:

```python
DSC_COUPON_CODE_LENGTH = 16
```

3 - Run the migrations:

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

And that's it! django-coupon-management should appear in your admin as ```Coupon Managements```.

### Changelog

***[https://github.com/krishnaansh/django-coupon-management/blob/master/CHANGELOG.txt](https://github.com/krishnaansh/django-coupon-management/blob/master/CHANGELOG.txt)***

### Documentation

***[https://github.com/krishnaansh/django-coupon-management/blob/master/docs/README.md](https://github.com/krishnaansh/django-coupon-management/blob/master/docs/README.md)***
