class Protected:
    __name = "Security"
    # can't be accessed outisde this class due to opening __ with no closing
    
    def __method(self):
        return self.__name