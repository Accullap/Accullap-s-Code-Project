class Item:
    def __init__(self,name,price,quantaty,IdNum,Fourniseur):
        self._name = name
        self._price = price
        self._quantaty = quantaty
        self._IdNum = IdNum
        self._Fourniseur = Fourniseur

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def quantaty(self):
        return self._quantaty

    @quantaty.setter
    def quantaty(self, value):
        self._quantaty = value

    @property
    def IdNum(self):
        return self._IdNum

    @IdNum.setter
    def IdNum(self, value):
        self._IdNum = value

    @property
    def Fourniseur(self):
        return self._Fourniseur

    @Fourniseur.setter
    def Fourniseur(self, value):
        self._Fourniseur = value
        
