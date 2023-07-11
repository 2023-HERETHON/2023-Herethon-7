from django.urls import path

from MatchZzic.main import admin
from . import views
from main.views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main, name='main'),
    path('createform/', views.createform, name='createform'),
    # 데이터 처리할 url 등록
]