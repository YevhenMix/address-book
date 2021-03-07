from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Resident
from .forms import ResidentForm, SearchForm


def main_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_text = form.data.get('search')
            residents = Resident.objects.filter(Q(first_name__icontains=search_text) |
                                                Q(last_name__icontains=search_text) |
                                                Q(country__icontains=search_text) |
                                                Q(city__icontains=search_text) |
                                                Q(street__icontains=search_text))
    else:
        residents = Resident.objects.all()
        form = SearchForm()
    paginator = Paginator(residents, 10)
    page = request.GET.get('page')
    residents = paginator.get_page(page)
    return render(request, 'residents/main.html', {'residents': residents, 'form': form})


class ResidentCreateView(SuccessMessageMixin, CreateView):
    model = Resident
    form_class = ResidentForm
    template_name = 'residents/create.html'
    success_url = reverse_lazy('residents:main')
    success_message = 'Добавлен новый житель'


class ResidentUpdateView(SuccessMessageMixin, UpdateView):
    model = Resident
    form_class = ResidentForm
    template_name = 'residents/update.html'
    success_url = reverse_lazy('residents:main')
    success_message = 'Информация о жителе обновлена'


def resident_delete_view(request, pk):
    if request.method == 'POST':
        resident = Resident.objects.get(id=pk)
        resident.delete()
        messages.error(request, 'Житель успешно удален')
    return redirect('residents:main')
