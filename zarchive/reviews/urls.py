from django.urls import path, include
from zarchive.reviews import views

urlpatterns = [
    path('edit/', views.ReviewEditView.as_view(), name='review_edit_page'),
    path('delete/', views.ReviewDeleteView.as_view(), name='review_delete_page'),
]
