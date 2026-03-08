from django.urls import path
from . import views

urlpatterns = [

    path('',views.login_view,name="login"),

    path('signup/',views.signup_view,name="signup"),

    path('dashboard/',views.dashboard,name="dashboard"),

    path('add/',views.add_note,name="add_note"),

    path('edit/<int:id>/',views.edit_note,name="edit"),

    path('delete/<int:id>/',views.delete_note,name="delete"),

    path('logout/',views.logout_view,name="logout"),
]