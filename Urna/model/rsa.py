import secrets
from pyprimes import isprime


bits = 1024

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def generate_primes(bits = 100):
    generator = secrets.SystemRandom()
    primes = []

    while len(primes) < 2:
        number = generator.randint(2 ** bits, 2 ** (bits + 1) - 1)
        if isprime(number) and number not in primes:
            primes.append(number)
    return primes

def get_keys():
    primes = generate_primes()

    modulo_publico = primes[0]*primes[1]
    totiente = (primes[0] - 1) * (primes[1] - 1)
    exponente_publico = 65537 
    exponente_privado = modinv(exponente_publico, totiente)
    priv_key = Priv_Key(exponente_privado, modulo_publico, exponente_publico)
    pub_key = Pub_Key(exponente_publico, modulo_publico)
    keys = [priv_key, pub_key]
    return keys

class blinder():
    def __init__(self, public_key):
        self.__r= secrets.SystemRandom().randint(public_key.n/2,public_key.n)
        self.__public_key = public_key
    
    def blind(self, m): 
#        privado
        return (m*pow(self.__r,self.__public_key.e, self.__public_key.n))%self.__public_key.n
    
    def unblind(self, m):
#        publico
        return m*modinv(self.__r, self.__n)
    
class Keys(object):
    def __init__(self, priv, pub):
        self.__public_key = pub
        self.__private_key = priv
        
    def return_public(self):
        return self.__public_key
    
    def return_private(self):
        return self.__private_key
        

class Pub_Key(object):
    def __init__(self, e,n):
        self.__public_exponent = e
        self.__public_modulus = n
    def return_variables(self):
        msg = [self.__public_exponent, self.__public_modulus]
        return msg
    def unblind(self, m):
        generator = secrets.SystemRandom()
        r =  generator.randint(2 ** bits, 2 ** (bits + 1) - 1)
        return m*modinv(r, self.__public_modulus)
    
    def verify(self, sign):
        msg = pow(sign, self.__public_exponent, self.__public_modulus)
        return msg.to_bytes(msg.bit_length(), byteorder='little' )
    
    def encrypt(self, msg):
        tipo = type(msg) 
        if tipo == str:
#            msg = msg.encode('utf-8')
            msg = bytes(msg, 'utf-8')
            msg = int.from_bytes(msg, byteorder='little')
        elif tipo == bytes:
            msg = int(msg)
        en_msg = pow(msg,self.__public_exponent, self.__public_modulus)
        
        return en_msg
    
    
class Priv_Key(object):
    def __init__(self, d, n, e):
        self.__private_exponent = d
        self.__public_modulus = n
        self.__public_exponent = e
        self.test = "hola"
        
    def hola(self):
        return self.__public_exponent
    
    def decrypt(self, en_msg):
        dec_msg = pow(en_msg, self.__private_exponent, self.__public_modulus)
        return  dec_msg.to_bytes(dec_msg.bit_length(), byteorder='little' )
    
    def sign(self, msg):
        tipo = type(msg) 
        if tipo == str:
#            msg = msg.encode('utf-8')
            msg = bytes(msg, 'utf-8')
            msg = int.from_bytes(msg, byteorder='little')
        elif tipo == bytes:
            msg = int(msg)
            
        return pow(msg, self.__private_exponent, self.__public_modulus)
    
    def get_public_key(self):
        return self.__public_exponent, self.__public_modulus
        
