from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # static files (css, js, ...)

urlpatterns = [
    path('', account_view),
    path('all', view_all)
]


urlpatterns += staticfiles_urlpatterns()
