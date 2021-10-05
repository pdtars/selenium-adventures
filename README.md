# Selenium Adventures

Just a fun name for some random scripts where I'm using Selenium to 
automate tasks in the browser.

###01. Cookie Clicker  
https://orteil.dashnet.org/cookieclicker/

Ever wanted to see how far one can go in this addictive game,
but without the hassle of breaking your mouse or being frowned 
upon by your carpal tunnel?

This script is set to run for 5 minutes, and will automatically 
buy store items and upgrades, prioritizing those that become available
first considering the cookie count (money).

##### Requires:
* Google Chrome (I despise it, but it's the most well developed webdriver out there, I think...)
* Python 3.6+

##### Steps:

1. Just run it 🙂


##### Footnotes
* Depending on your hardware/internet, the script may run faster than they can keep up, resulting in errors.
  * Tweak `time.sleep()` if that happens.
* After running the first time, the script will output a **save_file.txt**.
  * Uncomment this row to load your game afterwards: `#load_game("save_game.txt")`
* To keep it running for longer than 5 mins, change the constant (300 in this case):
  * `baking_timer = time.time() + 300` , where 300 is the number of seconds.