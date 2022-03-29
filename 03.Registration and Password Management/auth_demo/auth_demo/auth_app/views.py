from django.contrib.auth import get_user_model, login
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views
from django.contrib.auth import mixins as auth_mixins
from auth_demo.auth_app.forms import UserRegistrationForm

UserModel = get_user_model()


class RestrictedView(auth_mixins.LoginRequiredMixin, views.TemplateView):
    template_name = 'index.html'


class UserRegistrationView(views.CreateView):
    # if we want to extend the user form
    form_class = UserRegistrationForm
    # form_class = auth_forms.UserCreationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('index')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['profile_form'] = ProfileCreateForm()
    #     return context

    def form_valid(self, form):
        result = super().form_valid(form)
        #  user => self.objects
        #  request => self.request
        login(self.request, self.object)
        return result


# def login_user(request):
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     user = UserModel.objects.get(username=username)
#     login(request, user)

class UserLoginView(auth_views.LoginView):
    template_name = 'auth/login.html'

    def get_success_url(self):
        next = self.request.GET.get('next', None)
        if next:
            return next
        return reverse_lazy('index')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')
