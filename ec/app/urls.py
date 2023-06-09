from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('category/<slug:val>/', views.CategoryView.as_view(), name="category"),    
    path('product-detail/<int:pk>/', views.ProductDetail.as_view(), name="product-detail"),    
    path('category-title/<val>/', views.CategoryTitle.as_view(), name="category-title"), 
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('update-address/<int:pk>/', views.UpdateAddressView.as_view(), name='update-address'),
    
    # login authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name="customer-registration"),   
    path('accounts/login/', auth_view.LoginView.as_view(template_name="app/login.html", 
        authentication_form=LoginForm), name="login"),    
    path('password-change/', auth_view.PasswordChangeView.as_view(template_name="app/change_password.html", 
        form_class=MyPasswordChangeForm), name="password_change"), 
    path('password-change-done/', auth_view.PasswordChangeDoneView.as_view(template_name="app/password_change_done.html"), 
         name="password_change_done"), 
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name="logout"),
    
    
    # password reset
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name="app/password_reset.html", 
        form_class=MyPasswordResetForm), name="password-reset"),
        
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(
        template_name='app/password_reset_done.html'), name='password_reset_done'),    
    
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name='app/password_reset_confirm.html'), form_class=MySetPasswordForm, name='password_reset_confirm'),
    
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(
             template_name='app/password_reset_complete.html'), name='password_reset_complete'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)