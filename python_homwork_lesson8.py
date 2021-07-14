c = 'y'
apples = int(input('Amout of apples?'))
cpa = int(input('Cash per apple?'))
Cash = 0
transaction = 0
list2 = list()

def select_a(o):
    add_apples = int(input('How much apples do you want to add?'))
    o = add_apples + o
    return(o)
    
def select_b(o,p,q):
    sell_apples = int(input('How many apples do you want to sell?'))
    while sell_apples > o:
        print('You don\'t have that much apples')
        sell_apples = int(input('How many apples do you want to sell?'))
    o = o - sell_apples
    q = q + p*sell_apples 
    return(o,p,q)
    
def select_c(o):
    sell_price = int(input('What is the new sell price?'))
    o = sell_price
    return(o)


    
    
while c == 'y':
    print('--------------------------')
    print('APPLE STATUS')
    print('Amout of apples:',apples)
    print('Price of each apple:',cpa)
    print('Wallet:',Cash)
    print('Transactions:',transaction)

    print('--------------------------')
    print('Add apples  (a)')
    print('Sell apples  (b)')
    print('Change sell price  (c)')
    print('Show all transactions  (d)')
    print('Stop/Give up2  (e)')
    a = input('')
    print('--------------------------')
    
    if a == 'a':
        apples = (select_a(apples))
    
    elif a == 'b':
        list1 = (select_b(apples,cpa,Cash))
        apples = list1[0]
        cpa = list1[1]
        Cash = list1[2]
        list2.append(list1)
        
        transaction = transaction + 1
        
        
    elif a == 'c':
        cpa = (select_c(cpa))
    
    elif a == 'd':
        print(('Number of apple remaining, Cash per apple, Amount of cash'))
        print(list2)
        
    while a == 'e':
        input_ = input('Are you sure? y/n')
        
        if input_ == 'y':
            print('bye!!')
            a = 'exit_loop'
            c = 'exit_loop'
        
        elif input_ == 'n':
            input_ = 'exit_loop'
            a = 'exit_loop'
        
        elif input_ != 'y' or 'n' or 'exit_loop':
            print('That is not a vaild answer')
    