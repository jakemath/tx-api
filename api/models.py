# Definition of Transaction model

from django.db import models
import datetime

#Class contains each CSV column as a field
class Transaction(models.Model):
	id = models.IntegerField(default=-1, primary_key=True) 
	user = models.IntegerField(default=-1)
	transaction_date = models.DateField(default=datetime.date.today)
	sales_amount = models.FloatField(default=-1.0)
	join_date = models.DateField(default=datetime.date.today)
	region = models.CharField(max_length=1)
	class Meta:
		db_table = 'Transactions'	#Name of DB table
	def __str__(self):    # Command line return format
		out = str(self.num) + ', ' + str(self.user) + ', ' 
		out += self.transaction_date.strftime('%m/%d/%Y') + ', '
		out += str(self.sales_amount) + ', ' + self.region
		return out




