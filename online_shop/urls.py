"""
URL configuration for online_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from users.views import (CreateUserView, LoginUserView, RecoverPasswordView,
                         RecoveryCodeView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/users", CreateUserView.as_view(), name="create_user"),
    path("api/v1/login", LoginUserView.as_view(), name="login_user"),
    path("api/v1/users/recovery-code", RecoveryCodeView.as_view(), name="recovery_code"),
    path("api/v1/users/recover-password", RecoverPasswordView.as_view(), name="recover_password"),
]
