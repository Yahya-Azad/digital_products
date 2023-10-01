from django.contrib import admin

from .models import Category, Product, File


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent', 'title', 'is_enable', 'create_time']
    list_filter = ['is_enable', 'parent']
    search_fields = ['title']


# چون به ازای پروداکت های مختلف چندین فایل شاید وجود داشته باشه فایل رو اینلاین میکنیم به پروداکت
class FileInlineAdmin(admin.StackedInline):
    model = File
    fields = ['title', 'file_type', 'file',  'is_enable']
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_enable', 'create_time']
    list_filter = ['is_enable']
    search_fields = ['title']
    filter_horizontal = ['categories']  # واسه موقع سلکت کردن کتگوری های بیشتر از یکی از کنترل استفاده نکنیم
    inlines = [FileInlineAdmin]
