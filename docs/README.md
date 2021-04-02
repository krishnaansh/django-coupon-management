# Documentation

### Coupon

##### [https://github.com/krishnaansh/django-coupon-management/blob/master/docs/models/Coupon.md](https://github.com/krishnaansh/django-coupon-management/blob/master/docs/models/Coupon.md)

### Discount

##### [https://github.com/krishnaansh/django-coupon-management/blob/master/docs/models/Discount.md](https://github.com/krishnaansh/django-coupon-management/blob/master/docs/models/Discount.md)

### Coupon Validation

##### [https://github.com/krishnaansh/django-coupon-management/blob/master/docs/models/Ruleset.md](https://github.com/krishnaansh/django-coupon-management/blob/master/docs/models/Ruleset.md)

### Coupon User

##### [https://github.com/krishnaansh/django-coupon-management/blob/master/docs/models/Coupon_User.md](https://github.com/krishnaansh/django-coupon-management/blob/master/docs/models/Coupon_User.md)

### Validations Guide

##### [https://github.com/krishnaansh/django-coupon-management/blob/master/docs/validation/Validations.md](https://github.com/krishnaansh/django-coupon-management/blob/master/docs/validation/Validations.md)

### Usage Example

```python
# views.py - Example only
# /use-coupon/?coupon_code=COUPONTEST01

from django.contrib.auth.models import User
from django.http import HttpResponse

from coupon_management.validations import validate_coupon
from coupon_management.models import Coupon

class UseCouponView(View):
    def get(self, request, *args, **kwargs):
        coupon_code = request.GET.get("coupon_code")
        user = User.objects.get(username=request.user.username)
        
        status = validate_coupon(coupon_code=coupon_code, user=user)
        if status['valid']:
            coupon = Coupon.objects.get(code=coupon_code)
            coupon.use_coupon(user=user)
        
            return HttpResponse("OK")
        
        return HttpResponse(status['message'])
```

To use django-coupon-management accordingly, you'll need to validate the coupon first with the coupon code and the user that will use the coupon.

To validate the coupon, use the method ```validate_coupon()``` from ```coupon_management.validators```. This method returns a dict with one key (if valid) or two keys (if not valid):

```python
VALID = {
    "valid": True
}

INVALID = {
    "valid": False,
    "message": "Some message telling why it's not valid"
}
```

If it's valid, you can safely call the function ```use_coupon()``` from the Coupon instance.

Please note that I used the default User model from Django in this example. If you use a custom authentication system, you'll need to use the proper User model from your custom auth app!
