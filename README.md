### declaration
This site will be a marketplace for buying and selling watches, users will be able to **log** in to the site and leave **comments** and reply to **comments**, **bid** on offers, **place** an offer

so the site will have 3 types of user a Site Admin, sellers and buyers

the adverts should have a timer on them to expire to allow for bids to occur, timer set at advert creation and counts down on the card

### database table will be
	comments
	comments on comments
	adverts
	popular boolean
		
	user accounts

### technology used
	django
		allauth - django built in user authentication 
		flatpages - used for about page
	summernote - expands the text input options such as adding: bold, fonts and sizing among others
	whitenoise - used to serve static files to Heroku
	crispy forms
	oauth
	elephantdb
	bootstrap

## bugs

### django flatpages, 
	read up that this would be a great way to display a static page like a about page instead of creating a model for something that does not change. but running into major issues getting it to run.

	steps taken:
	added middleware to prevent the necessity for having a url pattern
	remove middleware and added urlpattern to watchbidcentral urls.py
	added "APPEND_SLASH = True" to help troubleshoot
	in the flatpages admin section add domains for all known such as gitpod, heroku localhost

	so far have not been able to resolve the issue, might end up scrapping the implementation. but moving on with the project for now to swin back.

	going to scratch this and opt for a standard mobel implementation, I have been unable to implement flatpages, keep getting 404 error. And this is taking up too much time.

### Like Button
	in setting up the like button to increment the database entry I had to use Javascript, but so far the error ""GET /like_listing/32/ HTTP/1.1" 401 36" appears and the button updates to remove the like count and only show the heart. 
	not that when logged in that the function works but need to add a presentable error to the user when not logged in offering them to signup and make sure the likes count does not get removed

### Listing images not loading on watch_detail page
	fixed, the issue was the iteration was incorrect
	

### Price showing as "{{ listing.price }}" instead of integer
	fixed by removing the if statment to show either the price of the bid, these should be shown seperately


### example code to enter image to readme
	<img src="assets\images\README-images\snake_board.png" alt="Picture of Snake Play board" width= 600px>

### implementations

	things left:
	bid timer count down - could have removed
	shop link filtering - should have added my listings
	like count icon on watch detail page - must have
	nested comments - could have removed
	about page - must have
	create listing form - must have (logged in users) - done
	automated testing - could have
	readme - must have
	like model - to track who likes and prevent mutiple likes from one user - removed
	

	will try to do:
	- the bid_timer does not have a function to coutndown the so it is a static number, if i cannot figure out how to implement it with heroku i may need to remove it as a feature to add later

	- carousel of most liked listings, have the top 10 most liked listings on a carousled on the top of the page scrolling width ways adding a different effect than the scroll down - done

	- main listing scroll effect, i want to add a independant scroll of the main listings section, this will one help to reduce the over all height of the page and give the option to have a every growing list of items.

 	- Nested Comments, I want to have the ability to have nested comments and them to display on the listing page. stack overflow link to get started https://stackoverflow.com/questions/56596266/how-to-make-nested-replies-for-comments-in-django
	
### testing

login
logout
view liked carousel
view listing list
create listing
edit listing
delete listing
view my liked listings
view my listings
write a comment

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
