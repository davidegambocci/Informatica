# Voglio printare tutti i numeri fino a 20
for numero in range(1, 21):  #
    
    # se il numero è divisibile per 3 printo "fizz"
    if numero % 5 == 0:
        print("buzz")
    
    elif numero % 3 == 0:  # elif devo aggiungere una condizione 
        print("fizz")
    
    elif numero % 15 == 0:
        print("fizzbuzz")
 
    else:                  # else si realizza se non si realizzano le precedenti
        print(numero)