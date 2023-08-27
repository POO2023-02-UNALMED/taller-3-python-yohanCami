class TV:

    _numTV = 0

    def __init__(self, marca, estado):
        
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None

        self.AumentarTV()

    def setMarca(self, marca):
        self._marca = marca

    def setCanal(self, canal):

        if (canal > 0) and (canal < 121):
            self._canal = canal

    def setPrecio(self, precio):
        self._precio = precio

    def setVolumen(self, volumen):

        if (volumen > -1) and (volumen < 8):
            self._volumen = volumen

    def setControl(self, control):

        self._control = control

    def getMarca(self):
        return self._marca
    
    def getCanal(self):
        return self._canal
    
    def getPrecio(self):
        return self._precio
    
    def getVolumen(self):
        return self._volumen
    
    def getControl(self):
        return self._control

    def turnOn(self):

        self._estado = True
        self._volumen = 1
        self._canal = 1

    def turnOff(self):

        self._estado = False

    def getEstado(self):

        return self._estado
    
    def canalUp(self):

        if(self._estado):

            if not ( self._canal >= 120):

                self._canal += 1

    def canalDown(self):

        if(self._estado):

            if not ( self._canal <= 1):

                self._canal -= 1

    def volumenUp(self):

        if(self._estado):

            if not ( self._volumen >= 7):

                self._volumen += 1

    def volumenUp(self):

        if(self._estado):

            if not ( self._volumen <= 0):

                self._volumen -= 1



    @classmethod

    def getNumTV(cls):
        return cls._numTV
    
    def setNumTV(cls, num):
        cls._numTV = num
    
    def AumentarTV(cls):
        cls._numTV += 1

    