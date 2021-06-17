from django.contrib import admin
from polls.models import *

admin.site.register(Question)
admin.site.register(Poll)
admin.site.register(BaseMultipleChoiceAnswer)
admin.site.register(BaseSingleChoiceAnswer)
admin.site.register(BaseTextAnswer)
