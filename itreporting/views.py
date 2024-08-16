from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Issue
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'itreporting/home.html')

def about(request):
    return render(request, 'itreporting/about.html')

def contact(request):
    return render(request, 'itreporting/contact.html')

def report(request):
    # Get all reported issues
    issues = Issue.objects.all()
    context = {'issues': issues, 'title': 'Issues Reported'}
    return render(request, 'itreporting/report.html', context)

class PostListView(ListView):
    model = Issue
    ordering = ['-date_submitted']
    template_name = 'itreporting/report.html'
    context_object_name = 'issues'
    paginate_by = 10  # Optional pagination

class UserPostListView(ListView):
    model = Issue
    template_name = 'itreporting/user_issues.html'
    context_object_name = 'issues'
    paginate_by = 5  # Optional pagination

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Issue.objects.filter(author=user).order_by('-date_submitted')

class PostDetailView(DetailView):
    model = Issue
    template_name = 'itreporting/issue_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    fields = ['type', 'room', 'urgent', 'details']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Issue
    fields = ['type', 'room', 'details']

    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Issue
    success_url = reverse_lazy('issue-list')  # Use reverse_lazy for URL resolution
    template_name = 'itreporting/issue_confirm_delete.html'  # Optional: Specify the template to use for the confirmation page

    def test_func(self):
        """Ensure that only the author of the issue can delete it."""
        issue = self.get_object()
        return self.request.user == issue.author

    def handle_no_permission(self):
        """Override the default behavior when the user does not have permission."""
        if self.request.user.is_authenticated:
            raise PermissionDenied
        return super().handle_no_permission()
