from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Match


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('id', 'first_name', 'last_name', 'nickname', 'score', 'email', 'is_active',)
    list_filter = ('is_active', 'is_staff', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Basic', {'fields': ('first_name', 'last_name', 'nickname', 'score')}),
        ('Dates', {'fields': ('last_login', 'date_joined')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'nickname', 'is_staff',
                       'is_active')}
         ),
    )

    readonly_fields = ('score',)
    search_fields = ('email', 'first_name', 'last_name')


admin.site.register(CustomUser, CustomUserAdmin)


class MatchAdmin(admin.ModelAdmin):
    list_display = ('date', 'player_a1', 'player_a2', 'player_b1', 'player_b2', 'set1', 'set2', 'set3', 'validated')
    search_fields = ['player_a1__first_name', 'player_a2__first_name', 'player_b1__first_name', 'player_b2__first_name']
    list_filter = ('date', 'validated')

    def set1(self, obj):
        if obj.set1_a and obj.set1_b:
            return '%s %s' % (obj.set1_a, obj.set1_b)
        return ''

    def set2(self, obj):
        if obj.set2_a and obj.set2_b:
            return '%s %s' % (obj.set2_a, obj.set2_b)
        return ''

    def set3(self, obj):
        if obj.set3_a and obj.set3_b:
            return '%s %s' % (obj.set3_a, obj.set3_b)
        return ''


admin.site.register(Match, MatchAdmin)
