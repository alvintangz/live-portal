from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.views import redirect_to_login
from django.contrib import messages
from django.conf import settings

class IsTypeMixin:
    """
    Verify that the user is of a specific type by calling function.
    """
    def is_delegate(self):
        user = self.request.user
        return user.is_delegate and hasattr(user, 'delegate')
    
    def is_partner(self):
        user = self.request.user
        return user.is_partner and hasattr(user, 'partner')
    
    def is_judge(self):
        user = self.request.user
        return user.is_judge and hasattr(user, 'judge')

class TypesRequiredMixin(AccessMixin, IsTypeMixin):
    """
    Verify that the current user is of a specific type or specific types.
    """
    delegate_allowed = False
    partner_allowed = False
    judge_allowed = False

    def dispatch(self, request, *args, **kwargs):
        # User is not authenticated
        if not request.user.is_authenticated:
            messages.error(request, "Please login to continue to use the app.")
            return self.handle_no_permission()
        # User account is not activated (exception: is_staff)
        if not request.user.activated and not request.user.is_staff:
            messages.error(request, ("Your account has not been activated. " +
                "If you think this is a mistake, please contact us at " + 
                f"{settings.MANAGER_EMAIL}."))
            return redirect_to_login(
                self.request.get_full_path(),
                self.get_login_url(), 
                self.get_redirect_field_name())
        # User account is of a specific type asked, then continue
        if ((self.delegate_allowed and self.is_delegate()) or 
            (self.partner_allowed and self.is_partner()) or 
            (self.judge_allowed and self.is_judge())):
            return super().dispatch(request, *args, **kwargs)
        # Last option: User is authenticated but is not allowed
        return self.handle_no_permission()

class DelegateRequiredMixin(TypesRequiredMixin):
    """
    Verify that the current user is just a delegate.
    """
    delegate_allowed = True

class PartnerRequiredMixin(TypesRequiredMixin):
    """
    Verify that the current user is just a partner.
    """
    partner_allowed = True

class JudgeRequiredMixin(TypesRequiredMixin):
    """
    Verify that the current user is just a judge.
    """
    judge_allowed = True