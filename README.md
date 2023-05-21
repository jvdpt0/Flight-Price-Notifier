# Flight-Price-Notifier

Flight Price Notifier is an application that sends you an SMS when it finds flight deals for you, made using Twillio's API, Kiwi's API and Sheety's API.

For it to work you need to specify  your departure city and the date range from which you want to travel, you can change these values inside the flight_data_search function on flight_search.py
The application consults a google sheet (Sheety API) with previously added destinations and their lowest prices, it then uses these prices to compare with flights deals found using Kiwi's API, if the current deal price 
is lower than the lowest value on the sheet it sends you an SMS, using Twillio's API, letting you know a good deal from X to Y exists.
