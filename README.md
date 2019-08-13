# REST API
An implementation of a REST API framework using Python Django.

The program defines the 'transaction' model with fields 'id', 'user', 'transaction_date', 'sales_amount', 'join_date', and 'region' to parse transaction CSV files. The data is contained in a default SQLite database.

Views are defined for computing the following metrics: Revenue, Active User Count (Number of users who have made at least one transaction in the given year), New User Count (Number of users who have joined in the given year) Average Revenue per Active User (Revenue / Active User Count), and returns the result as a JSON expression. The output is formatted as such:

    {“<metric>”: { “2013”: [xxx], “2014”: [xxx], “2015”: [xxx], “2016”: [xxx]}}
    
where xxx contains the value of the metric for the given year. While running the server, the query is made by entering the url:

    http://***localhost***.com/dataengr/<metric>/
    
where the options for <metric> are /revenue/, /activeusers/, /newusercount/, /arpau/ (average revenue per active user).

I've deactivated the virtual environment for this app on AWS to avoid incurring charges when not being used, but feel free to message me if you would like to see this app in action.
