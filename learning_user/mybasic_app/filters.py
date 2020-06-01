import django_filters
from django_filters import CharFilter

from  mybasic_app.models import (Chercheur,Evaluateur,Article
,Conferance,User,Item)


class FilterClass(django_filters.FilterSet):
	name = CharFilter(field_name='name',lookup_expr='icontains')
	class Meta:
		model = Article
		fields=['name','Conferance']

	


