
from datetime import date

PESEL_LEN = 11
def pesel_checksum (pesel):
    multipliers = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    sum = 0
    for i in range(PESEL_LEN-1):
        sum += (int(pesel[i]) * multipliers[i]) % 10  
    if int(pesel[PESEL_LEN-1]) == ((10 - (sum % 10)) % 10):        
        return True
    else:
        return False

def main():   
    pesel_year = 0
    pesel_month = 0     #first digit of month of birth. Used to determine year of birth.
    pesel_sex = 0
    print ("Podaj mi PESEL a powiem Ci ile masz lat i jakiej jesteś płci.")
    
    while True:
        pesel = input("Wpisz numer PESEL: ")
       
        try: 
            if pesel_checksum (pesel) == True:    
                pesel_year = int(pesel[:2])
                pesel_month = int(pesel[2])
                pesel_sex = int(pesel[9])
                if len(pesel) == PESEL_LEN:
                    break
                else: 
                    print ("PESEL Musi mieć 11 cyfr.")
            else:
                raise ValueError()
        except:
            print ("To nie jest PESEL! Spróbuj jeszcze raz.")  

    if pesel_sex % 2 == 0:
        print ("PESEL wskazuje, że jesteś kobietą,")
    else:
        print ("PESEL wskazuje, że jesteś mężczyzną,")

    century = { 
        0: 1900,
        1: 1900,
        2: 2000,
        3: 2000,
        4: 2100,
        5: 2100,
        6: 2200,
        7: 2200,
        8: 1800,
        9: 1800, 
    }

    age = date.today().year - (century.get(pesel_month) + pesel_year)
    if age >=0:
        print ("a Twój wiek to: " + str(age) )
    else:
        print ("ale jeszcze nie ma Cię jeszcze na świecie.")          

if __name__ == "__main__":
    main()