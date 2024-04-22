from django.urls import path
from app.views import IndexView  # より具体的にインポート

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # ルートURLに対してIndexViewをマッピング
]
