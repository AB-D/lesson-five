from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, RedirectView
from django.core.urlresolvers import reverse


from .forms import EntryForm, ProjectForm, ClientForm
from .models import Client, Entry, Project


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'clients.html'

    def get_context_data(self, **kwargs):
        context = super(ClientCreateView, self).get_context_data(**kwargs)
        context['client_list'] = self.model.objects.all()
        return context

    def get_success_url(self):
        return reverse("client-list")


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_detail.html'

    def get_success_url(self):
        return reverse('client-list')



class EntryCreateView(CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'entries.html'

    def get_context_data(self, **kwargs):
        context = super(EntryCreateView, self).get_context_data(**kwargs)
        context['entry_list'] = self.model.objects.all()
        return context

    def get_success_url(self):
        return reverse('entry-list')


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'projects.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectCreateView, self).get_context_data(**kwargs)
        context['project_list'] = self.model.objects.all()
        return context

    def get_success_url(self):
        return reverse('project-list')


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'project_detail.html'

    def get_success_url(self):
        return reverse('project-list')






