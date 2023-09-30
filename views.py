from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

class CustomLogoutView(LogoutView):
    """
    Custom logout view that extends the LogoutView.
    Redirects to the specified LOGOUT_REDIRECT_URL from settings.
    """
    next_page = settings.LOGOUT_REDIRECT_URL

@method_decorator(never_cache, name="dispatch")
class CustomLoginView(LoginView):
    """
    Custom login view that extends the LoginView.
    Uses the 'accounts/login.html' template and the default AuthenticationForm.
    Displays a success message upon successful login.
    """
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm

    def form_valid(self, form):
        user = form.get_user()
        messages.success(self.request, f'Logged in as {user.email}')
        return super().form_valid(form)

class CustomPasswordChangeView(PasswordChangeView):
    """
    Custom Password Change View that extends PasswordChangeView.
    Uses the specified template and the default PasswordChangeForm.
    Redirects to a customizable success URL.
    """
    form_class = PasswordChangeForm
    template_name = 'accounts/change_password.html'  # Replace with your template name

    def get_success_url(self):
        # Use a custom success URL if provided in project settings, or use a default URL
        return getattr(settings, 'PASSWORD_CHANGE_SUCCESS_URL', "/")
