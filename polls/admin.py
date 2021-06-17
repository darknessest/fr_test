from django.contrib import admin
from polls.models import *

admin.site.register(Question)
admin.site.register(Poll)
admin.site.register(MultipleChoiceAnswer)
admin.site.register(SingleChoiceAnswer)
admin.site.register(TextAnswer)
