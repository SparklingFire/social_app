from django.contrib import admin
from .models import (RatingModel, UserRating, Vote)


admin.site.register(RatingModel)
admin.site.register(UserRating)
admin.site.register(Vote)
