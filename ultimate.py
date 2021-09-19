class uStr:
    def __init__(self, word: str, lowerLetters: str | list | tuple = None, upperLetters: str | list | tuple = None):
        self.word = word
        if not lowerLetters and not upperLetters:
            self.lowerLetters = "abcçdefgğhıijklmnoöprsştuüvyz"
            self.upperLetters = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"
        else:
            lo = list(lowerLetters.replace(" ", "").strip())
            up = list(upperLetters.replace(" ", "").strip())
            if len(up) != len(lo):
                raise Exception("The alphabet in different lengths!")
            else:
                self.lowerLetters = "".join(lo)
                self.upperLetters = "".join(up)

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
        firstChrIndex = [x + 1 for x in range(len(self.word)) if self.word[x] in (" ", "\n", ".", "!", "?", ":") \
                         and (x + 1 != len(self.word))]
        firstChrIndex.insert(0, 0)
        lowerCaseList = []
        for x in list(self.word):
            lowerCaseList.append(x.translate(self.make_trans_lower()))

        for y in firstChrIndex:
            lowerCaseList[y] = lowerCaseList[y].translate(self.make_trans_upper())
        return "".join(lowerCaseList)

    def forSorted(self) -> tuple:
        cleanWords = ""
        for l in self.lower().strip().replace(" ", ""):
            if l in self.lowerLetters:
                cleanWords += l
        letterOrder = {i: self.lowerLetters.index(i) for i in self.lowerLetters}
        sorX = [(letterOrder.get(cleanWords[i])) for i in range(len(cleanWords))]  # to use sorted method
        return tuple(sorX)

    def __str__(self):
        return self.word

    def __repr__(self):
        return f"ultimateStr({self.word})"


