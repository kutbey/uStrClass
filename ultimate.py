class ultimateStr:
    def __init__(self, word: str, lowerLetters: str = None, upperLetters: str = None):
        self.word = word
        if not lowerLetters:
            self.lowerLetters = "abcçdefgğhıijklmnoöprsştuüvyz"
        if not upperLetters:
            self.upperLetters = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

    def make_trans_upper(self) -> dict:
        changeTable = str.maketrans(self.lowerLetters, self.upperLetters)
        return changeTable

    def make_trans_lower(self) -> dict:
        changeTable = str.maketrans(self.upperLetters, self.lowerLetters)
        return changeTable

    def upper(self) -> str:
        return self.word.translate(self.make_trans_upper())

    def lower(self) -> str:
        return self.word.translate(self.make_trans_lower())

    def capitalize(self) -> str:
        return f"{self.lower()[0].translate(self.make_trans_upper())}{self.lower()[1:]}"

    def title(self) -> str:
        firstChrIndex = [x + 1 for x in range(len(self.word)) if
                         self.word[x] in (" ", "\n", ".", "!", "?", ":") and (x + 1 != len(self.word))]
        firstChrIndex.insert(0, 0)
        copyWord = list(self.word)
        for y in firstChrIndex:
            copyWord[y] = copyWord[y].translate(self.make_trans_upper())
        return "".join(copyWord)

    def forSorted(self) -> tuple:
        cleanWords = ""
        for l in self.lower().replace(" ", ""):
            if l in self.lowerLetters:
                cleanWords += l
        letterOrder = {i: self.lowerLetters.index(i) for i in self.lowerLetters}
        sorX = [letterOrder.get(cleanWords[i]) for i in range(len(cleanWords))]  # to use sorted method
        return tuple(sorX)

    def __str__(self):
        return self.word

    def __repr__(self):
        return f"ultimateStr({self.word})"

print(ultimateStr("FAtih Çelik Isparta").upper())
print(ultimateStr("FAtih Çelik Isparta").lower())
print(ultimateStr("FAtih Çelik Isparta").title())
print(ultimateStr("FAtih Çelik Isparta").capitalize())
print(ultimateStr("FAtih Çelik Isparta").forSorted())

# OUTPUTLAR

# FATİH ÇELİK ISPARTA
# fatih çelik ısparta
# FAtih Çelik Isparta
# Fatih çelik ısparta
# (6, 0, 23, 11, 9, 3, 5, 14, 11, 13, 10, 21, 19, 0, 20, 23, 0)