from django.urls import path
from . import views

urlpatterns = [
    path('omikuji/', views.OmikujiView.as_view(), name="omikuji"),
    path('omikuji/result/', views.OmikujiResultView.as_view(), name='omikuji_result'),
]


# viewsがclassベースで定義されている場合
# path('omikuji/', views.OmikujiView.as_view(), name='omikuji')
# ".as_view()"がつく。class名大文字はじまり
# 関数ベースで定義されている場合
# path('omikuji/', views.omikujiView, name='omikuji')
# 命名規則を検討しても良いかもしれない
