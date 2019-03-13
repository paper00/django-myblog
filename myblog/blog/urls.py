from django.urls import path, include
from . import views

app_name = 'blog'
urlpatterns = [
    path('main/', views.main),
    path('classify/<article_category>', views.classify),
    path('article_page/<article_id>', views.article_page, name='article_page'),
    path('edit_page/<article_id>', views.edit_page, name='edit_page'),
    path('edit_action/', views.edit_action, name='edit_action'),
    path('delete/<article_id>', views.delete_action, name='delete_action'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('login_state/', views.login_state, name='login_state'),
    path('logout/', views.logout, name='logout'),
]
