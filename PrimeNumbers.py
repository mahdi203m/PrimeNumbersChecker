import os
import requests
import datetime

def project_inputs():
    '''
    this function is the project inputs
    '''
    response = requests.get('http://worldtimeapi.org/api/timezone/Asia/Tehran')
    print(f'The Time Project Started:{response.json()['datetime']}')
    global my_inputs
    my_inputs = []
    for i in range(1,11):
        number = int(input(f'Please Enter Number{i}:'))
        my_inputs.append(number)
    os.system('cls')
    print(my_inputs)

project_inputs()    

def prime_numbers_identifier():
    '''
    this will identify the prime numbers of
    each number that we have
    '''
    global my_inputs,first_prime_numbers
    first_prime_numbers = []
    my_inputs_len = len(my_inputs)
    for g in range(0,my_inputs_len):
        for l in range(1,my_inputs[g]+1):
            if(my_inputs[g] % l == 0):
                match g:
                    case 0:
                        first_prime_numbers.append('one')
                    case 1:
                        first_prime_numbers.append('two')
                    case 2:
                        first_prime_numbers.append('three')
                    case 3:
                        first_prime_numbers.append('four')
                    case 4:
                        first_prime_numbers.append('five')
                    case 5:
                        first_prime_numbers.append('six')
                    case 6:
                        first_prime_numbers.append('seven')
                    case 7:
                        first_prime_numbers.append('eight')
                    case 8:
                        first_prime_numbers.append('nine')
                    case 9:
                        first_prime_numbers.append('ten')
                    case 10:
                        first_prime_numbers.append('eleven')
    print(first_prime_numbers)

prime_numbers_identifier()

def prime_counter():
    '''
    this function will be the counter of prime numbers
    that we have
    '''
    global my_inputs,first_prime_numbers
    my_second_list = []
    my_second_list.append(first_prime_numbers.count('one'))
    my_second_list.append(first_prime_numbers.count('two'))
    my_second_list.append(first_prime_numbers.count('three'))
    my_second_list.append(first_prime_numbers.count('four'))
    my_second_list.append(first_prime_numbers.count('five'))
    my_second_list.append(first_prime_numbers.count('six'))
    my_second_list.append(first_prime_numbers.count('seven'))
    my_second_list.append(first_prime_numbers.count('eight'))
    my_second_list.append(first_prime_numbers.count('nine'))
    my_second_list.append(first_prime_numbers.count('ten'))
    for n in range(0,len(my_second_list)):
        if(max(my_second_list) == my_second_list[n]):
            print(f'THE NUMBER THAT HAS BIGGEST PRIME NUMBERS:{my_inputs[n]}')
    print('Im Happy That You Used My Project')
    print(f'The Time Project Ended:{datetime.datetime.now()}')


prime_counter()
    
