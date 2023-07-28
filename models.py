from django.db import models

# Create your models here.

#заголовок, описание,цена, датасозданияЮ дата обновления, торг
class Mmrrmma(models.Model):
    title = models.CharField('Заголовок',max_length=100)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена',max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text='Уместен ли торг?')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Mmrrmma(id = {self.id}, title = {self.title}, price = {self.price})"


#настройки для таблицы
    class Meta:
        db_table = 'Advertisements'

#from app_mmrrmma.models import Mmrrmma
#mmrr1 = Mmrrmma (title = 'Молоко', description = 'Свежее молоко', price = 100, auction = True) создаю запись
#mmrr1.save() сохраняю
# from django.db import connection
# connection.queries - получаю все запросы к sql