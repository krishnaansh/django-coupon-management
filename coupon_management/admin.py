from django.contrib import admin

from coupon_management.models import (Coupon,
                                          Discount,
                                          Ruleset,
                                          CouponUser,
                                          AllowedUsersRule,
                                          MaxUsesRule,
                                          ValidityRule)

from coupon_management.actions import (reset_coupon_usage, delete_expired_coupons)


# Register your models here.
# ==========================
@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'ruleset', 'times_used', 'created', )
    actions = [delete_expired_coupons]


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    pass


@admin.register(Ruleset)
class RulesetAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'allowed_users', 'max_uses', 'validity', )


# @admin.register(CouponUser)
# class CouponUserAdmin(admin.ModelAdmin):
#     list_display = ('user', 'coupon', 'times_used', )
#     actions = [reset_coupon_usage]


@admin.register(AllowedUsersRule)
class AllowedUsersRuleAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


@admin.register(MaxUsesRule)
class MaxUsesRuleAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}


@admin.register(ValidityRule)
class ValidityRuleAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}
