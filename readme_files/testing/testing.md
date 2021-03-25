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



> As a User, I would like purchase event to be simple, so I can avoid filling out too many inputs.

* Completing a purchase on the site is incredibly easy. After the user has picked his e-Book/s, 
he is one click away from accessing the shopping bag (that is always available in the fixed navbar) and two clicks away from the checkout page.
Then in the checkout page the user needs only to fill the fields with his personal details (for returning users with a profile already created, 
those fields are automatically filled) and the credit/debit card details.



> As a User, I would like confirmation of my orders, so I can know that my purchase was successfull.

* Once an order has been saved to the database and this has been verified by the webhook handler, a email confirming 
the order is sent out. Checkouts which experience no issues redirect the user to a checkout success page which 
verifies an order is completed (along with the emails).
Logged in users can also check an order by looking at their order history.



> As a User with an account, I would like a list of my past orders, so I can know what e-Books I have purchased.

* A user's "my profile" page displays past orders, sorted by date so they can see all the purchases they have done.



> As an Owner, I would like simple navigation to the e-Books pages, so I can encourage users to buy e-Books.

* The e-Books page is one of the first links seen on the landing page, along with being the first link after **Home** in the navbar.
On the mobile navbar it is the second link after **Home**.



> As an Owner, I would like lots of links back to the e-Books pages, so I can get users to buy more products.

* There are multiple links back to the e-Books pages. There is one on the landing page and one appear in empty baskets.
After successful checkouts, users are linked back to .
After successful checkouts, users are linked back to the e-Books pages and baskets have an option to go back to the e-Books pages or checkout.

After a user successfully adds an e-Book to the basket or logs in, they are redirected to the events page and not the basket page. 
These all provide users ample chance to get back to the e-Books pages and add more items.



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













> As an Owner, I would like order confirmation to work even if a user navigates away from the checkout page whilst processing an order, so I can know users haven't purchased tickets without the database updating.

* If the user navigates away from the checkout page before the order is submitted to the model it is handled by the webhooks instead.
This way users can still recieve the confirmation they'd need and the Order and EventBooking models aren't missing
entries. The webhook handler checks the database for an order with a matching stripe_id to the 
payment intent. If this isn't found after 10 searches then the webhook handler creates the order and sends the confirmation
emails.

> As an Owner, I would like dates where events are fully booked to be unpickable, so I can know that users haven't purchased tickets to events which won't be able to cater for them.

* When users navigate to the book an event page, the date picker is given an array of dates which are unbookable due to the ticket 
limit being reached. The date picker then disables these dates to prevent users from booking them. 

> As an Owner, I would like validation on the date picking input, so I can make sure users don't create bookings using dates which aren't correct.

* To prevent users manually inputting dates, the date input only accepts inputs from the date picker.

> As an Owner, I would like validation on the ticket input, so I can stop users booking too many tickets for events which are nearly full.

* The  date picker input has an event listener. This checks booked events in the database and the user's basket tickets to make sure 
they can't accidentally book more tickets than are avaliable. Fuly booked dates in the database are disabled on the date picker. If the user
has all the tickets for a particular day in their basket, then the input for that date is disabled to prevent them getting
more. If for some reason the ticket amount in the user's basket exceeds the amount avaliable at checkout, this item is rejected and 
removed from the basket before the payment can be processed as an added layer of security against over booking.

> As an Owner/User, I would like responsive design, so I can easily use the site across multiple devices.

* The site has responsive elements on almost every page. The homepage hides the contact button on smaller devices. The navbar
collapses to a mobile dropdown on medium and small devices. The event cards hide extra detail that can be found on 
their individual pages on smaller screens along with reducing how many cards appear on each row. Information on the event details page,
Checkout and Visit page all shifts to make it easier to view on smaller devices. Images are cut from the smallest screens 
for Basket, Order and Booking summaries to make the infomation easier to understand. Overall, the site has a very responsive design 
with an aim to make information more digestible (rather than just to make it move).

> As an Owner/User, I would like message styling to be intuitive (red for alerts, green for success), so I can quickly understand what the message is trying to convey.

* Toast messages are consistently styled so error messages produce red toast headings, success messages produce green toast headings
and info messages produce blue toast headings.
