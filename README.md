searching for abandoned red circuit city storefronts across america
===

![abandoned circuit city storefront](https://media.boingboing.net/wp-content/uploads/2016/10/nicholas-eckhart.jpg)

http://money.cnn.com/news/specials/storysupplement/circuitcity/

http://articles.latimes.com/2009/jan/17/business/fi-circuitcity17/2

[Data src](https://www.slideshare.net/finance22/circuit-city-stores-store-closing-list-11609-updated-information-2909-1045am-et) (see `locations.txt`)

steps:
0. save list of addresses as json

selenium: 
1. go to maps.google.com
2. wait 5 seconds
2. paste address into search bar
3. hit enter key on search bar
4. wait 10 seconds
5. click 360 view image on left side panel (to escape "map view" and get satellite view) 
6. wait 10 seconds
7. click zoom out button 3 times
8. wait 15 seconds
9. take screenshot (https://stackoverflow.com/a/6282203/1757149)
10. capture name of current store from ad in left side panel
11. create new json with uid (matching saved image filename), address, and current store name

##Step 0:

The data contains the following items: Store #, Store Name, Street Address, City, State, ZIP for all stores. Using regex on `locations.txt` in sublime text to remove everything but the address:

`[ ]{1}[0-9]{5}(?![0-9])`

Finds all addresses (5 digit numbers), so that a newline can be added immediately following each one to deliniate between list items when `readlines()` is executed on this file from python.

Next:

`[\n][0-9]*(?=[ ])`

Finds any series of digits between newline and a space, which is the first set of digits in each entry, in order to delete them.

Next:

`[\n](\D)+(?![0-9])`

Finds all chars between newline and the first digit that is anything but a digit, in order to delete them and be left with just the address of each entry.

Finally delete the Puerto Rican address because its format is different. Result: `locations_pretty.txt`

##THIS ERROR

`selenium.common.exceptions.ElementNotInteractableException: Message: Element <input id="searchboxinput" class="tactile-searchbox-input" name="q"> is not reachable by keyboard`

:((

