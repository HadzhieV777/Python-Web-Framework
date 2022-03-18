from django.urls import reverse_lazy
from petstagram.web.forms import AddPetForm, EditPetForm, DeletePetForm
from django.views import generic as views

from petstagram.web.models import PetPhoto


class CreatePetView(views.CreateView):
    template_name = 'main/pet_create.html'
    form_class = AddPetForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditPetView(views.UpdateView):
    template_name = 'main/pet_edit.html'
    form_class = EditPetForm
    success_url = reverse_lazy('dashboard')


class DeletePetView(views.DeleteView):
    template_name = 'main/pet_delete.html'
    form_class = DeletePetForm
    success_url = reverse_lazy('dashboard')

