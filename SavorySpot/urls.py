from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index-url'),
    path('contact', views.contact, name='contact-url'),
    path('book_a_table', views.book_a_table, name='Book-a-table-url'),
    path('grocery', views.grocery, name='grocery-url'),
    path('register', views.register_user, name='register_user-url'),
    path('login', views.login_user, name='login-url'),
    path('register_client', views.signup, name='signup-url'),
    path('make_an_order/<id>',views.make_an_order,name='make_an_order-url'),
]
