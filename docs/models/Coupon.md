# Coupon

Each coupon has a ***code***, ***discount*** and set of rules (known as ***coupon validatino*** in the admin).

Every time you click ```Add Coupon```, a new coupon code will be generated randomly for you. Don't worry, you can set your own personal code if you wish.


Each Coupon Validation has three basic validation that you need to supply: ***Valid Users***, ***Max Usage Count*** and ***Validity rule***.


## Methods (Instance)

- ##### coupon.use_coupon(user=\<User Object\>) -> None


##### Example:

```python
from django.contrib.auth.models import User

from coupon_management.validations import validate_coupon
from coupon_management.models import Coupon

coupon_code = "COUPONTEST01"
user = User.objects.get(username="john_doe")

status = validate_coupon(coupon_code=coupon_code, user=user)
if status['valid']:
    coupon = Coupon.objects.get(code=coupon_code)
    coupon.use_coupon(user=user)
```

<hr>

- ##### coupon.get_discount() -> Dict

Returns a dict with two keys, with the discount ***value*** and if it's ***percentage*** or not.



##### Example:

```python
from django_simple_coupons.models import Coupon

coupon_code = "COUPONTEST01"
coupon = Coupon.objects.get(code=coupon_code)

discount = coupon.get_discount()  # Example: {'value': 50, 'is_percentage': True} 
```

<hr>

- ##### coupon.get_discounted_value(initial_value=<int/float>) -> Float

Returns a float with the new, discounted value.

##### Example:

```python
from coupon_management.models import Coupon

coupon_code = "COUPONTEST01"
coupon = Coupon.objects.get(code=coupon_code)

''' Example: Returns 50.0 if discount is 50% or 80.0 if discount is $20 '''
discount_value = coupon.get_discounted_value(initial_value=100.0)
```
