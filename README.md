# freeCodeCamp-Time-Calculator

## Instructions:
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator

## Purpose
```python
add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
  ```

## Preview:
<img src="https://github.com/iVuDang/freeCodeCamp-Time-Calculator/blob/main/time%20preview.png" width=100% height=100%>

## Technologies: 
* Python

## Outcome :white_check_mark: :
| Website | Link | 
| ------------- | ------------- | 
| Replit demo | https://replit.com/@iVuDang/freeCodeCamp-Time-Calculator-v1#main.py | 

<br/>

- - - -

## What I learned:
1. "formattingtype".format(value)

    "{:02d}".format(3)
    03

    02d formats an integer (d) to a field of minimum width 2 (2), with zero-padding on the left (leading 0).

2. When encountering Index Error when using lists, this can commonly be resolved using modulus operator %. 

    If there's 7 items in the list, apply % 7 to the indexing variable, the remainder from our modulus calc used as the index reference will appropriately fit between positions 0 to 6. 


## Citations:
* https://stackoverflow.com/questions/36543804/what-does-02d-mean-in-python 
* 24H to 12H format conversion idea inspired from sfoteini
* "{:02d}".format(value) idea inspired from ZeynebBechiri 


