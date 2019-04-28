# Object Rocket Developer Test

This is a simple farmer's market app designed to allow the user to:

    1. Add items to cart
    2. View cart
    3. Checkout

Input:

Text file ("product_input.txt") with the format:

```
       CODE,NAME,PRICE
    1. CH1,Chai,3.11
    2. AP1,Apples,6.00
    3. CF1,Coffee,11.23
    4. MK1,Milk,4.75
    5. OM1,Oatmeal,3.69

```

Output:

When viewing cart
```
+                                                       +
|       CURRENT CART                                    |
+                                                       +
|       CODE    NAME    DISCOUNT        PRICE           |
+       ---     ---     ---             ---             +
|       AP1     Apples                  $6.00           |
|                       APPL            -1.50           |
|                                                       |
|       AP1     Apples                  $6.00           |
|                       APPL            -1.50           |
|                                                       |
|       AP1     Apples                  $6.00           |
|                       APPL            -1.50           |
|                                                       |
|       MK1     Milk                    $4.75           |
|                                                       |
+       ---     ---     ---             ---             +
|       TOTAL:                          $18.25          |
+       ---     ---     ---             ---             +
```

When checking out
```

+                                                       +
|       SALES RECEIPT                                   |
+                                                       +
|       CODE    NAME    DISCOUNT        PRICE           |
+       ---     ---     ---             ---             +
|       AP1     Apples                  $6.00           |
|                       APPL            -1.50           |
|                                                       |
|       AP1     Apples                  $6.00           |
|                       APPL            -1.50           |
|                                                       |
|       AP1     Apples                  $6.00           |
|                       APPL            -1.50           |
|                                                       |
|       MK1     Milk                    $4.75           |
|                                                       |
+       ---     ---     ---             ---             +
|       TOTAL:                          $18.25          |
+       ---     ---     ---             ---             +

Thanks for shopping with us!
```



## Instructions to set up the demo

Download python 3.x from https://www.python.org/downloads/

Create and activate a virtual environment
```
python3 -m venv /path/to/new/virtual/environment
source /path/to/new/virtual/environment/bin/activate
```
Install the requirements
`pip install -r requirements.txt`
Run the app
`./app.py`

### Test it out


## Python Modules
* `main.py` Run the main application with additional helper functions such as:
    
    1. Build_products
    2. Print_menu
    3. Print_commands
    4. Take_command
    5. Request_item_for_cart
    6. Make_cart_item

* `cart_class.py` Cart class file with business logic for:

    1. Adding to cart
    2. Viewing cart
    3. Checking out

* `product_class.py` Product class file with:

    1. Product attributes (code, name, price, etc.)
    2. Set_greatest_discount function
    
        *For a given product that is eligible for multiple discounts, apply a single discount of highest value

* `promotions_class.py` Promotions class file with business logic for determining if a cart is eligible for the following promotions:
    
    1. BOGO
    2. APPL
    3. CHMK
    4. APOM
    

* `test_cases.py` File with test cases that test the functionality of:
    
    1. Product class
    2. Cart class
    3. Promotion class
