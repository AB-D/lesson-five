from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView
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

    def get_context_data(self, **Kwargs):
        context = super(EntryCreateView, self).get_context_data(**kwargs)
        context['entry_list'] = self.model.objects.all()
        return context

    def get_success_url(self):
        return reverse('entry_list')

def entries(request):
    if request.method == 'POST':
        # Create our form object with our POST data
        entry_form = EntryForm(request.POST)
        if entry_form.is_valid():
            # If the form is valid, let's create and Entry with the submitted data
            entry = Entry()
            entry.start = entry_form.cleaned_data['start']
            entry.stop = entry_form.cleaned_data['stop']
            entry.project = entry_form.cleaned_data['project']
            entry.description = entry_form.cleaned_data['description']
            entry.save()
            return redirect('entry-list')
    else:
        entry_form = EntryForm()

    entry_list = Entry.objects.all()
    return render(request, 'entries.html', {
        'entry_list': entry_list,
        'entry_form': entry_form,
    })


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


