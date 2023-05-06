from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .permissions import OwnerRquiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from . import models


class CoursesListView(ListView):
    model = models.Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = models.Course
    template_name = 'courses/course_details.html'
    context_object_name = 'course'

class CourseUpdateView(LoginRequiredMixin, OwnerRquiredMixin, UpdateView):
    model = models.Course
    fields = ('title', 'slug', 'subject', 'overview')
    template_name = 'courses/course_create.html'
    login_url = reverse_lazy('users:login')

    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse('courses:course-detail', kwargs={'pk': pk})

class CourseDeleteView(LoginRequiredMixin, OwnerRquiredMixin, DeleteView):
    model = models.Course
    template_name = 'courses/course_delete.html'
    context_object_name = 'course'
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('courses:course-list')



    #def form_valid(self, form):

class CourseCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Course
    fields = ('title', 'slug', 'subject', 'overview', 'course_image')
    template_name = 'courses/course_create.html'
    success_url = reverse_lazy('users:login')
    permission_required = 'courses.add_course'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
