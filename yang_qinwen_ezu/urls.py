from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', RedirectView.as_view(
        pattern_name='about_urlpattern',
        permanent=False
    )),
    path('login/',
         LoginView.as_view(template_name='courseinfo/login.html'),
         name='login_urlpattern'),
    path('logout/',
         LogoutView.as_view(),
         name='logout_urlpattern'),
    path('about/', TemplateView.as_view(
        template_name='courseinfo/about.html'),
        name='about_urlpattern'
    ),
    path('admin/', admin.site.urls),
    path('', include('courseinfo.urls'))
]

