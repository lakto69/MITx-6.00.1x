class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        # self.valid_words = load_words(WORDLIST_FILENAME)
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        self.cifra = dict()
        base = 'abcdefghijklmnopqrstuvwxyz'
        # x = 0
        for x in range(26):
            i = x + shift
            if i > 24:
                i -= 26
            self.cifra[base[x]] = base[i]
            self.cifra[base[x].upper()] = base[i].upper()
            x += 1
        return self.cifra
        # pass #delete this line and replace with your code here


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        texto = ''
        base = 'abcdefghijklmnopqrstuvwxyz'
        self.build_shift_dict(shift)

        # print('mensagem:',self.message_text)
        # print(self.cifra)
        for letra in self.message_text: # COLOCA UM GETTER AQUI!!
            if letra.lower() in base:
                texto += self.cifra[letra]
            else:
                texto += letra

        return texto

a = Message('hello')
# (a.build_shift_dict(0))
print(a.apply_shift(0))