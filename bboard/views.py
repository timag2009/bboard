#from django.shortcuts import render

# Create your views here.
# функция - сокращение render()

from django.shortcuts import render
from .models import Bb

# Код контроллера INDEX
def index(request):
     #bbs = Bb.objects.order_by('-pablished')
     bbs = Bb.objects.all()
     rubrics = Rubric.objects.all()
     context = {'bbs': bbs, 'rubrics': rubrics }
     return render(request, 'bboard/index.html', context)


# Код контроллера BY_RUBRIC
from .models import Rubric              # импорт Rubric из models.py 
def by_rubric(request, rubric_id):
     bbs = Bb.objects.filter(rubric=rubric_id)
     rubrics = Rubric.objects.all()
     current_rubric = Rubric.objects.get(pk=rubric_id) 
     context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
     return render(request, 'bboard/by_rubric.html', context)

# Код контроллера класса формы связанной с моделью
from django.views.generic.edit import CreateView

from .forms import BbForm               # BdForm импорт класса из forms.py
from django.urls import reverse_lazy

class BbCreateView(CreateView):
     template_name = 'bboard/create.html' # путь и имя шаблона формы
     form_class = BbForm                  # ссылка на класс формы из forms.py
     success_url =  reverse_lazy('index') # куда направить после успешного сохранения

     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs) # переопределяем метод get_context_data()
                                                       # который формирует контекст шаблона
          context['rubrics'] = Rubric.objects.all() # добавляем в контекст список рубрик
          return context                               # возвращаем контекст в качестве результата


