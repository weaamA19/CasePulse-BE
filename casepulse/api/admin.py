from django.contrib import admin
from .models import Case, Lawyer, Document, Reminder


# Register your models here.
admin.site.register(Case)
admin.site.register(Lawyer)
admin.site.register(Document)
admin.site.register(Reminder)
