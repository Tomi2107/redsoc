from django.urls import path
from .views import UserProfileView, EditProfile

app_name="accounts"

urlpatterns = [
    path('<username>/', UserProfileView, name="profile"),
    path('profile/edit', EditProfile, name="edit-profile"),
    
]
