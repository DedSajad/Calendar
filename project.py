def LeapYear (leap):            # Definition of Leap Year
    if leap == 0 :
        return False
    elif leap % 4 == 0 and leap % 100 != 0:
        return True
    elif leap % 100 == 0 and leap % 400 == 0:
        return True
    else:
        return False

class Date:
    MonthList = ("" , "January" , "February" , "March" , "April" , "May" , "June" , "July" , "August" ,
                 "September" , "October" , "November" , "December")
    DaysofMonth = [0 , 31 , 28 , 31 , 30 , 31 , 30, 31 , 31 , 30 , 31 , 30 , 31]
    LeapYearList = [0 , 31 , 29 , 31 , 30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31]
    WeekList = ("Saturday" , "Sunday" , "Monday" , "Tuseday" , "Wednesday" , "Thursday" , "Friday")
    d31 = [1 , 3 , 5 , 7 , 8 , 10 , 12]
    d30 = [4 , 6 , 9 , 11]
    d = 1
    m = 1
    y = 1900
    plus = 0
    convert = 0
    WeekDays = 0
    number = 0
    year = 0
    month = 1
    day = 0
    def date_to_day (self , a , b , c):                                 # Converting to Day
        for i in range (1 , a + 1):
            if LeapYear (i) == True:
                self.convert = self.convert + 1
        self.convert += a * 365
        if LeapYear (a) == True:
            self.convert -= 1
        if LeapYear (a) == True:
            for j in range (0 , b):
                self.convert += self.LeapYearList[j]
        else:
            for j in range (0 , b):
                self.convert = self.convert + self.DaysofMonth[j]

        self.convert += c
        self.WeekDays = self.convert % 7
        return self.convert


    def show1 (self):           # Showing the Date with Numeral Characters
        if self.d < 10:
            print ("0" , end="")
        print (self.d , end="-")
        if self.m < 10:
            print ("0" , end="")
        print (self.m , end="-")
        print (self.y)


    def show2 (self):           # Showing the Date with String Month
        if self.d < 10:
            print ("0" , end="")
        print (self.d , end="-")
        print (self.MonthList[self.m] , self.y , sep= "-")

    def show3 (self):           # Showing the Date with Weekdays and also String Month
        p = self.date_to_day (self.y , self.m , self.d)
        print (self.WeekList[self.WeekDays] , end= ",")
        if self.d < 10:
            print ("0" , end= "")
        print (self.d , end= "-")
        print (self.MonthList[self.m] , self.y , sep= "-")

    def show4 (self):           # Showing the Result of Sum if You Want to Add Days
        if self.y < 10:
            print ("0" , end= "" )
        print (self.y , end= "-" )
        if self.m < 10:
            print ("0" , end= "")
        print (self.m , end= "-")
        if self.d < 10:
            print ("0" , end= "")

        print (self.d , " + " , self.plus , " = " , end= "")
        print (self.year , self.month , self.day , sep="-" )

    def get (self):             
       
        self.y = int (input("Enter Year (1900 - 3000): "))
        while self.y < 1900 or self.y > 3000:

            print ("Invalid Number ; Enter a Number in Range 1900 - 3000")
            self.y = int (input("Enter Year (1900 - 3000): "))

        self.m = int (input ("Enter Month (1 - 12): "))
        while self.m < 1 or self.m > 12:
            print ("Invalid Number ; Enter a Number in Range 1 - 12")
            self.m = int (input("Enter number of month = "))

        if self.m == 2 :

            if self.y % 100 == 0 and self.y % 400 == 0:

                self.d = int (input("Enter Day (1 - 29): "))
                while self.d > 29 or self.d < 1:
                    print("Invalid Number ; Enter a Number in Range 1 - 29")
                    self.d = int (input("Enter Day (1 - 29): "))

            elif self.y % 4 == 0 and self.y % 100 != 0:
                self.d = int (input("Enter Day (1 - 29): "))
                while self.d > 29 or self.d < 1:
                    print ("Invalid Number ; Enter a Number in Range 1 - 29")
                    self.d = int (input("Enter Day (1 - 29): "))

            else:
                self.d = int (input("Enter Day (1 - 28): "))
                while self.d>28 or self.d<1:
                    print ("Invalid Number ; Enter a Number in Range 1 - 28")
                    self.d = int (input("Enter Day (1 - 28): "))

        elif self.m in self.d31:
            self.d = int (input("Enter Day (1 - 31): "))
            while self.d > 31 or self.d < 1:
                print ("Invalid Number ; Enter a Number in Range 1 - 31")
                self.d = int (input("Enter Day (1 - 31): "))

        else:
            self.d = int (input("Emter Day (1 - 30): "))
            while self.d > 30 or self.d < 1:
                print ("Invalid Number ; Enter a Number in Range 1 - 30")
                self.d = int (input("Enter Day (1 - 30): "))
        self.plus = int (input("Enter a Number that You Want to Plus with: "))
        

            
    def get2(self):                                # The Result of Sum Definition
        self.number= self.plus + self.convert
        while self.number >= 365 :
            if LeapYear(self.year) == True:
                self.year += 1
                self.number -= 366
            else:
                self.year += 1
                self.number -= 365

        if LeapYear(self.year) == True:
            for PlusNum in range (1 , len(self.LeapYearList)):
                if self.LeapYearList[PlusNum] < self.number:
                    self.month += 1
                    self.number -= self.LeapYearList[PlusNum]
        else:
            for PlusNum in range (1 , len(self.DaysofMonth)):
                if self.DaysofMonth[PlusNum] < self.number:
                    self.month += 1
                    self.number -= self.DaysofMonth[PlusNum]
                else:
                    break

        self.day += self.number
        if self.day == 0:
            self.day += 1


        #           Main            #


x = Date()
x.get() 
x.show1()
x.show2()
x.show3()
x.get2()
x.show4()
