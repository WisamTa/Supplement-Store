# Testing
* [Testing User Stories](#testing-user-stories)
* [Manually Testing Functionality](#manually-testing-functionality)
---

### Validator Testing
The website's was tested with following validators:

### HTML Markup Validation Service
*  I used [Html Checker](https://validator.w3.org/) to validate the html files.
The files can be found [here]()

### CSS Validation Service
* I used [CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate the css files.
The files can be found [here]()

### JShint
* I used [JShint](https://jshint.com/) to check the JavaScript files
The files can be found [here]()

### PEP8online
* I used [PEP8online](http://pep8online.com/) to check the files
The files can be found [here]()


* [Back to Table of Content](#table-of-content)

### Testing User Stories
#### User Stories Images
* Can be found [here](https://github.com/WisamTa/Supplement-Store/tree/main/media/readme_images)<br>
* [Products User Stories](https://github.com/WisamTa/Supplement-Store/blob/main/media/readme_images/produc-deatail.PNG)
* [Products User Stories](https://github.com/WisamTa/Supplement-Store/blob/main/media/readme_images/product-added-to-bag.PNG)
* [Products User Stories](https://github.com/WisamTa/Supplement-Store/blob/main/media/readme_images/products.PNG)

#### Navigation
     * All users

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
| Home button    | To redirect to home page | Click the home button | Button navigates to home | Pass |
| Navbar links | Clicking All Products takes user to All Products page | Click All Products | Redirected to All Products page | Pass |
|  | Clicking All Category takes user to the specific category page | Click each category in turn | Redirected to specific category page | Pass |
|   | Click Bag takes user to Bag page | Click Bag | Redirected to Bag page | Pass |
|   | Searching using Search Bar displays the product in the products page | Type vegan | Redirected to Products page with all the vegan vitamins in the store | Pass |
|  | Clicking on the Contact link | Redirects user to the contact page with a conatct form , were the user can query site owner| | Pass |
|  | Clicking on the Faq link | Redirects user to the faq page, were they can find "about us, privacy policy and return policy| | Pass |

#### Navigation
     * Users logged in

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :----: |
|  Navbar links   | Clicking Profile takes user to their profile page | Click Profile | Redirected to Profile Page | Pass |
|  | Click Log Out logs out the user | Click Log Out | User logged out and redirected to Log In | Pass |

     * User not logged in

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- | :-----:|
| Navbar links | Click Log In redirects to log in page | Click Log In | User redirected to Log In Page | Pass |
|  | Click Register redirects to log in page | Click Register | User redirected to Register Page | Pass |

#### Home Page
    * Home

| Feature        | Expected           | Testing  | Result | Pass/Fail |
| ------------- |-------------| -----|  ---------- |:----:|
| Menu | Click on any link | rederecet correct page| User redirected to the correct page | Pass |
| Shopping Options | Clicking Categories | Click immune system vitamins| Redirected to the relevant products in shop | Pass |

