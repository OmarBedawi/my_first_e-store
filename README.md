# E-Book Store
![E-Book Store](https://github.com/SDGreen/elwood-castle/blob/master/flat_pages/static/flat_pages/images/background.jpg?raw=true)
### Deployed site: [https://omar-e-book-store.herokuapp.com/](https://omar-e-book-store.herokuapp.com/)

#### For testing the following credentials can be used:
* User Credentials:  
  - Username: create your username  
  - Password: create your password  
  - Email: use your own e-mail to receive the confirmation link to activate your account OR create a temporary e-mail on [temp-mail](https://temp-mail.org/it/)

* Card payments:
  - Card number: 4242 4242 4242 4242
  - Zip & CCV must be filled out with any integers
---
## Table of Contents
1. [Aim](#aim)
2. [User Experience (UX)](#user-experience-(ux))
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Credits](#credits) 
---
## Aim
The aim of this Django app is to create an interactive interface where users can find out
e-book titles and their relative informations.  
This app is to be a one stop shop where users can create accounts and purchase e-books.

---
## User Experience (UX)
### User Stories
#### Shopper:

##### VIEWING AND NAVIGATION
| As a... | I would like... | So I can ... |
| :------ | :-------------- | :----------- |
| Shopper | View a list of products | Select some to purchase |
| Shopper | View individual product details | Identify price, authors, description, year, product rating and product image|
| Shopper | Easy view of the total of my purchase at any time | Avoid spending too much |

##### SORTING AND SEARCHING
| As a... | I would like... | So I can ... |
| :------ | :-------------- | :----------- |
| Shopper | Sort the list of available products | Easily identify the best rated, best price and categorically sorted products |
| Shopper | Sort a specific category of product | Find the best-rated or best-priced product in a specific category, or sort the products in that category by name |
| Shopper | Sort multiple categories of produts simultaneously | Find the best-priced or best-rated products across broad categories, such as "Nature" of "Medicine" |
| Shopper | Search for a product by title or description | Find a specific product I'd like to purchase |
| Shopper | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available |

##### PURCHASING AND CHECKOUT
| As a... | I would like... | So I can ... |
| :------ | :-------------- | :----------- |
| Shopper | Easily select the quantity of a product when purchasing it | Ensure I don't accidentaly select the wrong product or quantity |
| Shopper | View items in my bag to be purchased | Identify the total cost of my purchase and all items I will receive |
| Shopper | Adjust the quantity of individual items in my bag | Easily make changes to my purchase before checkout |
| Shopper | Easily enter my payment information | Checkout quickly and with no hassles |
| Shopper | Feel my personal and payment informations is safe and secure | Confidently provide the needed information to make a purchase |
| Shopper | View an order confirmation after checkout | Verify that I haven't made any mistakes |
| Shopper | Receive an email confirmation after checking out | Keep the confirmation of what I've purchased for my records |

#### Site User:
##### REGISTRATION AND USER ACCOUNTS
| As a...   | I would like... | So I can ... |
| :------   | :-------------- | :----------- |
| Site User | Easily register for an account | Have a personal account and be able to view profile |
| Site User | Easily login or logout | Access my personal account information |
| Site User | Easily recover my password in case I forget it | Recover access to my account |
| Site User | Receive an email confirmation after registering | Verify that my account registration was successful |
| Site User | Have a personalized user profile | View my personal order history and order confirmations, and save my payment information |

#### Store Owner:
##### ADMIN AND STORE MANAGEMENT
| As a... | I would like... | So I can ... |
| :------ | :-------------- | :----------- |
| Store Owner | Add a product | Add new items to my store |
| Store Owner | Edit/update a product | Change product prices, descriptions, images and other product criteria |
| Store Owner | Delete a product | Remove items that are no longer for sale |




### Information Architecture
#### Overview
E-Book Store works with a relational database using SQL.
The reason behind this choice is because users can't directly add items to the database which
would have wildly unknown values. All orders would follow the same structure which is where the
users have most control over what is inputted. 
The models built in the Django framework provide great validation to prevent incorrect values being added, 
so it's extremely unlikely that E-Book Store would need a database structure like MongoDB where unknown values 
are expected to be inputted frequently.

The information in each model would also be related to another model in many cases. 
Having such interlinked models required a relational database to easily
handle the data and prevent creating a large database with many repeated values.
---

#### Models 

##### UserProfile
This model builds on the user model provided by Django. 

This model maintain default delivery information and order history
| Field | Field Type | Validation |
| :---- | :--------- | :--------- |
| user | OneToOneField | User, on_delete=models.CASCADE |
| default_phone_number | CharField | max_length=20, null=True, blank=True |
| default_street_address1 | CharField | max_length=80, null=True, blank=True |
| default_street_address2 | CharField | max_length=80, null=True, blank=True |
| default_town_or_city | CharField | max_length=40, null=True, blank=True |
| default_county | CharField | max_length=80, null=True, blank=True |
| default_postcode | CharField | max_length=20, null=True, blank=True |
| default_country | CountryField | blank_label='Country', null=True, blank=True |


##### Ebooks 
This model stores and display to the user, the informations of every book and a picture of its cover.
| Field | Field Type | Validation |
| :---- | :--------- | :--------- |
| category | ForeignKey | (related field) Category, null=True, blank=True, on_delete=models.SET_NULL |
| sku | CharField | max_length=254, null=True, blank=True |
| title | CharField | max_length=254 |
| authors | CharField | max_length=254, default='' |
| year | CharField | max_length=254, default='' |
| description | TextField |  |
| price | DecimalField | max_digits=6, decimal_places=2 |
| rating | DecimalField | max_digits=6, decimal_places=1, null=True, blank=True |
| image_url | URLField | max_length=1024, null=True, blank=True |
| image | ImageField | null=True, blank=True |

##### Category
This is a simple model used to store the different types of categories each book can belong to.
New categories can be easily added if the store decides to start selling new types of books.
| Field | Field Type | Validation |
| :---- | :--------- | :--------- |
| name | CharField | max_length=254 |
| friendly_name | CharField | max_length=254, null=True, blank=True |

##### Order
This is a simple model used to create and store orders.
This model is capable to generate an order number every time a user complete an order. 
It's relation to OrderLineItem and UserProfile allows users to see their upcoming
and past orders on their profile page. It also has a stripe_pid field for validation, 
preventing orders from being created twice by mistake.
| Field | Field Type | Validation |
| :---- | :--------- | :--------- |
| order_number | CharField | UserAccount, null=True, blank=True, on_delete=models.SET_NULL, related_name='orders' |
| user_profile | ForeignKey | max_length=32, null=False, editable=False |
| full_name | CharField | max_length=100, null=False, blank=False |
| email  | EmailField | max_length=200, null=False, blank=False |
| phone_number | CharField | max_length=200, null=False, blank=False |
| country  | CountryField | max_length=20, null=True, blank=True |
| postcode | CharField | auto_now_add=True |
| town_or_city  | CharField | max_length=27, null=False, blank=False |
| street_address1 | CharField | max_length=27, null=False, blank=False |
| street_address2 | CharField | max_length=27, null=False, blank=False |
| county | CharField | max_length=27, null=False, blank=False |
| date | DateTimeField | max_length=27, null=False, blank=False |
| order_total  | DecimalField | max_length=27, null=False, blank=False |
| grand_total  | DecimalField | max_length=27, null=False, blank=False |
| original_bag | TextField | max_length=27, null=False, blank=False |
| stripe_pid  | CharField | max_length=27, null=False, blank=False |


##### OrderLineItem
This model is used to display the informations contained in an order placed by a user.
The OrderLineItem's relation to the Order model is used to show upcoming and past orders on the user's profile page.
 
| Field | Field Type | Validation |
| :---- | :--------- | :--------- |
| order | ForeignKey | (related model) Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' |
| ebook | ForeignKey | (related model) Ebook, null=False, blank=False, on_delete=models.CASCADE |
| quantity | IntegerField | null=False, blank=False, default=0 |
| lineitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False |

---

# OMAR




### Wireframes
All wireframes can be found [Here](https://github.com/SDGreen/elwood-castle/tree/master/wireframes)  
I reccomend viewing the [Navbar](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/navbars.pdf)
and [Footer](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/footers.pdf) files first to give context to the rest of the wireframes.  
For individual files, please click the relevant name:
  * [Navbar](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/navbars.pdf)
  * [Footer](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/footers.pdf)
  * [Index page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/index.pdf)
  * [Events page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/events.pdf)
  * [Event Details page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/event-detail.pdf)
  * [Book Event page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/book-event.pdf)
  * [View Basket page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/view-basket.pdf)
  * [Checkout page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/checkout.pdf)
  * [Checkout Success page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/checkout-success.pdf)
  * [User Home page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/user-home.pdf)
  * [Order Summary page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/order-summary.pdf)
  * [Visit page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/visit.pdf)
  * [FAQ page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/faq.pdf)
  * [Contact page](https://github.com/SDGreen/elwood-castle/blob/master/wireframes/contact.pdf)

  Please note that these wireframes may not match the finished product. Some elements
  may be moved or changed based on feedback or styling issues discovered during development.
  
# OMAR  

### Design Choices
#### Overview
For the E-Book Store website, the design took inspiration from other e-book websites. 
Looking at [ebooks.com](https://www.ebooks.com/en-nl/), [bookboon.com](http://bookboon.com/), 
[hoepli](https://www.hoepli.it/), [feedbooks](http://www.feedbooks.com/publicdomain) & the 
[ebooklobby](http://www.ebooklobby.com/) websites identified aspects to include (heritage fonts, large vista images).

##### Layout
E-Book Store website, compared with the other websites mentioned above is presenting a much
cleaner and tidier layout, in order to obtain a high UX and is responsive for 
every screen size.

##### Images
The background image of the Homepage is coming from a google research.

The e-book cover images have been borrowed from [ebooks.com](ebooks.com/en-nl/)

##### Fonts
To keep brand consistency, [Google Fonts Lato](https://fonts.google.com/specimen/Lato)
is used as the main font of the entire E-Book Store website. In my opinion it giving 
a neat and tidy look the content pages.


##### Colours
The main two colors used for this project are black and white.

In most of the project is black on white except for the magazine banner that 
is white on black, together with some other few buttons like "Add to Bag", 
"Go to Secure Checkout", "Secure Checkout" and "Complete Order".
These two colors make text easily readable for users, especially when it comes to e-book descriptions. 
They provide a good contrast and a positive UX.

Other colors are used when the flash messages appear:
* Green for Success
* Blue for Alert
* Yellow for Warning
* Red for Danger
---

## Features
### Existing Features
* #### Dynamic Search Bar 
    * E-Books can be searched by title and description using the search bar.
    * Dropdown menus allow the user to search by price, rating & category (highest to lowest and vice versa).
    * Number of results for searches and categories is dynamically displayed on the page, just before the list of e-Books.

# OMARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR

* #### Dynamic Event Cards
    * Each event card features an image of the event or the stock missing image
    if no image has been uploaded for the event.
    * On larger screens, the price and rating are displayed on each card; on smaller
    pages these are hidden to keep the page looking tidy.
    * Each card has links to the event details page and a direct link to the booking page.
    * The number of cards per row changes dynamically depeninding on screen size, 
    this keeps the page looking uncluttered and prevents the images from becoming too 
    small to understand or comically large.
* #### Dynamic Event Details Page 
    * Each event has an event details page which renders the information stored in the database. 
    * The layout shifts depending on screen size to keep the information easy to read.
    * The information within the "Key Details" and "Notes" sections changes depending on 
    the event's category, if it requires adult supervision, or is age restricted.
* #### Smart Date Picker
    * The date picker automatically disables fully booked dates (days where the amount of 
    tickets booked matches the event's 'day_ticket_limit' value), along with dates over a year in 
    the future, one day in the future, past days of the current month, Christmas dates and New Years day when the 
    castle is closed. 
    * The date picker searches the user's basket to prevent them from booking too many tickets 
    even if the values aren't present in the database.
    * The ticket input alerts users to available tickets for their chosen date and warns them 
    if this value is 5 or less. If the available tickect value is 0, but the date isn't disabled 
    due to the user having these tickets in their basket (which isn't checked when disabled 
    dates are generated) then the input is disabled and the user is asked to pick a new date.
* #### Smart Ticket Update input
    * Users can update their ticket quantities in their basket. The update script checks 
    the database for bookings to make sure the day_ticket_limit of that event isn't exceeded.
* #### Stripe Payments 
    * Users can checkout and purchase event tickets using the Stripe API.
* #### Smart Checkout Validator
    * User details and basket are validated twice before the stripe API is called to make 
    the payment. Once to check the user details are valid, along with checking that no
    tickets in the basket somehow exceed the day_ticket_limit of the event they are purchasing.
    If ticket quantities in the basket do exceed the day_ticket_limit, then they are removed 
    from the basket. This feature also prevents users from purchasing tickets that may have been 
    in their basket, whilst other users have already purchased the maximum tickets for that day, thus 
    preventing overbooking.
    If there are any issues with the details or basket items the payment can't take place 
    and the page is reloaded showing the user an error message and assuring them the purchase hasn't 
    gone through.
* #### Checkout Redundancy
    * If somehow the user navigate away from the checkout page before the order is submitted 
    to the database then it is created in the webhooks.
* #### Order and Booking Confirmation/Emails
    * Once a payment is successful the user gets an email confirming their order, along 
    with individual emails for bookings which they can use to pick up their tickets. 
    * Once an order is created the user is redirected to a checkout summary page displaying 
    information about that order.
* #### Account Creation 
    * Users can create an account with Elwood Castle, this automatically creates 
    a UserAccount entry for the User in the database. They can use the account to 
    view previous orders, upcoming and past events.
* #### User Account
    * Users can store their details and use them next time 
    a user reaches checkout.
    * User details can be updated from their account page. This will not affect their 
    user details (username, email, password) and this is outlined under the update details form.
* #### Password Reset 
    * Users can update their password using their email if they have forgotton their current 
    one.
* #### Contact Form
    * Users can send emails to Elwood's Gmail account using the contact form. 
    If the user is logged in, it will preload their saved email into the email 
    field of the form.
* #### Toast Alerts 
    * Throughout the site Toast alerts are used to give the user feedback, such as 
    when a user logs in, logs out, adds items to a basket, removes/updates 
    basket items, checks out out successfully etc.
    * Alerts change colour depending on the type of message used to create them, 
    red for error, green for success and blue for information (i.e. email verification emails being sent).
* #### Responsive Basket
    * The basket won't allow users to checkout if their basket is empty.
    * If the basket is empty it offers a link back to events page.
* #### Responsive Fixed Navbar
  * Includes dropdown links to account pages which change depending on if the 
  user is logged in, a superuser or an anonymous user.
  * Logo text disappears on smaller screens, key elements (basket and account dropdown) 
  remain as icons, whilst less essential links are stored in a mobile dropdown.
  * Logo image changes size depening on screen size.
  * Due to it's small size it remains fixed to the top of the page to eliminate the need
  for a "back to top" button.
* #### Simple Footer
    * Footer remains consistent across the site and includes three social links and a link
    to the creator's github page. All external links create a new tab rather than change the 
    current windows location. 
    The social links aren't live and so currently redirect back to the index page with a
    message explaining why.
* #### Dismissable Alert Banner
    * On the events page, a banner appears linking users to the FAQ page if they want 
    information about Elwood Castle's Covid-19 policy.
    * The banner is dismissable but reappears each time a user goes to the events page 
    where it's message is most important.
* #### Dynamic Landing Page 
    * Has a scrolling background of Elwood Castle's grand vista images.
    * Elwood's logo appears above the key links highlighted on the page.
    * On very small devices the less used contact link is removed to maintain 
    the balance of the page.

### Features Left to Implement
* #### Subscription Service
    * In future it would be great to create a subscription service where uses pay 
    either per year or month, which entitles them to a certain amount of free 
    tickets.
* #### Real-time Ratings 
    * A future feature would be to allow users to rate events which automatically 
    updates an event's rating in real-time.
* #### Ticket Reservation
    * With sites like Ticketmaster, tickets are held for a period of time and cannot 
    be booked whilst another user has them in their basket. Currently this feature 
    is not deemed necessary as Elwood Castle doesn't deal with the types of volumes 
    that a major arena deals with but it would be good to add in future.
* #### Styled Superuser Dashboard 
    * With more time, a nicely styled dashboard would be created for super users.
    Currently it is just the standard Django admin dashboard which is usable but 
    one fitting with the rest of the site would be better for UX.
* #### Custom 404 Page 
    * Fairly self explanatory, but this feature wasn't deemed necessary for the site 
    to be deployed.

---
## Technologies Used
### Languages
* [HTML5](https://html.spec.whatwg.org/multipage/) - Used to create the structure of the website.
* [CSS3](https://www.w3.org/Style/CSS/Overview.en.html) - Used to style the website.
* [JavaScript](https://www.javascript.com/) - Used for stripe functionality, as well as Bootstrap & Google maps API functionality and the date-picker element.
* [Python (v3.8.6)](https://www.python.org/) - Used to handle backend programming within the Django framework.
### Libraries
* [Google Fonts](https://fonts.google.com/) - Used for website fonts [Lora](https://fonts.google.com/specimen/Lora) for headings, [Raleway](https://fonts.google.com/specimen/Raleway) for content text and [IM Fell French Canon SC](https://fonts.google.com/specimen/IM+Fell+French+Canon+SC) for logo text.
* [Font Awesome](https://fontawesome.com/) - This library provided the Icons used across the site.
* [jQuery](https://jquery.com/) - Included with Bootstrap, also used to code various elements such as the date picker, stripe functionality and Google maps API.
* [Stripe API Library](https://stripe.com/gb) - Used to handle the payments send from the Elwood Website.
### Frameworks
* [Django v3.1.4](https://docs.djangoproject.com/en/3.1/) - Framework used to create the app along with inbuilt templating language.
* [Bootstrap v4.5](https://getbootstrap.com/docs/4.5/getting-started/introduction/) - Framework to add structure & styling to the site, along with
responsive breakpoints and pre-built elements.
### Tools 
* [Git](https://git-scm.com/) - Used for version control and tracking changes to the code whilst in development.
* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - Key for finding bugs and testing responsive design.
* [Autoprefixer](https://autoprefixer.github.io/) - Used to prefix the CSS, allowing it to work across different browsers.
* [AWS S3](https://aws.amazon.com/s3/) - Used for storing static and media files used across the site.
* [Heroku](https://www.heroku.com/home) - Used to deploy and host the finished site.
* [Heroku Postgres](https://www.heroku.com/postgres) - Used to serve the database Elwood Castle manages event and user data with.
---
## Testing
See the [testing write up](https://github.com/SDGreen/elwood-castle/blob/master/TESTING.md) for full details on testing.

---
## Deployment

### How to run Elwood Castle's code locally:
The Elwood Castle app was coded using the GitPod IDE. The git repository is stored locally before being pushed 
to the remote repository online at GitHub.

To run Elwood Castle's app locally you will need the following:
    * Python installed on your environment
    * An AWS account
    * A Stripe account
    * A Google maps API key

#### Setting up the code:

1. Go to: [https://github.com/SDGreen/elwood-castle](https://github.com/SDGreen/elwood-castle)
2. Click the "Code" button next to the "Gitpod" button which will have a dropdown including "Clone with HTTPS",
"Open with GitHub Desktop" & "Download ZIP"
3. To clone the repository using HTTPS, under "Clone with HTTPS", click the copy to clipboard icon. To clone the
repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click the copy to clipboard icon.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to appear.
7. Type git `clone`, and then paste the URL you copied in Step 3 (https://github.com/SDGreen/elwood-castle.git).
8. Install the requirements by typing `pip3 install -r requirements.txt` in your CLI
9. Finally create a superuser using `python3 manage.py create superuser`

#### Creating a database:
1. To use the local version of the database first type `python3 manage.py makemigrations`
2. Then migrate (`python3 manage.py migrate`) the migrations so that your local db.sqlite3
database included with Django is setup.
3. To use the same data as this Elwood Castle site, type `python3 manage.py loaddata`
4. You now have a local version of the database.

#### Adding environment varibales:
In either your `env.py` file or your environment settings (like GitPod offers) you'll need to
add the following  environment variables:

    * SECRET_KEY = <Your secret key>
    * STRIPE_PUBLIC_KEY = <Stripe public key>
    * STRIPE_SECRET_KEY = <Stripe secret key>
    * STRIPE_WH_SECRET  = <Wehhook key>
    * AWS_ACCESS_KEY_ID = <Your AWS access key id>
    * AWS_S3_REGION_NAME  = <Your AWS region name>
    * AWS_SECRET_ACCESS_KEY = <Your AWS secret key>
    * AWS_STORAGE_BUCKET_NAME = <Your AWS bucket name>

While technically not an environment variable, you'll also need to add your Google API key to this file:  
`flat_pages/templates/flat_pages/visit.html`  
Add your key to this script tag in the file:   
`<script async defer
    src="https://maps.googleapis.com/maps/api/js?key<YOUR_KEY_HERE>&callback=initMap"
    type="text/javascript"></script>`  
Make sure you restrict your Google API to just your local environment (and deployed site if created)

#### Running the app
1. If you are using your AWS bucket to serve the static and media files, go to the bucket and create 
a file named `media/`
2. Export all the files in your local environment directory `media`, to the `media/` file in your AWS bucket.
3. You are ready to run the code locally!

### Deploying to Heroku
1. If you have added any new packages which the code requires to run, type `pip3 freeze > requirements.txt`
to creat a requirements file.
2. If you have deleted the Procfile, create a new one containing: `web: gunicorn elwood_castle.wsgi:application` in your root directory.
3. Create a new app in Heroku, if you want to use Heroku Postgres to serve your database you can do so 
by going to the dashboard *resources*>*add-ons* and attaching the Heroku Postgres database.
    * Please note, you will need to make your migrations and load the data to the new Postgres database as detailed above in 
  the **Creating a database** steps. Ensure the DATABASE_URL variable matches that in your Heroku App's 
  **Config Vars**
4. Add your environment variables as detailed in the steps for **Adding environment variables** above
to your apps **Config Vars** including this new variable:  
USE_AWS = True
5. Download the Heroku CLI if you haven't already (found under the *Deploy* tab on the dashboard).
6. Login to Heroku using `heroku login`
7. Set up a remote repository connected to you Heroku app: `git remote add heroku <your heroku git URL>`
    * If you're unsure of your Heroku git URL it can be found under *settings* on the dashboard.
8. Finally push your code to the Heroku remote repo after making any change.  
`git add .`   
`git commit -m "some change"`  
`git push heroku master`

The site is now deployed remotely.

---
## Credits

### Content
* All copy was written by myself.
* Fake phone number provided by [Fake Number](https://fakenumber.org/uk/london).

### Media
Copyright free images taken from [Pxhere](https://pxhere.com/)
* [Archer](https://pxhere.com/en/photo/1410420) (file name: archer.jpg)
* [Armour Set](https://pxhere.com/en/photo/615382) (file name: helmet.jpg)
* [Baking](https://pxhere.com/en/photo/757323) (file name: baking.jpg)
* [Banquet Hall](https://pxhere.com/en/photo/830346) (file name: banquet.jpg)
* [Blacksmith's Forge](https://pxhere.com/en/photo/1272972) (file name: blacksmith.jpg)
* [Carousel](https://pxhere.com/en/photo/879353) (file name: carousel.jpg)
* [Dried flowers](https://pxhere.com/en/photo/1231000) (file name: perfume.jpg)
* [Coat of Arms](https://pxhere.com/en/photo/535891) (file name: crest.jpg)
* [Crossed Swords](https://pxhere.com/en/photo/1570543) (file name: swords.jpg)
* [Crayons](https://pxhere.com/en/photo/608898) (file name: caryons.jpg)
* [Elwood Castle](https://pxhere.com/en/photo/1056258) (file name: background.jpg)
* [Elwood Gardens](https://pxhere.com/en/photo/1190433) (file name: background-gardens.jpg)
* [Elwood Grounds](https://pxhere.com/en/photo/1398482) (file name: background-grounds.jpg)
* [Falcon](https://pxhere.com/en/photo/551960) (file name: falcon.jpg)
* [Gallery Hall](https://pxhere.com/en/photo/1059117) (file name: halls.jpg)
* [Haunted Hall](https://pxhere.com/en/photo/870234) (file name: spooky.jpg)
* [Jousting Knight](https://pxhere.com/en/photo/590971) (file name: joust.jpg)
* [Kid's Castle](https://pxhere.com/en/photo/862705) (file name: small-castle.jpg)
* [Knight](https://pxhere.com/en/photo/687171) (file name: knight.jpg)
* [Library](https://pxhere.com/en/photo/707871) (file name: library.jpg)
* [Mead Bottles](https://pxhere.com/en/photo/1032511) (file name: bottles.jpg)
* [Missing Image Placeholder](https://pxhere.com/en/photo/1334124) (file name: no-image.jpg)
* [Old Kitchen](https://pxhere.com/en/photo/1069371) (file name: kitchen.jpg)
* [Puppet](https://pxhere.com/en/photo/896895) (file name: puppet.jpg)
* [Sparkler](https://pxhere.com/en/photo/1169641) (file name: sparkler.jpg)
* [Spice Market](https://pxhere.com/en/photo/959535) (file name: spices.jpg)
* [Tapestry](https://pxhere.com/en/photo/575238) (file name: tapestry.jpg)
* [Teacup](https://pxhere.com/en/photo/649039) (file name: tea.jpg)
* [Castle Vista](https://pxhere.com/en/photo/843450) (file name: vista.jpg)
* [Wine Glasses](https://pxhere.com/en/photo/733330) (file name: romantic.jpg)

Logos created using [Canva](https://www.canva.com/):
* [Color Logo](https://github.com/SDGreen/elwood-castle/blob/master/static/logos/logo_color.jpg) (file name: logo_color.jpg)
* [Dark Logo](https://github.com/SDGreen/elwood-castle/blob/master/static/logos/logo_dark.png) (file name: logo_dark.png)
* [Large Dark Logo](https://github.com/SDGreen/elwood-castle/blob/master/static/logos/logo_dark_large.png) (file name: logo_dark_large.png)
* [Light Logo](https://github.com/SDGreen/elwood-castle/blob/master/static/logos/logo_light.png) (file name: logo_light.png)
* [Navbar Logo](https://github.com/SDGreen/elwood-castle/blob/master/static/logos/navbar_logo.png) (file name: navbar_logo.png)


Favicon created using [Favicon.io](https://favicon.io/favicon-converter/) from edited logo:
* [Favicon](https://github.com/SDGreen/elwood-castle/blob/master/static/logos/favicon.png) (file name: favicon.png)

### Code
* Card, Navbar, Accordian and Form elements adjusted from [Bootstrap 4 examples](https://getbootstrap.com/docs/4.5/getting-started/introduction/).
* Google map created using [Google Maps JS API](https://developers.google.com/maps/documentation/javascript/tutorial).
* Date picker created using [bootstrap-datepicker](https://bootstrap-datepicker.readthedocs.io/en/latest/).
* CSS prefixer used: [https://autoprefixer.github.io/](https://autoprefixer.github.io/).
* Every effort has been taken to avoid this apps code from becoming too similar to the
[Boutique Ado](https://github.com/ckz8780/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546) 
Code Institute mini project but it was a very helpful tool in setting up the site.
* README stucture borrows heavily from the [Code institute readme example](https://github.com/Code-Institute-Solutions/SampleREADME#)

### Acknowledgements
A massive thank you to my mentor Antonio Rodriguez for his continuous and helpful feedback (even in the face of tropical storms).   
Thanks also to the kind people at Tutor Support who went above and beyond to help me fix issues.  
Finally, a big thank you to Sharon Luff for helping me start my journey into coding and providing great moral support along the way.  




---
