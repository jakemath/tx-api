# REST API
An implementation of a REST API framework using Python Django.

The program uses a model called 'transaction' which contains the fields 'id', 'user', 'transaction_date', 'sales_amount', 'join_date', and 'region' to parse the data in the 'transaction_.csv' files. The data is contained in a SQLite database courtesy of Django.

The code queries the data to compute the following metrics: Revenue, Active User Count (Number of users who have made at least one transaction in the given year), New User Count (Number of users who have joined in the given year) Average Revenue per Active User (Revenue / Active User Count), and returns the result as a JSON expression. The output is formatted as such:

    {“<metric>”: { “2013”: [xxx], “2014”: [xxx], “2015”: [xxx], “2016”: [xxx]}}
where xxx contains the value of the metric for the given year. The query is made by entering the url:

    http://restapi2-env.ph2p2zpdk5.us-west-1.elasticbeanstalk.com/dataengr/<metric>/
and the options for metric are /revenue/, /activeusers/, /newusercount/, /arpau/ (average revenue per active user).

I've deactivated the virtual environment for this app on AWS to avoid incurring charges when not being used, but feel free to message me if you would like to see this app in action.
