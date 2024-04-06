from abc import ABC
from django.contrib import admin
from django.db.models import CharField
from django.db.models.functions import Lower
from .models import Team, Player

CharField.register_lookup(Lower)


# Register your models here.
class CollegeFilter(admin.SimpleListFilter, ABC):
    title = 'college'
    parameter_name = 'college'

    def lookups(self, request, model_admin):
        colleges = set(model_admin.model.objects.distinct().values_list(Lower('college'), flat=True))
        res = [(clg, clg) for clg in colleges]
        return res

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(college__lower=self.value())
        return queryset


@admin.register(Player)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'gender', 'college')
    list_filter = ('gender', CollegeFilter)
    search_fields = ('email',)


admin.site.register(Team)
