[back to README.md file](https://github.com/OmarBedawi/my_first_e-store/blob/master/README.md)


# Testing


### Testing User Stories from User Experience (UX) Section


> As a User, I would like simple navigation to the whole site, so I can find exactly what I want without searching through links.

* Users are never more than two clicks away from parts of the site that they are expected to access quickly. 
On smaller devices the categories are 3 clicks away but they are always easily accessible 
from the fixed Navabar.  
Seeing old order summaries does take more clicks to access if you are not logged in but this is not expected to be a key
feature users need to view in a rush.
Lately, in the list of products view, I have added an "Add to Bag" button below every product. 
I did this to don't obligate users to enter the detail page to add a product to the basket.



> As a User, I would like to easily see the product's details.

* On all the screen size, the essential informations of every product are displayed below its image.
If the user clic on a product's image, he will access a page with all the product's details, including the product's description.
On this page users can add items to the shopping bag and decide the quantity (from 1 to 99) using the quantity form.



> As a User, I would like to easily see my basket, so I can checkout quickly at any moment.

* Users can always click on their basket icon which is always on the top right of the screen. As it is a key feature, at smaller 
breakpoints this basket icon remains in place rather then entering the mobile dropdown menu.
In case there are items in the basket, below the bag is always displayed the total price of the items in the shopping bag.


> As a User, I would like to easily be able to sort the products in different ways.

* In every page where e-Books and e-Book readers are listed, the user always have the chance to sort the products 
by price, by rating, alphabetically or by category (highest to lowest and vice versa).


> As a User, I would like to easily be able to search for an e-Book, filtering one or more key word.

* A user can always search for an e-Book using the search bar that is always available on the top of the page.
The e-Books can be searched by title and description.
Number of results for searches is dynamically displayed on top of the page.



> As a User, I would like to have a profile page, so I can see my past orders and checkout details.

* Logged in users can easily access their "my profile" page under the account dropdown in the navbar. 
This single page displays their default details used at checkout and their past orders. 
Order numbers can be clicked to get a full summary of that specific order.



> As a Returning User, I would like to be able to save my default informations, so I can easily use them for the next purchase.

* On the profile page, users can update their details which will be used next time they checkout. 
If a user updates his details, a confirmation toast appears letting him know the action has occured. 
The page is then reloaded showing the new details. If there is an error then the page still reloads 
but an error message appears informing them there was an issue updating the details.



> As a New User, I would like to be able to create a profile, so I can save my details and see my future orders.

* New users can quickly create a profile from the account dropdown by clicking 'Register'. Once their details
have been filled out and validated, they will receive a confirmation email asking them to verify their new profile.



> As a Returning User, I would like to be able to reset my password, so I can update my password if I forget it.

* On the Login page there is a 'forgot password?' option which allows users to update their password. 
* A link is sent to their email which they can use to update their password. An info toast appears 
when the email has been sent, and a success toast appears once they have completed updating their password.



> As a User, I would like the "purchase process" to be simple, so I can avoid filling out too many inputs.

* Completing a purchase on the site is incredibly easy. After the user has choosen the products, 
he is one click away from accessing the shopping bag (that is always available in the fixed navbar) and two clicks away from the checkout page.
Then in the checkout page the user needs only to fill the fields with his personal details (for returning users with a profile already existing, 
those fields are automatically filled) and the credit/debit card details.



> As a User, I would like confirmation of my orders, so I can know that my purchase was successfull.

* Once an order has been saved to the database and this has been verified by the webhook handler, an e-mail confirming 
the order is sent out. Checkouts which experience no issues redirect the user to a checkout success page which 
verifies an order is completed (along with a success toast message and the email).
Logged in users can also check an order by looking at their order history in the profile page.



> As a User with an account, I would like a list of my past orders, so I can know what products I have purchased in the past.

* A user's profile page displays past orders, sorted by date so they can see all the purchases they have done.



> As a User I want to feel that my personal and payment informations are safe and secure.

* The User is constantly informed by toast messages or/and e-mail confirmation if an user action was successfully
or not.



> As an Owner, I would like simple navigation to the product pages, so I can encourage users to buy more.

* The e-Books page is one of the first link seen on the landing page, along with being the first link after **Home** in the navbar
and on the mobile dropdown.



> As an Owner, I would like lots of links back to the e-Books pages, so I can get users to buy more.

* There are multiple links to or back to the e-Books page. There is one on the Homepage (Shop now) and one appears in empty shopping bag.
After successful checkouts, users are linked back to the e-Books page, and shopping bag have an option to go back to the e-Books page or checkout.

After an user successfully adds an e-Book to the basket or logs in, they are redirected to the e-Books page.
All that provide users ample chance to get back to the main shopping page and add more items.



> As an Owner, I would like professional and clean styling, so I can keep the site attractive to users.

* Throughout the site, attention has been paid to not overcrowd pages and keep styling simple and consistent. 
All buttons have the same styling, along with text-links and the font-family, following the same styling.



> As an Owner, I would like login validation, so I can prevent users from creating multiple accounts with the same email.

* By using the AllAuth package, all accounts must have a distinct email and username.



> As an Owner, I would like email verification on accounts, so I can prevent malicious users from easily creating multiple accounts.

* All users have to verify their account via the email they used to create it, otherwise it cannot be accessed.



> As an Owner, I would like details of every product, easily foundable by the user.

* Product and the Product Detail pages offer the users a full panoramic of all the details they
need to know about the product.



> As an Owner, I would like items to be kept in a basket, so I can make sure users only have to pay once, encouraging them to purchase more.

* As users navigate through the site, unpaid items are held in a basket which relys on session data to stay up-to-date.
Users can use the basket to add more items, update items quantity or remove items before they have to checkout.



> As an Owner/User, I would like responsive design, so I can easily use the site across multiple devices.

* The site has responsive elements on every page. The navbar hides the logo button on smaller devices. 
The navbar collapses to a mobile dropdown on medium and small devices. 
The product cards are displayed in a row of 4 on xl screens, 3 on lg screens, 2 on md and sm, and 1 on xs screens.
Shopping Bag, Checkout and Profile pages all shifts to make it easier to view and understand on smaller devices.

Overall, the site has a very responsive design with an aim to make information more digestible (rather than just to make it move).



> As an Owner/User, I would like message styling to be intuitive, so I can quickly understand what the message is trying to convey.

* Toast messages are consistently styled:
  - success messages produce green toast headings
  - info messages produce blue toast headings
  - warning messages produce yellow toast headings
  - error messages produce red toast headings



> As an Owner, I would like to easily be able to add, update and delete products from the website.

* The Owner can access the website with a special profile provided by the website creator, called superuser. 
  With this profile the owner can find (available only for him) the "Product Management" page to add new products to the store.
  For the already existing products in the website, the owner has available the Edit and Delete buttons next to every item.
    
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
* Samsung Galaxy S8 (Google Chrome, Samsung Internet Browser)
* Samsung Galaxy Tab 4 (Google Chrome, Mozilla Firefox, Samsung Internet Browser)
* RedMi Note 8 (Mi Browser, Google Chrome, Mozilla Firefox)
* Laptop HP 17-ca0133nb (Chrome, Mozilla Firefox, Microsoft Edge)


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
    * 'template literal syntax' is only available in ES6 (use 'esversion: 6'). - Not deemed an issue.
* Python code validated using [Extend Class Python Validator](https://extendsclass.com/python-tester.html) and [Pep8](http://pep8online.com/)
    * Some warning with elements "imported but not used". - Not deemed an issue.



### Known Bugs

During the development proccess many bugs (predictably) arose. 

Here are some of the more interesting examples:

> #### Full Name and e-mail address fields are not automatically prefilled when a returning user with profile is about to checkout
* The fields of the checkout page contains the details of a user. For a returning user all these fields (except the credit/debit card field)
suppose to be all prefilled when he/she is about to complete another order.


> #### In the e-Books page, Titles and Authors are not always on the same line
* On bigger screen size, in the e-Books page, e-Book titles can be displayed in row of 4, or 3 or 2.
When the title of an e-Book is so long that required to be displayed on multiple lines, can cause 
that the authors line are not aligned with the authors line of the e-Book next to.


> #### Misplaced navbar icons on smaller screens
* On some smaller screens,  search bar, profile icon and basket icon cannot stay on the same line.
After struggling with padding and margin I have decided to reduce the font-size of the icons on xs screen. 


> #### Struggling with e-Book reader images
* The e-Book images all come from the same website, so I did not have any problem with sizing and pixelation.
At the contrary, the e-Book reader images were much more difficult to find and they all come from different sources.
That means I had a lot of hard time to find the right size for displaying them on the site without to be comically pixelated.
I think I found a compromising size but I believe that some picture are still a little compressed but acceptable.


> #### Issues with displaying total price (e-Book price + e-Book reader price)
* I had issues with adding the e-Book total with the e-Book reader total.
I had a lot of situations where at the checkout I was able to display only one of them.
I solved that letting the e-Book total landing on the order_total field and then doing the sum with the grand_total (where the e-Book readers total lands).
I could do that because the discount for now is fake.


> #### Order confirmation e-mail
* Normally the order confirmation e-mail, arrives few seconds after concluding a successful checkout.
However, it happend in very few cases that the mail took even up to 15 minutes to be delivered.


> #### Some commits seems repeated and not clear
  * I'm aware that some of my commits are maybe not very informative.
That happened when I had issues that were making my site stuck or crush completely without to understand what was the cause. 
That give me some panic time because is like groping in the dark.
I'm aware I have to improve this aspect.

> #### Quantity-form functions not working in the shopping bag
  * The quantity-form suppose to accept numbers between 1 and 99 only. The plus and minus buttons are normally black, but they became grey
when the extremes are reached (minus become grey at 1, plus become grey at 99) as a signal that the user cannot go out of this range.
This is still working properly on xs and sm screen size, but not anymore when the screen size is md, lg or xl.
If a number out of the 1-99 range is manually typed, a django messagge suppose to appear, saying that the action is not allowed. 
This bug happens at every screen size in the shopping bag.

It's a very strange bug because the same quantity-form with the same functions is used in the product detail pages and works perfectly 
with every screen size.
I have asked help to tutor and mentor support but with no success.

 
