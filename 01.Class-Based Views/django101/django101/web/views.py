from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from django101.web.models import Todo


def index(request):
    # pure python func
    # - called with django request object
    # - returns django response
    context = {
        'title': 'Function-based view',
    }
    return render(request, 'index.html', context)


class IndexView(views.View):
    # Organization of code related to specific HTTP methods
    # (GET, POST, etc.) can be addressed
    # by separate methods instead of conditional branching.
    def get(self, request):
        context = {
            'title': 'Class-based view',
        }
        return render(request, 'index.html', context)

    # def post(self, request):
    #     pass


# we can also use a CBV as base view
class IndexTemplateView(views.TemplateView):
    template_name = 'index.html'

    # taking the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # take the context data from the parent
        context['title'] = 'Class-based with TemplateView'  # add the things that we want to change
        return context


class TodoListView(views.ListView):
    model = Todo
    template_name = 'todos-list.html'
    ordering = ('title', 'category__name')

    #     if we want to reverse the order just add "-"
    #     ordering = ('title', 'category__name')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

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
