from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.web.forms import DeletePetPhotoForm
from petstagram.web.models import PetPhoto


class CreatePetPhotoView(auth_mixins.LoginRequiredMixin, views.CreateView):
    model = PetPhoto
    template_name = 'main/photo_create.html'
    fields = ('photo', 'description', 'tagged_pets')
    success_url = reverse_lazy('dashboard')

    # if no form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditPetPhotoView(views.UpdateView):
    model = PetPhoto
    template_name = 'main/photo_edit.html'
    fields = ('tagged_pets', 'description')
    success_url = reverse_lazy('dashboard')


class DeletePetPhotoView(views.DeleteView):
    template_name = 'main/photo_delete.html'
    model = PetPhoto
    success_url = reverse_lazy('dashboard')


class PetPhotoDetailsView(views.DetailView):
    model = PetPhoto
    template_name = 'main/photo_details.html'
    context_object_name = 'pet_photo'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('tagged_pets')

    # Everything that is received from the view
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # self.object.user = PetPhotoUser
        # self.request.user = currently logged user
        context['is_owner'] = self.object.user == self.request.user
        return context


def like_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()

    return redirect('photo details', pk)
