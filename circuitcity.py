#https://media.boingboing.net/wp-content/uploads/2016/10/nicholas-eckhart.jpg
#http://money.cnn.com/news/specials/storysupplement/circuitcity/

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

# 1. save list of addresses as json
# 2. go to maps.google.com
# 3. paste address into search bar
# 4. hit enter key on search bar
# 5. wait 3 seconds
# 6. click zoom in button 3 times
# 7. click 3d button
# 8. tak screenshot
# 9. capture name of store from ad in left column