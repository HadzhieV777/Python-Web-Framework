from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from django101.web.models import Todo, Category


def permissions_required(required_permissions):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated or not user.has_perms(required_permissions):
                return HttpResponse('No permission')
            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator


# @login_required(login_url='/login-with-fb')  # the param 'login_url' will overwrite the 'LOGIN_URL'
# to check if the user is  logged for func-based view
# will take the 'LOGIN_URL' from the settings that we declared
@permissions_required(required_permissions=['web.change_category'])
def index(request):
    if not request.user.is_authenticated:  # same as the 'login_required' decorator
        redirect('login')

    # print(request.user)
    #
    # print(authenticate(
    #     request,
    #     username='pesho_mashinata', # User == pesho_mashinata
    #     password='123QwER',
    # ))
    #
    # print(authenticate(
    #     request,
    #     username='pesho_mashinata', # User == None
    #     password='12QER',
    # ))
    #
    # print(authenticate(
    #     request,
    #     username='pesho',  # User == None
    #     password='123QwER',
    # ))
    user = authenticate(
        request,
        username='pesho1',
        password='1123QwER',
    )
    # check if user is in content_creator & content_manager
    # Change in admin requires new code
    #  => "content_reviewer"
    # if user.has_perm('web.change_category'):
    #     cat = Category.objects.get(pk=4)
    #     cat.name = 'New Name'
    #     cat.save()
    #
    # if user:
    #     login(request, user)

    context = {
        'title': 'Function-based view',
    }
    return render(request, 'index.html', context)


# If we want to implement the @login_required logic on CBV we use a LoginRequiredMixin
class IndexView(LoginRequiredMixin, views.View):
    def get(self, request):
        context = {
            'title': 'Class-based view',
        }
        return render(request, 'index.html', context)


class IndexTemplateView(views.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Class-based with TemplateView'
        return context


class TodoListView(views.ListView):
    model = Todo
    template_name = 'todos-list.html'
    ordering = ('title', 'category__name')

    def get_queryset(self):
        queryset = super().get_queryset()
        # queryset.prefetch_related('category_set')
        title_filter = self.request.GET.get('filter', None)
        if title_filter:
            queryset = queryset.filter(title__contains=title_filter)

        return queryset


class TodoDetailsView(views.DetailView):
    model = Todo
    template_name = 'todo-details.html'
    context_object_name = 'todo'


class CreateTodoForm:
    pass


class TodoCreateView(views.CreateView):
    model = Todo
    template_name = 'todo-create.html'
    success_url = reverse_lazy('todos list')  # When the same for each create
    fields = ('title', 'description', 'category')
    #     we can pass custom forms
    # form_class = CreateTodoForm # first way when is the same
    #
    # def get_form_class(self): # when the form will be different

    # When different based on the create
    # def get_success_url(self):
    #     pass

# def sample():
#     pk = 1
#     Todo.objects.get(pk=pk)
#     Todo.objects.filter(pk=pk).get()


# # the RedirectView generate all the queries and returns the result from self.get()
# class RedirectToIndexView(views.RedirectView):
#     # url = reverse_lazy('index class-based')
#     def get_redirect_url(self, *args, **kwargs):
#         # by overwriting the above method will allow us to apply a branching if needed
#         if ...:
#             return 'place 1'
#         else:
#             return 'place 2'
