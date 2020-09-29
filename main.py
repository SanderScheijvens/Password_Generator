import random
import string

def wachtwoord(lengte, nummers, speciaal):
    sample_str = ''.join((random.choice(string.ascii_letters) for i in range(lengte)))
    sample_str += ''.join((random.choice(string.digits) for i in range(nummers)))
    sample_str += ''.join((random.choice(string.punctuation) for i in range(speciaal)))

    sample_list = list(sample_str)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return final_string

if __name__ == "__main__":
    lengte_wachtwoord = input('Hoeveelheid letters: ')
    hoeveel_nummers = input('Hoeveelheid cijfers: ')
    hoeveel_speciaal = input('hoeveelheid speciale charaters: ')

    print("Wachtwoord:", wachtwoord(lengte_wachtwoord, hoeveel_nummers, hoeveel_speciaal))
    print('toppie')
