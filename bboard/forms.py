from django.forms import ModelForm  # импорт из страндартной библиотеки django

from .models import Bb    # Импорт класса Bb  из models.py
class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric')
        