from django.urls import path
from . import views

urlpatterns = [

    # HOME AND LOGIN
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),



    # SUPPLEMENTS PATH
    path('supplements/', views.supplements),  # this is the index page
    path('supplements/add/form/', views.supplements_form),
    path('supplements/submit_form/', views.submit_form),
    path('supplements/<int:p_id>/delete/', views.supplements_delete),


    # PRODUCTS PATH
    path('products/', views.products),
    path('products/add/form/', views.products_add),
    path('products/submit/', views.products_submit),
    path('products/<int:p_id>/delete/', views.products_delete),

    # LOG PAGES
    path('log/hair/', views.hair_log),
    path('log/skin/', views.skin_log),


    # HAIR
    path('log/hair/<int:hair_id>/', views.hair_detail),
    path('log/hairdiary/create_form/', views.create_form),
    path('log/hairdiary/submit_create_form/', views.submit_create_form),
    path('log/<int:hair_id>/delete/', views.delete),
    path('log/<int:hair_id>/edit/', views.edit_form),
    path('log/<int:h_id>/hairdiary/submit_update_form/', views.submit_update_form),


    # SKIN
    path('log/skindiary/create_form/', views.skin_create_form),
    path('log/skindiary/submit_create_form/', views.submit_skin_form),
    path('log/skin/<int:skin_id>/', views.skin_detail),
    path('log/skindiary/<int:s_id>/edit/', views.skin_edit_form),
    path('log/skindiary/<int:s_id>/skin_submit_update_form/',
         views.skin_submit_update_form),
    path('log/skindiary/<int:skin_id>/delete/', views.skin_delete),


    # PHOTO PATHS
    path('log/hair/<int:hair_id>/add_hair_photo/',
         views.add_hair_photo, name='add_hair_photo'),
    path('log/skin/<int:skin_id>/add_skin_photo/',
         views.add_skin_photo, name='add_skin_photo'),
]
