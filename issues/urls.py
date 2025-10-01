from django.urls import path
from .import views

urlpatterns = [
    path('', views.issues, name='issues'),
    path('issues/<str:member>', views.member_issue, name='member_issue'),
    path('open_issue', views.open_issue, name='open_issue'),
    path('update_issue/<path:issue>', views.update_issue, name='update_issue'),
    path('edit_issue/<int:id>', views.edit_issue, name='edit_issue'),
    path('delete_issue/<int:id>', views.delete_issue, name='delete_issue'),
    path('issue/<path:issue>', views.issue, name='issue'),    
#    path('issues/all_issue/<str:member>', views.all_member_issue, name='all_member_issue'),   
#    path('search/results/', views.search_results_view, name='search_results_view'),
  
]