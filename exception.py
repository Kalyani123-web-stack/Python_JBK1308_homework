#Pune RTO project for license.accept age from user & check if age is less than 18 then
#raise AgeTooLowException & if age is above 75 then raise AgeTooHighException & if age is between 18-75 display welcome to pune RTO portal msg.

class AgeTooLowException(Exception):
   pass

class AgeTooHighException(Exception):
   pass


try:
    age=int(input('enter age:'))
    
    if age<18:
        raise AgeTooLowException 
    elif age>75:
      raise AgeTooHighException 
    else:
     print('welcome to pune RTO')

except AgeTooLowException :
   print('age is too low')

except AgeTooHighException:
   print('age is too high')

except ValueError:
   print('Invalid no.')
