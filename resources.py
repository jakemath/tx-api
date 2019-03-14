# api/resources.py

from tastypie.resources import ModelResource
from api.models import Transaction
from tastypie.authorization import Authorization

class TransactionResource (ModelResource): #Resource definition for reading csv files
	class Meta:
		queryset = Transaction.objects.all()
		resource_name = 'transaction'
		authorization = Authorization()

