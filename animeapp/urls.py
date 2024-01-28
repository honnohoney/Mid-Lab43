from django.urls import path, include
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_page),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('anime-list/', views.anime_list, name='anime-list'),
    path('add-anime/', views.add_anime, name='add-anime'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('search/', views.search_view, name='search'),
    path('register/', views.register_page, name='register'),
]

from django.contrib.auth.views import LogoutView

urlpatterns += [
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)