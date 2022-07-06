from django.shortcuts import render
from django.http import HttpResponse
import random


class PassGen:

    simple_characters = list('abcdefghijklmnopqrstuvwxyz')
    uppercase_characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('1234567890')
    symbols = list('!#$%&()*+,-./:;<=>?@[\]^_')

    def __init__(self, length, is_uppercase, special_symbols, numbers):
        self.length = length
        self.params = {'is_uppercase': {'value': is_uppercase, 'characters': PassGen.uppercase_characters},
                       'special_symbols': {'value': special_symbols, 'characters': PassGen.symbols},
                       'numbers': {'value': numbers, 'characters': PassGen.numbers},
                       }

    def pass_gen(self):

        characters = PassGen.simple_characters
        password = ''

        for param in self.params.values():
            if param['value']:
                characters.extend(param['characters'])

        for i in range(self.length):
            password += random.choice(characters)

        return password



def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):


    passgen = PassGen(
        length=int(request.GET.get('length')),
        is_uppercase=request.GET.get('uppercase'),
        special_symbols=request.GET.get('symbols'),
        numbers=request.GET.get('numbers')
    )
    generated_password = passgen.pass_gen()
    
    return render(request, 'generator/password.html', {'password': generated_password})

