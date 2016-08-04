# Metro-scrapy
Scrap the data from the Metro online shop, comparing with every other locations of shops


The key idea is to use the cookies to change the location of online shop so that the get the aim of comparing the price of the certain product.



The program use the multiprocess to ahcieve a relatie high speed, and store them in the CSV file in real-time, however I am not sure further increasing the speed would whether have any influcence on the storing process.


Several json files are provided , they are considered as the configs of the program. Every locations of the Metro online shop are included in the files, the sample one gives a light version for fast test.



To do list: For what I need is some unique products, so there is no changing pages function provided; Changing the cookies automatically is function urgently needed.

Based on windows 10 and pythno 2.7 , libraries needed can be found at the beginning of the file 
