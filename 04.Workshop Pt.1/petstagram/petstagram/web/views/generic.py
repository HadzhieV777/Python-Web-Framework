# from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from petstagram.common.view_mixins import RedirectToDashboard
from petstagram.web.models import PetPhoto

from django.views import generic as views


# LoginRequiredMixin --> to check how to do it
class HomeView(RedirectToDashboard, views.TemplateView):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context



class DashboardView(views.ListView):
    model = PetPhoto
    template_name = 'main/dashboard.html'
    context_object_name = 'pet_photos'


def show_unauthorized(request):
    return render(request, 'main/401_error.html')
