from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Home, AddProduct, AddStock, SignUp, Logout, Users, UsersDelete, Login, Detail, Update, Delete, AddTextile, AddColor, AddImage, \
    AddImageDelete, Basket, DeleteOrder, DeleteColorView, Bought, Index, VerifyEmailView, VerifySuccessView, VerifyErrorView, get_available_sizes, get_available_quantities, \
    DeleteTextileView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('home/', Home.as_view(), name='home'),
    path('addgoods/', AddProduct.as_view(), name='addproduct'),
    path('addstock/', AddStock.as_view(), name='addstock'),
    path('addtextile/', AddTextile.as_view(), name='addtextile'),
    path('addtextile/delete_textile/<int:pk>/', DeleteTextileView.as_view(), name='delete_textile'),
    path('addcolor/', AddColor.as_view(), name='addcolor'),
    path('addcolor/delete_color/<int:pk>/', DeleteColorView.as_view(), name='delete_color'),    
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('users/', Users.as_view(), name='users'),
    path('users/<int:pk>/delete/', UsersDelete.as_view(), name='delete_users'),
    path('detail/<int:pk>/', Detail.as_view(), name='detail'),
    path('detail/<int:pk>/update/', Update.as_view(), name='update'),
    path('detail/<int:pk>/delete/', Delete.as_view(), name='delete'),
    path('get-available-sizes/', get_available_sizes, name='get-available-sizes'),
    path('get-available-quantities/',get_available_quantities, name='get-available-quantities'),    
    path('addgoods/<int:product_pk>/addimage/', AddImage.as_view(), name='addimage'),
    path('addgoods/<int:product_pk>/addimage/<int:image_pk>/delete/', AddImageDelete.as_view(), name='addimage_delete'),
    path('basket/<int:user_pk>/', Basket.as_view(), name='basket'),
    path('basket/<int:user_pk>/delete_order/<int:order_pk>/', DeleteOrder.as_view(), name='delete_order'),
    path('basket/<int:user_pk>/bought/', Bought.as_view(), name='bought'),
    path('verify/<int:user_pk>/<str:token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('verification_success/', VerifySuccessView.as_view(), name='verify_success'),
    path('verification_error/', VerifyErrorView.as_view(), name='verify_error'),    
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


