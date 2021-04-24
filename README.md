# E-Book Store
![E-Book Store](https://github.com/OmarBedawi/my_first_e-store/blob/master/readme_files/readme_images/ebook.png?raw=true)
### Deployed site: [https://omar-e-book-store.herokuapp.com/](https://omar-e-book-store.herokuapp.com/)

#### For testing, the following credentials can be used:
* User Credentials:  
  - Username: create your username  
  - Password: create your password  
  - Email: to receive confirmation of registration and orders you can use your own e-mail OR, create a temporary e-mail on [temp-mail](https://temp-mail.org/en/)

* Superuser Credentials:  
  - Username: TestSuperUser  
  - Password: testingebook  

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
e-Book titles and e-Book readers with useful details.  
With this app a user, can create his/her own profile and, purchase e-Books and eventually e-Book readers.

---
## User Experience (UX)
### User Stories
#### Shopper:

##### VIEWING AND NAVIGATION
| As a... | I would like... | So I can ... |
| :------ | :-------------- | :----------- |
| Shopper | View a list of products | Select some to purchase |
| Shopper | View individual e-Books details | Identify price, authors, description, year, rating and image|
| Shopper | View individual e-Book reader details | Identify brand, model, description, screen and memory size, rating and image|
| Shopper | Easy view of the total of my purchase at any time | Always be aware of how much I'm spending |

##### SORTING AND SEARCHING
| As a... | I would like... | So I can ... |
| :------ | :-------------- | :----------- |
| Shopper | Sort the list of available products | Easily identify the best rated, best price and categorically sorted products |
| Shopper | Sort a specific category of product | Find the best-rated or best-priced product in a specific category, or sort the products in that category by name |
| Shopper | Sort multiple categories of produts simultaneously | Find the best-priced or best-rated products across broad categories |
| Shopper | Search for an e-Book by title or description | Find a specific e-Book I'd like to purchase |
| Shopper | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available |

##### PURCHASING AND CHECKOUT
| As a... | I would like... | So I can ... |
| :------ | :-------------- | :----------- |
| Shopper | Easily select the quantity of a product when purchasing it | Ensure I don't accidentaly select the wrong product or quantity |
| Shopper | View items in my shopping bag to be purchased | Identify the total cost of my purchase and all items I will receive |
| Shopper | Adjust the quantity of individual items in my shopping bag | Easily make changes to my purchase before checkout |
| Shopper | Easily enter my payment information | Checkout quickly and with no hassles |
| Shopper | Feel my personal and payment informations are safe and secure | Confidently provide the needed information to make a purchase |
| Shopper | View an order confirmation after checkout | Verify that I haven't made any mistakes |
| Shopper | Receive an email confirmation after checking out | Keep the confirmation of what I've purchased for my records |

#### Site User:
##### REGISTRATION AND USER ACCOUNTS
| As a...   | I would like... | So I can ... |
| :------   | :-------------- | :----------- |
| Site User | Easily register a new account | Have a personal account and be able to see your profile |
| Site User | Easily login or logout | Access my personal account information |
| Site User | Easily recover my password in case I forget it | Recover access to my account |
| Site User | Receive an email confirmation after registering | Verify that my account registration was successful |
| Site User | Have a personalized user profile | See my personal order history and order confirmations, and save my personal and delivery informations |

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

##### Ebooks App
###### Category
This is a simple model used to store the different type of categories each book or reader can belong to.
New categories can be easily added by the store owner.
| Field | Field Type | Validation |
| :---- | :--------- | :--------- |
| name | CharField | max_length=254 |
| friendly_name | CharField | max_length=254, blank=True |

###### Ebook
This model stores and displays the informations of every book and a cover's picture.
| Field | Field Type | Validation |
| :---- | :--------- | :--------- |
| category | ForeignKey | (related field) Category, null=True, blank=True, on_delete=models.SET_NULL |
| sku | CharField | max_length=254, blank=True |
| title | CharField | max_length=254 |
| authors | CharField | max_length=254, default='' |
| year | CharField | max_length=254, default='' |
| description | TextField |  |
| price | DecimalField | max_digits=6, decimal_places=2 |
| rating | DecimalField | max_digits=6, decimal_places=1, null=True, blank=True |
| image_url | URLField | max_length=1024, blank=True |
| image | ImageField | blank=True |

###### Ebook_reader
This model stores and displays the informations of every e-Book reader and a product's picture.
| Field | Field Type | Validation |
| :---- | :--------- | :--------- |
| category | ForeignKey | (related field) Category, null=True, blank=True, on_delete=models.SET_NULL |
| sku | CharField | max_length=254, blank=True |
| brand | CharField | max_length=254 |
| model | CharField | max_length=254, default='' |
| size | CharField | max_length=254, default='' |
| memory | CharField | max_length=254, default='' |
| description | TextField |  |
| price | DecimalField | max_digits=6, decimal_places=2 |
| rating | DecimalField | max_digits=6, decimal_places=1, null=True, blank=True |
| image_url | URLField | max_length=1024, blank=True |
| image | ImageField | blank=True |

##### Checkout App
###### Order
This is a simple model used to create and store orders.
This model is capable to generate an order number every time a user complete an order. 
Its relation to OrderLineItem, OrderLineReader and UserProfile allows users to see their past orders 
on their profile page. It also has a stripe_pid field for validation, 
preventing orders from being created twice by mistake.
| Field | Field Type | Validation |
| :---- | :--------- | :--------- |
| order_number | CharField | max_length=32, null=False, editable=False |
| user_profile | ForeignKey | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' |
| full_name | CharField | max_length=50, null=False, blank=False |
| email  | EmailField | max_length=254, null=False, blank=False |
| phone_number | CharField | max_length=20, null=False, blank=False |
| country  | CountryField | blank_label='Country *', null=False, blank=False |
| postcode | CharField | max_length=20, null=True, blank=True |
| town_or_city  | CharField | max_length=40, null=False, blank=False |
| street_address1 | CharField | max_length=80, null=False, blank=False |
| street_address2 | CharField | max_length=80, null=True, blank=True |
| county | CharField | max_length=80, null=True, blank=True |
| date | DateTimeField | auto_now_add=True |
| order_total  | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 |
| grand_total  | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 |
| original_bag | TextField | null=False, blank=False, default='' |
| stripe_pid  | CharField | max_length=254, null=False, blank=False, default='' |


###### OrderLineItem
This model is used to display the e-Books informations contained in an order placed by a user.
The OrderLineItem's relation to the Order model is used to show past orders with the relative details on the user's profile page.
 
| Field | Field Type | Validation |
| :---- | :--------- | :--------- |
| order | ForeignKey | (related model) Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' |
| ebook | ForeignKey | (related model) Ebook, null=False, blank=False, on_delete=models.CASCADE |
| quantity | IntegerField | null=False, blank=False, default=0 |
| lineitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False |


###### OrderLineReader
This model is used in the same way of the OrderLineItem model but it displays e-Book readers in the Order model
| Field | Field Type | Validation |
| :---- | :--------- | :--------- |
| order | ForeignKey | (related model) Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitemsreader' |
| ebook_reader | ForeignKey | (related model) Ebook_reader, null=False, blank=False, on_delete=models.CASCADE |
| quantity | IntegerField | null=False, blank=False, default=0 |
| lineitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False |


##### Profile App
###### UserProfile
This model builds on the user model provided by Django. 

This model maintain default delivery information and order history
| Field | Field Type | Validation |
| :---- | :--------- | :--------- |
| user | OneToOneField | User, on_delete=models.CASCADE |
| default_phone_number | CharField | max_length=20, blank=True |
| default_street_address1 | CharField | max_length=80, blank=True |
| default_street_address2 | CharField | max_length=80, blank=True |
| default_town_or_city | CharField | max_length=40, blank=True |
| default_county | CharField | max_length=80, blank=True |
| default_postcode | CharField | max_length=20, blank=True |
| default_country | CountryField | blank_label='Country', null=True, blank=True |

---


### Wireframes
The wireframes have been built using the Balsamiq Cloud service.

All wireframes can be found [here](https://github.com/OmarBedawi/my_first_e-store/tree/master/readme_files/wireframes/wireframes.md)  
 
For individual files, please click the desired page:
  * [Homepage](https://github.com/OmarBedawi/my_first_e-store/tree/master/readme_files/wireframes/wireframes_images/1.homepage.png)
  * [Register Page](https://github.com/OmarBedawi/my_first_e-store/tree/master/readme_files/wireframes/wireframes_images/2.register_page.png)
  * [Login Page](https://github.com/OmarBedawi/my_first_e-store/tree/master/readme_files/wireframes/wireframes_images/3.login_page.png)
  * [Ebook Page](https://github.com/OmarBedawi/my_first_e-store/tree/master/readme_files/wireframes/wireframes_images/4.ebook_page.png)
  * [Ebook Detail Page](https://github.com/OmarBedawi/my_first_e-store/tree/master/readme_files/wireframes/wireframes_images/5.ebook_detail_page.png)
  * [Shopping Bag Page](https://github.com/OmarBedawi/my_first_e-store/tree/master/readme_files/wireframes/wireframes_images/6.shopping_bag_page.png)
  * [Checkout Page](https://github.com/OmarBedawi/my_first_e-store/tree/master/readme_files/wireframes/wireframes_images/7.checkout_page.png)
  * [Checkout Success Page](https://github.com/OmarBedawi/my_first_e-store/tree/master/readme_files/wireframes/wireframes_images/8.checkout_success.png)


  Please note that these wireframes may not match the finished product. 
  
  Some elements may be moved or changed based on feedback or styling issues discovered during development.
   

### Design Choices
#### Overview
For the E-Book Store website, the design took inspiration from Boutique Ado (is a Code Institute mini project) and other e-Book websites. 
Looking at [ebooks.com](https://www.ebooks.com/en-nl/), [bookboon.com](http://bookboon.com/), 
[hoepli.it](https://www.hoepli.it/), [feedbooks.com](http://www.feedbooks.com/publicdomain) & the 
[ebooklobby.com](http://www.ebooklobby.com/) websites, I have identified aspects to include (for example structure of the products and their details).

##### Layout
E-Book Store website, compared with the other e-Book websites mentioned above is presenting a much
cleaner and tidier layout, in order to obtain a high UX and is responsive for 
every screen size.

##### Images
The background image of the Homepage is coming from a google research.

The e-Book cover images have been borrowed from the website [ebooks.com](ebooks.com/en-nl/)

The e-Book reader images come from different google researches.

##### Fonts
To keep the website consistent, [Google Fonts Lato](https://fonts.google.com/specimen/Lato)
is used as the main font of the entire E-Book Store website. 

In my opinion it giving a neat and tidy look to the content pages.


##### Colours
The main two colors used for this project are very simple: black and white.

In most of the project is black on white except for the magazine banner that 
is white on black, together with some other few buttons like "Add to Bag", 
"Go to Secure Checkout", "Secure Checkout" and "Complete Order".
These two colors make text easily readable for users, especially when it comes to read the e-Books descriptions. 
They provide a good contrast and a positive UX.

Other colors are used when the flash messages appear:
* Green for Success
* Blue for Information
* Yellow for Warning
* Red for Danger

---

## Features
### Existing Features
* #### Dynamic Search Bar 
    * E-Books can be searched by title and description using the search bar.
    * Dropdown menus allow the user to sort the titles by price, rating, category and alphabetically (highest to lowest and vice versa).
    * Number of results for searches is dynamically displayed on the page, just before the list of e-Books.
    * Not working for e-Book readers because they are not in big quantity.
* #### Dynamic product Cards and Details Page
    * Each e-Book cover or e-Book reader image is contained in a card that features an image of the product, or the 
    stock missing image if no image has been uploaded.
    * Below each card are displayed some of the product's details.
    * The number of cards per row changes dynamically depeninding on screen size, 
    this keeps the page looking uncluttered and prevents the images from becoming too 
    small to understand or comically large.
    * Clicking on the card image will take the user to the detail page, where all the product's details are displayed. 
    * On larger screens the details page is displayed next to each card; 
    on smaller screens, these details are listed below the card.
    * On the detail page users can select the quantities for a max of 99 units, and add the product to the basket.    
* #### Smart Shopping Bag Update input
    * Users can update their product quantities in the shopping bag, or even delete a product from it.
* #### Stripe Payments 
    * Users can checkout and purchase products using the Stripe API.
* #### Smart Checkout Validator
    * User details and basket are validated twice before the stripe API is called to make the payment.
    If there are any issues with the personal and credit/debit card details or basket items the payment can't take 
    place and the page is reloaded showing the user an error message and assuring them the purchase 
    hasn't gone through.
* #### Checkout Redundancy
    * If somehow the user navigate away from the checkout page before the order is submitted 
    to the database then it is created in the webhooks.
* #### Order and Purchase Confirmation/Emails
    * Once a payment is successful the user gets an email confirming the placed order. 
    * Once an order is created the user is redirected to a checkout summary page displaying 
    information about the order.
* #### Account Creation 
    * Users can create an account with E-Book Store website and this automatically creates 
    a UserAccount entry for the User in the database. Users can use the account to 
    view past orders.
* #### User Profile
    * Users can store their details and use them next time a user reaches the Checkout page.
    * User details can be updated from their profile page. This will not affect their 
    user details (username, email, password) and this is outlined under the update details form.
* #### Password Reset 
    * Users can update their password using their email if they have forgotten their current 
    one.
* #### Toast Alerts 
    * Throughout the site Toast alerts are used to give the user feedback, such as 
    when a user logs in, logs out, adds items to a basket, removes/updates 
    basket items, checks out successfully etc.
    * Alerts change colour depending on the type of message used to create them:
    red for error, green for success, blue for information and yellow for warning.
* #### Responsive Basket
    * The basket won't allow users to checkout if their basket is empty.
    * If the basket is empty it offers a link back to the shopping area.
* #### Responsive Fixed Navbar
  * Includes dropdown links to the different categories of e-Books, e-Book readers and profile pages.
  * Logo text disappears on smaller screens, key elements (basket and account dropdown) 
  remain as icons, while less essential links are stored in the mobile dropdown.
* #### Simple Footer
    * Footer remains consistent across the site and includes three social links and a link
    to the creator's github page. All external links create a new tab rather than change the 
    current windows location. 

### Features Left to Implement
* #### Styled Superuser Dashboard 
    * With more time, a nicely styled dashboard would be created for super users.
    Currently it is just the standard Django admin dashboard which is usable but 
    if is fitting with the rest of the site would be better for UX.
* #### Discount for users
    * With more time, I would like to implement a function for discount. At the moment there is only a 
    discount voice displayed between order total and grand total that is fake for now, is only
    showing: "Discount to apply: 0%"
* #### Custom 404 Page 
    * Fairly self explanatory, but this feature wasn't deemed necessary for the site 
    to be deployed.


---
## Technologies Used
### Languages
* [HTML5](https://html.spec.whatwg.org/multipage/) - Used to create the structure of the website.
* [CSS3](https://www.w3.org/Style/CSS/Overview.en.html) - Used to style the website.
* [JavaScript](https://www.javascript.com/) - Used for stripe functionality, as well as Bootstrap & country field functionality and the quantity buttons.
* [Python (v3.8.7)](https://www.python.org/) - Used to handle backend programming within the Django framework.
### Libraries
* [Google Fonts](https://fonts.google.com/) - Used for website fonts [Lato](https://fonts.google.com/specimen/Lato) for the whole website.
* [Font Awesome](https://fontawesome.com/) - This library provided the Icons used across the website.
* [jQuery](https://jquery.com/) - Included with Bootstrap, also used to code various elements such as the stripe functionality.
* [Stripe API Library](https://stripe.com/gb) - Used to handle the payments to send to E-Book Store Website.
### Frameworks
* [Django v3.1.6](https://docs.djangoproject.com/en/3.1/) - Framework used to create the app along with inbuilt templating language.
* [Bootstrap v4.5](https://getbootstrap.com/docs/4.5/getting-started/introduction/) - Framework to add structure & styling to the site, along with
responsive breakpoints and pre-built elements.
### Tools 
* [Balsamiq Cloud](https://balsamiq.cloud/) - Used for creation of wireframes
* [Git](https://git-scm.com/) - Used for version control and tracking changes to the code whilst in development.
* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - Key for finding bugs and testing responsive design.
* [AWS S3](https://aws.amazon.com/s3/) - Used for storing static and media files used across the site.
* [W3 Html validator](https://validator.w3.org/) - Used to test and validate my html code.
* [W3 Css validator](https://jigsaw.w3.org/) - Used to test and validate my css code.
* [JSHint](https://jshint.com/) - Used to validate my Javascript code.
* [Free Formatter](https://www.freeformatter.com/) - Used to format my html, css and javascript code.
* [Heroku](https://www.heroku.com/home) - Used to deploy and host the finished site.
* [Heroku Postgres](https://www.heroku.com/postgres) - Used to serve the database of E-Book Store manages products and user data with.
---

## Testing
See the [testing write up](https://github.com/OmarBedawi/my_first_e-store/tree/master/readme_files/testing/testing.md) for full details on testing.

---
## Deployment

### How to run E-Book Store's code locally:
The E-Book Store app was coded using the GitPod IDE. 
The git repository is stored locally before being pushed to the remote repository online at GitHub.

To run E-Book Store's app locally you will need the following:
    * Python installed on your environment
    * An AWS account
    * A Stripe account
    

#### Setting up the code:

1. Go to: [https://github.com/OmarBedawi/my_first_e-store](https://github.com/OmarBedawi/my_first_e-store)
2. Click the "Code" button next to the "Gitpod" button which will have a dropdown including "Clone with HTTPS",
"Open with GitHub Desktop" & "Download ZIP"
3. To clone the repository using HTTPS, under "Clone with HTTPS", click the copy to clipboard icon. To clone the
repository using an SSH key, including a certificate issued by your organization's SSH certificate authority, click Use SSH, then click the copy to clipboard icon.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to appear.
7. Type git `clone`, and then paste the URL you copied in Step 3 (https://github.com/OmarBedawi/my_first_e-store.git).
8. Install the requirements by typing `pip3 install -r requirements.txt` in your CLI
9. Finally create a superuser using `python3 manage.py create superuser`

#### Creating a database:
1. To use the local version of the database first type `python3 manage.py makemigrations`
2. Then migrate (`python3 manage.py migrate`) the migrations so that your local db.sqlite3
database included with Django is setup.
3. To use the same data as this E-Book Store site, type `python3 manage.py loaddata`
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


#### Running the app
1. If you are using your AWS bucket to serve the static and media files, go to the bucket and create 
a file named `media/`
2. Export all the files in your local environment directory `media`, to the `media/` file in your AWS bucket.
3. You are ready to run the code locally!

### Deploying to Heroku
1. If you have added any new packages which the code requires to run, type `pip3 freeze > requirements.txt`
to creat a requirements file.
2. If you have deleted the Procfile, create a new one containing: `web: gunicorn my_estore.wsgi:application` in your root directory.
3. Create a new app in Heroku, if you want to use Heroku Postgres to serve your database you can do so 
by going to the dashboard *resources*>*add-ons* and attaching the Heroku Postgres database.
    * Please note, you will need to make your migrations and load the data to the new Postgres database as detailed above in 
  the **Creating a database** steps. Ensure the DATABASE_URL variable matches what is in your Heroku App's 
  **Config Vars**
4. Add your environment variables as detailed in the steps for **Adding environment variables** above
to your apps **Config Vars** including this new variable:  
USE_AWS = True
5. Download the Heroku CLI if you haven't already (found under the *Deploy* tab on the dashboard).
6. Login to Heroku using `heroku login`
7. Set up a remote repository connected to your Heroku app: `git remote add heroku <your heroku git URL>`
    * If you're unsure of your Heroku git URL it can be found under *settings* on the dashboard.
8. Finally push your code to the Heroku remote repo after making any change.  
`git add .`   
`git commit -m "some change"`  
`git push heroku master`

The site is now deployed remotely.


### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and choose [my_first_e-store](https://github.com/OmarBedawi/my_first_e-store).
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate and click the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.


### Making a Local Clone

1. Log in to GitHub and locate the [my_first_e-store](https://github.com/OmarBedawi/my_first_e-store)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/OmarBedawi/my_first_e-store
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/OmarBedawi/my_first_e-store
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.


---

## Credits

### Code
* Card, Navbar, Buttons and Form elements adjusted from [Bootstrap 4 examples](https://getbootstrap.com/docs/4.5/getting-started/introduction/).
* [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546) 
is a Code Institute mini project. It was a very helpful tool in setting up the site.
* README stucture borrows heavily from the [Code institute readme example](https://github.com/Code-Institute-Solutions/SampleREADME#)

### Content

-   Most of the content took inspiration from [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546) 


### Media

* All the images used as e-Book cover, have been borrowed by the website [ebooks.com](ebooks.com/en-nl/).
* All the other images are coming from google research.

### Acknowledgements
A massive thank you to my mentor Antonio Rodriguez for his helpful feedbacks.   
Thanks also to the kind people at Tutor Support who went above and beyond to help me fix issues.  

---
