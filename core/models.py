from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    score = models.FloatField(_('Puntuación'), null=True, blank=True)
    nickname = models.CharField(_('Apodo'), blank=True, max_length=80)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    def __str__(self):
        return '%s' % self.first_name

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['first_name']


# Create your models here.
class Match(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(_('Fecha del partido'), null=True, blank=True)
    validated = models.BooleanField(default=False)

    player_a1 = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.SET_NULL, related_name='player_a1')
    player_a2 = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.SET_NULL, related_name='player_a2')
    player_b1 = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.SET_NULL, related_name='player_b1')
    player_b2 = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.SET_NULL, related_name='player_b2')

    set1_a = models.IntegerField(_('Puntuación set 1 pareja A'), blank=True, null=True)
    set1_b = models.IntegerField(_('Puntuación set 1 pareja B'), blank=True, null=True)
    set2_a = models.IntegerField(_('Puntuación set 2 pareja A'), blank=True, null=True)
    set2_b = models.IntegerField(_('Puntuación set 2 pareja B'), blank=True, null=True)
    set3_a = models.IntegerField(_('Puntuación set 3 pareja A'), blank=True, null=True)
    set3_b = models.IntegerField(_('Puntuación set 4 pareja B'), blank=True, null=True)

    # def __str__(self):
    #     return '%s %s VS %s %s | %s' % (self.player_a1.first_name,
    #                                     self.player_a2.first_name,
    #                                     self.player_b1.first_name,
    #                                     self.player_b2.first_name,
    #                                     self.date)

    def __str__(self):
        return '%s %s' % (self.date, self.player_a1.first_name)

    class Meta:
        ordering = ['date']
        verbose_name = 'Partido'
        verbose_name_plural = 'Partidos'
