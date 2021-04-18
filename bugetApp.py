class Budget:
    def __init__ (self, a):
        ff = (open("budgetsaves.txt").read()).strip()
        ff = eval(ff)
        b = dict (ff)
        if b[a]:
            self.a = b[a]
            self.dict = b
        else:
            b[a] = 0
            self.a = b[a]
            self.dict = b
        self.budget = a

    def Funds_depo(self):
        c = int(input('How much do you want to deposite?'))
        d = c + int(self.a)
        print (z + ' budget balance is', d)
        self.dict[a] = d
    def Funds_withd(self):
        c = int(input('How much do you want to withdraw?'))
        d = int(self.a) - c
        print (z, 'budget balance is', d)
        self.dict[a] = d
    def balance(self):
        y = 0
        for i in self.dict:
            x = self.dict[i]
            y = x + y
        print ('Total budget is', y)
        print (self.budget, 'budget is', self.a)
    def Funds_trans(self):
        x = input('Transfer from?')
        y = input('Transfer to?')
        z = int(input('How much to transfer'))
        if self.dict[x] > Z:
            xx = self.dict[x] - z
            yy = self.dict[y] + z
            self.dict[x] = xx
            self.dict[y] = yy
            print ('Transaction successful')
        else :
            print ('Cannot tranfer amount')

        
