import abc

class Ciphers(abc.ABC):

    @abc.abstractmethod
    def decryptionLogicForLetters(self, letter, key):
        pass

    @abc.abstractmethod
    def decryptCiphertext(self, key, ciphertext):
        pass 

    @abc.abstractmethod
    def getCipherName(self):
        pass
