from django.contrib.auth.decorators import login_required
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from .forms import BirthdayForm, CongratulationsForm
from .models import Birthday, Congratulations
from .utils import calculate_birthday_countdown


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10


class BirthdayCreateView(CreateView):
    model = Birthday
    form_class = BirthdayForm


class BirthdayUpdateView(UpdateView):
    model = Birthday
    form_class = BirthdayForm


class BirthdayDeleteView(DeleteView):
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(self.object.birthday)
        context['form'] = CongratulationsForm()
        context['congratulations'] = self.object.congratulations.select_related('author')
        return context


@login_required
def add_comment(request, pk):
    birthday = get_object_or_404(Birthday, pk=pk)
    form = CongratulationsForm(request.POST)
    if form.is_valid():
        congratulation = form.save(commit=False)
        congratulation.author = request.user
        congratulation.birthday = birthday
        congratulation.save()

    return redirect('birthday:detail', pk=pk)

