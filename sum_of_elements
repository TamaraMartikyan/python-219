def sum_of_elements(numbers,exclude_negative=False):
    if(exclude_negative==False):
       return sum(num for num in numbers if num >=0 )
    else:
        return sum(numbers)

numbers=(input('Enter a list of numbers:'))
numbers=list(map(int,numbers.split()))

en_input=input('Shall we include negative numbers? yes or no ')

if en_input=='yes' :
  result=sum_of_elements(numbers,exclude_negative=True)
else:
    result=sum_of_elements(numbers,exclude_negative=False)

print(f'The result is {result}')




