class Secret:

    # Constructor
    def __init__(self, key: int, message: str):
        
        self.key = key
        self.message = message
        self.dict_1 = {}
        self.dict_2 = {}
        self.new_message = ''
    
    # Create dicts => method
    def dictionaries(self):
        
        import string
        
        if self.key == 0:
            return self.message
        
        # Add alphabets and postitions to dicts
        for i, letter in enumerate(string.ascii_lowercase):
            self.dict_1[letter] = i
            self.dict_2[i] = letter
    
        return self.dict_1, self.dict_2
    
    
    # Decrypt message => method
    def encrypt(self):
        
        for i in self.message:
            dict_1, dict_2 = self.dictionaries()
            if i.isalpha():
                index = dict_1.get(i.lower()) + self.key
                if index < 26:
                    i = dict_2.get(index).upper()
                else:
                    index = index - 26
                    i = dict_2.get(index).upper()
                self.new_message += i
            else:
                self.new_message += i
                
        return self.new_message
    

    # Decrypt message => method
    def decrypt(self):
        
        for i in self.message:
            dict_1, dict_2 = self.dictionaries()
            if i.isalpha():
                index = dict_1.get(i.lower()) - self.key
                if index >= 0:
                    i = dict_2.get(index).upper()
                    self.new_message += i
                else:
                    index = 26 + index
                    i = dict_2.get(index).upper()
                    self.new_message += i
            else:
                self.new_message += i
                
        return self.new_message

if __name__ == '__main__':
    message = input('Enter message: ')
    key = int(input('Enter encryption or decryption key: '))
    action = input('Do you want to encrypt(e) or decrypt(d)? ')
    if type(key) != int or type(message) != str or type(action) != str:
        raise Exception ('Key must be of type int and Message must be of type str/object')
    cipher = Secret(key, message)
    if action.lower() == 'encrypt' or action.lower() == 'e':
        print(cipher.encrypt())
    elif action.lower() == 'decrypt' or action.lower() == 'd':
        print(cipher.decrypt())