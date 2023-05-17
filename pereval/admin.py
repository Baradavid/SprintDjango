from django.contrib import admin
from .models import Users, PerevalAdded, PerevalAreas, PerevalImages, Coords

admin.site.register(Users)
admin.site.register(PerevalAdded)
admin.site.register(PerevalAreas)
admin.site.register(PerevalImages)
admin.site.register(Coords)


