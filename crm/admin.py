from django.contrib import admin
from .models import Order, StatusCrm, CommentCrm

# Register your models here.
class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_dt','comment_text')
    readonly_fields = ('comment_dt',)
    extra = 1


class OrderAdm(admin.ModelAdmin):
    # для отображение таблицы с заказами
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')

    # для кликабельности полей в таблице
    list_display_links = ('id', 'order_name')

    # виджет поиска позволяющий искать данные по полям из кортежа
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')

    # фильтр по статусу
    list_filter = ('order_status',)

    # редактирование полей таблицы напрямую
    list_editable = ('order_status', 'order_phone')

    # количество полей таблицы на странице
    list_per_page = 10

    # максимальное количество показываемых полей
    list_max_show_all = 100

    fields = ('id', 'order_status', 'order_dt', 'order_name', 'order_phone')
    readonly_fields = ('id', 'order_dt')

    # поле класса коммент
    inlines = [Comment,]

admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)