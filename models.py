from django.db import models
from curr_conv import fields
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Rates(models.Model):

    base = models.CharField(max_length=3, verbose_name=_('CURR_BASE_FIELD'))
    created = models.DateTimeField('CURR_BASE_CREATED')
    name = models.CharField(max_length=100, verbose_name=_('CURR_NAME_FIELD'))
    symbol = models.CharField(max_length=3, verbose_name=_('CURR_SYMBOL_FIELD'))
    unit = models.IntegerField(verbose_name=_('CURR_UNIT_FIELD'))
    spread = models.DecimalField(max_digits=4,decimal_places=2,verbose_name=_('CURR_SPREAD_FIELD'))
    average = fields.CurrencyField(verbose_name=_('CURR_CURRENCY_FIELD'))
    supplier = models.CharField(max_length=100, verbose_name=_('CURR_SUPPLIER_FIELD'))                               
