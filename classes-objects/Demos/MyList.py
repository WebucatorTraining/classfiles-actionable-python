class MyList(list):
    "A subclass of list with additional functionality"
    def prepend(self, obj):
        """prepend obj to list
        
        Keyword arguments:
        obj -- obj to prepend"""
        self.insert(0, obj)