class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self,x):
        if x <= 0:
            raise NonPositiveError()
        elif x > 0:
            super().append(x)


l = PositiveList()
l.append(1)
print (l)



