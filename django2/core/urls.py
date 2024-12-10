from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('curso/', login_required(CursoView.as_view()), name='curso'),
    path('doc', DocView.as_view(), name='doc'),
    path('contato/', ContatoView.as_view(), name='contato'),
    path('accounts/login/', Login.as_view(), name='login'),
]