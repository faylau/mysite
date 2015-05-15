# coding=utf-8

from django.contrib import admin
from books.models import Publisher, Author, Book


"""
1.将models加入到Admin管理中
2.ModelAdmin类可对Model类管理进行定制
"""


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date' # 在管理界面上对日期字段进行层次划分
    ordering = ('-publication-date', )
    # 算定义编辑表单字段
    fields = ('title', 'authors', 'publisher', 'publication_date')
    # 自定义Many-to-Many字段的编辑，使用前先将fields注释掉
    filter_horizontal = ('authors',)
    # 将外键字段展现为文本框而非下拉框，提高数据加载和展示效率
    raw_id_fields = ('publisher', )


admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
