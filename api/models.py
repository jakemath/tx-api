# Definition of Transaction model

from django.db import models
import datetime

class Transaction (models.Model):	#Class contains each CSV column as a field
	id = models.IntegerField (default = -1, primary_key = True) #Additional field added to spreadsheet to enumerate entries
	user = models.IntegerField (default = -1)
	transaction_date = models.DateField (default = datetime.date.today)
	sales_amount = models.FloatField (default = -1.0)
	join_date = models.DateField (default = datetime.date.today)
	region = models.CharField (max_length = 1)
	
	class Meta:
		db_table = 'Transactions'	#Name of DB table
def __str__(self):    # Command line return format
	return '%s, %s, %s, %s, %s' % (str(self.num), str(self.user), self.transaction_date.strftime('%m/%d/%Y'), str(self.sales_amount), self.region)




