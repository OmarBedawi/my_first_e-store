[back to README.md file](https://github.com/OmarBedawi/my_first_e-store/blob/master/README.md)


# Testing


### Testing User Stories from User Experience (UX) Section


> As a User, I would like simple navigation to the whole site, so I can find exactly what I want without searching through links.

* Users are never more than two clicks away from parts of the site that they are expected to access quickly. 
On smaller devices the categories are 3 clicks away but they are always easily accessible 
from the fixed Navabar.  
Seeing old order summaries does take more clicks to access if you are not logged in but this is not expected to be a key
feature users need to view in a rush.



> As a User, I would like to easily see the informations of the e-Books.

* On all the screen size, the essential informations of every e-Book are displayed below the e-Book cover.
If the user clic on a e-Book cover, he will access a page with all the info plus a description of the product.
On this page users can add items to the shopping bag.



> As a User, I would like to easily see my basket, so I can checkout quickly at any moment.

* Users can always click on their basket which is always in the top right of the screen. As it is a key feature, at smaller 
breakpoints this basket icon remains in place rather then entering the mobile dropdown menu.
In case there are items in the basket, below the bag is always displayed how much the user is spending so far.


> As a User, I would like to easily be able to sort the products in different ways.

* In every page where the e-Books are listed, the user always have the chance to sort the products 
by price, by rating, alphabetically or by category (highest to lowest and vice versa).


> As a User, I would like to easily be able to search for an e-Book, filtering one or more key word

* A user can always search for an e-Book using the search bar that is always available on th etop of the page.
The e-Books can be searched by title and description.
Number of results for searches is dynamically displayed on top ofthe page.



> As a User, I would like to have a profile page, so I can see my past orders and checkout details.

* Logged in users can easily access their "my profile" page under the account dropdown in the navbar. 
This single page displays their default details used at checkout and their past orders. 
Order numbers can be clicked to get a full summary of that particular order.



> As a Returning User, I would like to be able to save my default informations, so I can easily use them for the next purchase.

* On the "my profile" page, users can update their details which will be used next time they checkout. 
If a user updates his details, a confirmation toast appears letting him know the action has occured. 
The page is then reloaded showing the new details. If there is an error then the page still reloads 
but an error message appears informing them there was an issue updating the details.



> As a New User, I would like to be able to create an account, so I can save my details and view my orders.

* New users can quickly create an account from the account dropdown by clicking 'Register'. Once their details
have been filled out and validated they will receive a confirmation email asking them to verify their account.



> As a Returning User, I would like To be able to reset my password, so I can update my password if I forget it.

* Under the login option on the Login page there is a 'forgot password?' option which allows users to update their 
password. A link is sent to their email which they can use to update their password. An info toast appears 
when the email has been sent and a success toast appears once they have completed updating their password.



> As a User, I would like the "purchase event" to be simple, so I can avoid filling out too many inputs.

* Completing a purchase on the site is incredibly easy. After the user has choosen his/her e-Book/s, 
he/she is one click away from accessing the shopping bag (that is always available in the fixed navbar) and two clicks away from the checkout page.
Then in the checkout page the user needs only to fill the fields with his/her personal details (for returning users with a profile already created, 
those fields are automatically filled) and the credit/debit card details.



> As a User, I would like confirmation of my orders, so I can know that my purchase was successfull.

* Once an order has been saved to the database and this has been verified by the webhook handler, a email confirming 
the order is sent out. Checkouts which experience no issues redirect the user to a checkout success page which 
verifies an order is completed (along with the emails).
Logged in users can also check an order by looking at their order history.



> As a User with an account, I would like a list of my past orders, so I can know what e-Books I have purchased.

* A user's "my profile" page displays past orders, sorted by date so they can see all the purchases they have done.



> As a User I want to feel that my personal and payment informations is safe and secure.

* The User is constantly informed by toast messages or/and e-mail confirmation if an user action was successfully
or not.



> As an Owner, I would like simple navigation to the e-Books pages, so I can encourage users to buy e-Books.

* The e-Books page is one of the first links seen on the landing page, along with being the first link after **Home** in the navbar.
On the mobile navbar it is the second link after **Home**.



> As an Owner, I would like lots of links back to the e-Books pages, so I can get users to buy more products.

* There are multiple links to or back to the e-Books pages. There is one on the Homepage (Shop now) and one appear in empty baskets.
After successful checkouts, users are linked back to the e-Books pages, and shopping bag have an option to go back to the e-Books pages or checkout.

After a user successfully adds an e-Book to the basket or logs in, they are redirected to the e-Books page.
These all provide users ample chance to get back to the main shopping page and add more items.



> As an Owner, I would like professional and clean styling, so I can keep the site attractive to users.

* Throughout the site, attention has been paid not to overcrowd pages and keep styling simple and consistent. 
All buttons have the same styling, along with text-links and the font-family, following the same styling.



> As an Owner, I would like login validation, so I can prevent users from creating multiple accounts with the same email.

* By using the AllAuth package, all accounts must have a distinct email and username.



> As an Owner, I would like email verification on accounts, so I can prevent malicious users from easily creating multiple accounts.

* All users have to verify their account via the email they used to create it, otherwise it cannot be accessed.



> As an Owner, I would like details of every e-Book, easily foundable by the user.

* The E-Book page and the E-Book Detail page offers the users a full panoramic of all the details they
need to know about an e-Book.



> As an Owner, I would like items to be kept in a basket, so I can make sure users only have to pay once, encouraging them to purchase more.

* As users navigate through the site, unpaid items are held in a basket which relys on session data to stay up-to-date.
Users can use this basket to add more items, update items quantity and remove items before they have to checkout.



> As an Owner/User, I would like responsive design, so I can easily use the site across multiple devices.

* The site has responsive elements on every page. The homepage hides the logo button on smaller devices. 
The navbar collapses to a mobile dropdown on medium and small devices. 
The e-Book cover cards are displayed in a row of 6 on xl screens, 3 on large screens, 2 on medium and small, and 1 on xs screens.
Shopping Bag, Checkout and Profile pages all shifts to make it easier to view and understand on smaller devices.

Overall, the site has a very responsive design with an aim to make information more digestible (rather than just to make it move).



> As an Owner/User, I would like message styling to be intuitive, so I can quickly understand what the message is trying to convey.

* Toast messages are consistently styled so error messages produce red toast headings, success messages produce green toast headings, 
info messages produce blue toast headings and warning messages produce yellow toast headings.



> As an Owner, I would like to easily be able to add, update and delete e-Books titles from the website.

* The Owner can access the website with a special profile provided by the website creator, called superuser. 
  With this profile the owner can find (available only for him) the "Product Management" page to add new e-Books to the store,
  and for the already existing e-Books in the website, the owner has available the Edit and Delete buttons next to every e-Book.
    
---



### Browser testing
The app was physically tested on the following browsers:
* Google Chrome 
* Mozilla Firefox
* Mi Browser
* Microsoft Edge 
* Samsung Internet Browser   

#### Responsive Design Testing
The responsive design was tested using these physical devices:
* Samsung Galaxy S8 (Google Chrome)
* Samsung Galaxy Tab 4 (Google Chrome, Mozilla Firefox, Samsung Internet Browser)
* RedMi Note 8 (Mi Browser, Google Chrome, Mozilla Firefox)
* Laptop HP 17-ca0133nb (Chrome, Mozilla Firefox)


No major issues were uncovered.

Chrome DevTools was also used to test the design on the following devices:
* RedMi Note 8
* Samsung Galaxy S8
* Samsung Galaxy Tab 4


### Code Validation
* HTML5 code validated using [https://validator.w3.org/](https://validator.w3.org/)
* CSS3 code validated using [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)
    * No issues found
* JS code validated using [https://jshint.com/](https://jshint.com/)
    * 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz). - Not deemed an issue.
    * 'template literal syntax' is only available in ES6 (use 'esversion: 6'). - Not deemed an issue.
* Python code validated using [Extend Class Python Validator](https://extendsclass.com/python-tester.html)
    * Some issues with f-strings as the checker didn't deem them valid Python. These bugs were not considered a problem.



### Known Bugs

During the development proccess many bugs (predictably) arose. 

Here are some of the more interesting examples:

#### Full Name and e-mail address fields are not automatically prefilled when a returning user with profile is about to checkout
The fields of the checkout page contains the details of a user. For a returning user all these fields (except the credit/debit card field)
suppose to be all prefilled when he/she is about to complete another order.


#### When user choose to navigate in a Category page, the options "Category (A-Z)" and "Category (Z-A)" not suppose to be available
"Category (A-Z)" and "Category (Z-A)" not suppose to show up in the "sort by" options if a user is already navigating inside a Category.

#### In the e-Books page, Titles and Authors are not always on the same line
On bigger screen size, in the e-Books page, e-Book titles can be displayed in row of 6, or 3 or 2.
When the title of an e-Book is so long that required to be displayed on multiple lines, can cause 
that the authors line are not vertically aligned with the authors line of the e-Book next to.


#### Misplaced navbar items on smaller screens
On some smaller screens, profile icon and search bar are pushed to the right side of the navbar creating
a little of white space between them and the toggle menu.


