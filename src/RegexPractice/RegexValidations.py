import re

class RegexValidations: 
    def __init__(self):
        self.phonePatterns = [] 
        self.emailPatterns = []
        
        self.phonePatterns.append(r'\d{2}?\s?(\d{1})?\s?(\d{4})-?(\d{4})')
        self.phonePatterns.append(r'(\(?\d{2}\)?)\s?(\d{1})?\s?(\d{4})-?(\d{4})')
        self.phonePatterns.append(r'(\+?\d{2})?\s?(\(?\d{2}\)?)\s?(\d{1})?\s?(\d{4})-?(\d{4})')
        self.emailPatterns.append(r'([A-Za-z0-9.!#$%&*+/=?^_]+)@([a-z]+).([a-z]+)')

    def matchPhone(self, word: str) -> bool:
        for pattern in self.phonePatterns:
            regex = re.compile(pattern)
            if regex.match(word) != None:
                 return True
        return False
        
    def matchEmail(self, word: str ) -> bool:
        for pattern in self.emailPatterns:
            regex = re.compile(pattern)
            if regex.match(word) != None:
                return True
        return False
