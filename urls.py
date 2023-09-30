from django.urls import path
from apps.accounts import views
from django.contrib.auth.decorators import login_required

app_name = "accounts"


urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    # Use the login_required_decorator for logout and change_password views.
    path("logout/", login_required(views.CustomLogoutView.as_view()), name="logout"),
    path("change_password/", login_required(views.CustomPasswordChangeView.as_view()), name="change-password"),
]
