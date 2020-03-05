import time
class RowGenerator:

    def __init__(self,parentRow,rule,loop):
        self.generatedRow = []
        self.grid = []
        self.grid.append(parentRow)
        self.parentRow = parentRow
        self.rule = rule
        self.loop = loop

    def __call__(self):
        self.fillGrid()
        self.printGrid()

    #Returns the rule for a case in a smart way :)
    def fillCell(self,case):
        return self.rule[case]

    #Generates the row
    def fillRow(self):
        for i in range(len(self.parentRow)):
            if i == 0:
                case = int('0' + str(self.parentRow[i]) + str(self.parentRow[i+1]),2)
                self.generatedRow.append(self.fillCell(case))
            elif i == len(self.parentRow) - 1:
                case = int(str(self.parentRow[i-1]) + str(self.parentRow[i]) + '0',2)
                self.generatedRow.append(self.fillCell(case))
            else:
                case = int(str(self.parentRow[i-1]) + str(self.parentRow[i]) + str(self.parentRow[i+1]),2)
                self.generatedRow.append(self.fillCell(case))
        self.reset()

    #Generates the grid
    def fillGrid(self):
        while(self.loop):
            self.fillRow()
            self.grid.append(self.parentRow)
            self.loop -= 1


    def reset(self):
        self.parentRow = self.generatedRow
        self.generatedRow = []

    def printGrid(self):
        self.beautifyGrid()
        for row in self.grid:
            for val in row:
                print(val, end=" "),
                time.sleep(.005)
            print()
    
    def beautifyGrid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 0:
                    self.grid[i][j] = " "
                else:
                    self.grid[i][j] = "*"

class Test:
    if __name__ == "__main__": 
        with open("data.txt", encoding="UTF-8") as data:
            #Reading the data from "data.txt" file
            readData = data.read().splitlines()
            
            #Defining variables neccesarry for testing
            row,rule,loop = [],[],0

            #Extracting the initial row
            for char in readData[0][::2]:
                row.append(int(char))

            #Extracting the rule
            if(int(readData[1]) < 0 or int(readData[1]) > 255):
                print("rule is not between 0 and 255\n resetting rule to 0")
                readData[1] = '0'
            rule = [int(x) for x in bin(int(readData[1]))[2:]]
            while(len(rule) != 8):
                rule.insert(0,0)
            rule.reverse()

            #extracting the loop
            loop = int(readData[2])

            #Testing
            generator = RowGenerator(row,rule,loop)
            generator()
            
