# ObjectRocketDevTest

This is a simple farmer's market app designed to allow the user to:
    1. Add items to cart
    2. View cart
    3. Checkout

Input:
```
{
 'state' : string OPTIONAL,  options are 'blue', 'green', 'yellow', 'red'
 'data'  : array of ints, ex: [1,2,3,4]
}
```

Output:
A recipe recommendation, ex: Red Smoothie 3, Blue Smoothie 1

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

### Test it out (Note: Not set up to actually query elastic search yet)
Run python test script:
`./test.py`
(optional : substitute your own data in the `data` variable in the text.py file)

Command line alternative: (haven't tested, might not work)
`curl -XPOST http://127.0.0.1:5000/recommend_nutrition -d '{"state":"blue","data":[1,2,3]}'`


## Saved Data Structures and Files

* `nutrition_map.json` simple json data that organizes health state and time of day recipes

* `requirements.txt` contains the python modules you need to install

## Python Modules
* `app.py` Run the Flask application.

* `recommend_nutrition.py` Where the "business" logic takes place, main script to organize data processing.

* `other_api.py` Dummy module for a call that mocks getting state information from another API.

* `detect_activity.py` Function that takes smart device data and runs though a series of functions to detect an activity done by a person

* `update_state.py` Dummy module that should eventually take a current state and activity, and return an updated state