        ##FOR_LOOP##

    #for loop => This is a loop that is not infinite

##EXAMPLE 1:
name = 'tyreek'
for range in name:
    print('Hello this is an example of a for loop')

#for range in name:
   # print('Hello this is an example of a for loop')
"""
The above for loop is used to iterate the variable name .
The variable name has 6 letters so the range for the loop is going to be 6 thus ,the for loop is going to run 6times.
The reference range or iteration number is based on the length of the variable.
"""

##EXAMPLE 2
integers =[1,2,3,4,5,6]
for _ in range(3):
    """
    The above loop FOR _IN RANGE(3):The key to notice is the underscore.
    Without refering to any variable we will run the code enclosed in the loop according to the number of times 
    the range is specified. 
    """
    integers.append(7)
    """
    Everytime the code is executed the integer 7 is appended to the array integers
    """
    print(integers)



"""
RANGE() This function returns a sequence of numbers ,starting from 0 by default, and increments by 1 (by default),and 
 stops before a specified number.
 """
##EXAMPLE 3

integers =[1,2,3,4,5,6]
for _ in range(3):
    """
    OUTPUT>>>>
    [1, 2, 3, 4, 5, 6, 1]
    [1, 2, 3, 4, 5, 6, 1, 1]
    [1, 2, 3, 4, 5, 6, 1, 1, 1]
    """
    integers.append(+1)
    print(integers)

##EXAMPLE 4
counter = 0
for _ in range(5):
    counter = counter + 1
    """
    The code above is a counter app. counter is defined as = 0 then in the body of the 
    loop counter is redefined as 'counter + 1'.
    DEPENDING ON THE RANGE GIVEN THE OUTPUT OF THIS FUNCTION IS ALWAYS GOING TO BE +1
    OUTPUT >>>>
    1
    2
    3
    4
    5
    6
    7 
    8
    9
    10
    """
    print(counter)


             ####WHILE LOOPS
        #While loops  are used to run a given code infinitely unless stopped.
for _ in range (5):
    """
    this for loop wil act on any code that is below it.
    All the codes below are executed according to the range set in the function. 
    """
    counter = int(input('enter any number.'))
     """
     counter is going to be == the input of the user/admin.Any input from the input()is a string and strings can't be used in arithmetic and logicall operations .
     Due to this we use the int() to convert the input string to an interger and thus any thing to do  wiht counter below is already an interger. 
     """
    while counter < 10:"""This checks to see if the input is less than 10 then the codes below are executed."""
        print(counter)
        counter = counter + 1.
        """
        we have other ways of writing line 88
        COUNTER += 1
        """
        """If the input was 9 then it would be added 1 and outputed 10."""
        print(counter)


work = 'coding'
while work != "run":
    """
    line 19 [while work != "run" ],this means that [while the variable work is not equal to the value/string "run"
    then the code below it will be executed infinitely.
    [!=]....THIS MEANS [NOT EQUAL TO
    """
    print('hello')


numbers = [1,2,3,4]
while number != "":
    """
    The while loop above is an endless while loop that appends to the array numbers the value TYREEK endlessly
    WE MAY CALL THIS AN "ENDLESS APPEND"
    """
    numbers.append("tyreek")
    print(numbers)


#counter code

def sum_list(numbers):
    """
    the function above will take the list that u give  it then it will set the first value as the first value of thelist then takes that value and adds it to the next value in the list and that become the next value for the count.
    :param numbers:
    :return:
    """
    count = 0
    for number in numbers:
        count += number
        print(count)

sum_list([2,1,3,4,5])
