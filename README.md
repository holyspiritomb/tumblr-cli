# tumblr-cli
Very bare-bones interactive tumblr client for making posts.

# Features
* Make text, chat, link and quote posts with tags!
* HTML input allowed in the post body, except for chat posts.
* Post privacy options: published, draft, queue and private.

# To be implemented in the future
* Photo, photoset, video and audio posts
* A message showing success or failure
* An error message if you aren't authenticated

# Setting up your environment
1. Make sure you have python >= 3.6 installed with the ```venv``` module (this is sometimes listed in package managers as ```python3-venv```).
2. Clone this repository: ```git clone https://github.com/pianycist/tumblr-cli.git```
3. Create a new python virtual environment, e.g. ```python3 -m venv tumblr-venv```
4. Activate the new virtual environment, e.g. ```source tumblr-venv/bin/activate``` (if using bash). If your shell is not bash, examine the contents of ```tumblr-venv/bin``` for the appropriate script, e.g. ```source tumblr-venv/bin/activate.fish``` if you are using fish.
5. Enter the ```tumblr-cli``` directory: ```cd tumblr-cli```
6. Execute ```pip3 install -r requirements.txt```.

# Getting data to fill the config file
1. [Register a new application with tumblr.](https://www.tumblr.com/oauth/register) The application website can be anything: I just input ```https://metapianycist.tumblr.com``` for it. For the default callback URL, put ```http://127.0.0.1/```. Input the consumer key and consumer secret into the correct places in ```configuration.py```.
2. Open the [Tumblr API Console](https://api.tumblr.com/console), input your consumer key and consumer secret, and click Authenticate. When it has authenticated you, click "Show keys" in the upper righthand corner. Copy the  keys into the correct places in ```configuration.py```.
3. Fill in your username in the selected_blog area.
4. Make sure each token in ```configuration,.py``` is surrounded with double quotes. (I just started learning python a few months ago on my own in my spare time and I haven't figured out how to get around this limitation yet.)

# Usage
1. Activate the virtual environment you created.
2. ```cd tumblr-cli```
3. ```python3 tumblrclient.py```
4. The script will ask you to input things. Title and tags can be left blank.
5. You can cancel a post in progress at any time before entering tags by pressing CTRL+C.
