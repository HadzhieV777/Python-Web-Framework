from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from petstagram.web.views.generic import HomeView, DashboardView, show_unauthorized
from petstagram.web.views.pet_photo import CreatePetPhotoView, PetPhotoDetailsView, like_pet_photo, \
    DeletePetPhotoView, EditPetPhotoView
from petstagram.web.views.pets import CreatePetView, EditPetView, DeletePetView

urlpatterns = [
                  path('', HomeView.as_view(), name='homepage'),
                  path('dashboard/', DashboardView.as_view(), name='dashboard'),
                  path('unauthorized/', show_unauthorized, name='unauthorized'),

                  path('pet/add/', CreatePetView.as_view(), name='add pet'),
                  path('pet/edit/<int:pk>/', EditPetView.as_view(), name='edit pet'),
                  path('pet/delete/<int:pk>/', DeletePetView.as_view(), name='delete pet'),

                  path('photo/add/', CreatePetPhotoView.as_view(), name='add photo'),
                  path('photo/edit/<int:pk>/', EditPetPhotoView.as_view(), name='edit photo'),
                  path('photo/delete/<int:pk>/', DeletePetPhotoView.as_view(), name='delete photo'),
                  path('photo/details/<int:pk>/', PetPhotoDetailsView.as_view(), name='photo details'),
                  path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
