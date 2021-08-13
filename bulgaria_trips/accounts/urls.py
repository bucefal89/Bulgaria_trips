from django.urls import path
from bulgaria_trips.accounts import views

urlpatterns = [
    path('sign-up/', views.sign_up, name="sign up"),
    path('sign-in/', views.sign_in, name="sign in"),
    path('sign-out/', views.sign_out, name="sign out"),
    path('profile/', views.profile_details, name='profile details'),
    path('profile/delete/<int:pk>', views.ProfileDeleteView.as_view(), name='delete profile')
    # path('delete/', views.delete_profile, name='delete profile')
]