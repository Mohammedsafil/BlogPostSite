from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('',views.index ,name="Index"),
    path('post/<str:post_id>',views.detail, name="Detail"),
    path('new_changed_url/',views.new_url, name="new_page"),
    path('old_url/',views.old_url, name="old_page")
]