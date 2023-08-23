from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User = get_user_model()
#заголовок, описание,цена, датасоздания, дата обновления, торг
class Mmrrmma(models.Model):
    title = models.CharField('Заголовок',max_length=100)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена',max_digits=10, decimal_places=2)
    auction = models.BooleanField("Торг", help_text='Уместен ли торг?')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='пользователь', on_delete=models.CASCADE)
    image = models.ImageField("изображение", upload_to="mmrrmmas/")

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style=>green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='дата последнего обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_date.date() == timezone.now().date():
            created_time = self.updated_date.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        return self.updated_date.strftime("%d.%m.%Y в %H:%M:%S")

    def __str__(self):
        return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    class Meta:
        db_table = "advertisements"





#from app_mmrrmma.models import Mmrrmma
#mmrr1 = Mmrrmma (title = 'Молоко', description = 'Свежее молоко', price = 100, auction = True) создаю запись
#mmrr1.save() сохраняю
# from django.db import connection
# connection.queries - получаю все запросы к sql

