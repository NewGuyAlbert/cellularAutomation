class Row:

    def __init__(self,parentRow,rule):
        self.generatedRow = []
        self.parentRow = parentRow
        self.rule = rule 

    def fillCell(self,case):
        return rule[case]

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


grid = []

row = [0,1,1,1,0,0,1,1]
rule = [0,1,1,1,1,0,0,0]

enhancedRow = Row(row,rule)

for i in range(2):
    grid.append(enhancedRow.parentRow)
    enhancedRow.fillRow()
    enhancedRow.parentRow=enhancedRow.generatedRow

print(grid)
