### declaration
This site will be a marketplace for buying and selling watches, users will be able to **log** in to the site and leave **comments** and reply to **comments**, **bid** on offers, **place** an offer

so the site will have 3 types of user a Site Admin, sellers and buyers

the adverts should have a timer on them to expire to allow for bids to occur, timer set at advert creation and counts down on the card

database table will be
	comments
	comments on comments
	adverts
		popular boolean
		
	user accounts

technology used
	django
		oauth
		flatpages - used for about page
	summernote - expands the text input options such as adding: bold, fonts and sizing among others
	whitenoise - used to serve static files to Heroku
	crispy forms
	oauth
	elephantdb
	bootstrap
	

implementations

will try to do:
- the bid_timer does not have a function to coutndown the so it is a static number, if i cannot figure out how to implement it with heroku i may need to remove it as a feature to add later

- carousel of most liked listings, have the top 10 most liked listings on a carousled on the top of the page scrolling width ways adding a different effect than the scroll down

- main listing scroll effect, i want to add a independant scroll of the main listings section, this will one help to redice the over all height of the page and give the option to have a every growing list of items.
	

### bootstrap templates from:https://startbootstrap.com/

1. [Shop Homepage - Bootstrap Ecommerce Store Template - Start Bootstrap](https://startbootstrap.com/template/shop-homepage)

### referals

watch placeholder image - https://www.shopify.com/ie/partners/blog/placeholder-images

























---






![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for Codeanywhere. If you are using Gitpod then you need [this template](https://github.com/Code-Institute-Org/gitpod-full-template) instead.  We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Codeanywhere and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **August 30th, 2023**

## Codeanywhere Reminders

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere, in the terminal, type:

`python3 -m http.server`

A button should appear to click: _Open Preview_ or _Open Browser_.

To run a frontend (HTML, CSS, Javascript only) application in Codeanywhere with no-cache, you can use this alias for `python3 -m http.server`.

`http_server`

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A button should appear to click: _Open Preview_ or _Open Browser_.

In Codeanywhere you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to _Account Settings_ in the menu under your avatar.
2. Scroll down to the _API Key_ and click _Reveal_
3. Copy the key
4. In Codeanywhere, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

---

Happy coding!
