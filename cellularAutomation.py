import time
class RowGenerator:

    def __init__(self,parentRow,rule,loop):
        self.generatedRow = []
        self.grid = []
        self.grid.append(row)
        self.parentRow = parentRow
        self.rule = rule
        self.loop = loop

    def __call__(self):
        self.fillGrid()
        self.printGrid()

    #Returns the rule for a case in a smart way :)
    def fillCell(self,case):
        return rule[case]

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


with open("data.txt", encoding="UTF-8") as data:
    #Reading the data from "data.txt" file
    x = data.read().splitlines()
    
    #Defining variables neccesarry for testing
    row,rule,loop = [],[],0

    #Extracting the initial row
    for char in x[0][::2]:
        row.append(int(char))

    #Extracting the rule
    for char in x[1][::2]:
        rule.append(int(char))

    #extracting the loop
    loop = int(x[2])

    #Testing
    generator = RowGenerator(row,rule,loop)
    generator()
    
