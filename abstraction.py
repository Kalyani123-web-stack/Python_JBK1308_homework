#I2C design pattern(Interface-Abstract class-Concrete class)
from abc import ABC,abstractmethod
class AmzI(ABC):
    #set of rules in interface
    @abstractmethod
    def logincheck(self,un,pwd):
        pass

    @abstractmethod
    def logout(self):
        pass

    @abstractmethod
    def addtocart(self,item,qty,price):
        pass

    @abstractmethod
    def payment(self):
        pass

#TL
class AmzAbs(AmzI):
    def payment(self):
        total=0
        print('Cart summary')
        for item in self.cart:
            print(f"{item['name']}*{item['qty']}={item['qty']*item['price']}")
            total+=item['qty']*item['price']

        print('Total Amount:',total)
        print('Payment received successfully')

    @abstractmethod
    def mens(self):
        pass

    @abstractmethod
    def womens(self):
        pass

#employee
class Shopping(AmzAbs):
    def __init__(self):
        self.cart=[]
        self.user=None

    def logincheck(self, un, pwd):
        if un=='admin' and pwd=='123':
            self.user=un
            print('Login successful')
        else:
            print('Invalid username and password')

    def logout(self):
        print(f'{self.user} log out')
        self.cart.clear()
        self.user=None

    def addtocart(self, item,qty,price):
        self.cart.append({'name':item,'qty':qty,'price':price})
        print(f'{item} added to cart')

    
    def mens(self):
        print(f'Mens clothes:Tshirt,Jeans')

    def womens(self):
        print(f'Womens clothes:Sari,Kurta')


s1=Shopping()
username=input('enter username:')
pwd=input('enter password:')
s1.logincheck(username,pwd)
s1.mens()
s1.womens()
s1.addtocart('Shoes',1,500)
s1.addtocart('Tshirt',2,500)
s1.payment()

s1.logout()

#output
# enter username:admin
# enter password:123
# Login successful
# Mens clothes:Tshirt,Jeans
# Womens clothes:Sari,Kurta
# Shoes added to cart
# Tshirt added to cart
# Cart summary
# Shoes*1=500
# Tshirt*2=1000
# Total Amount: 1500
# Payment received successfully
# admin log out

        
