class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        return Cell(self.cells - other.cells)

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, cells_in_row):
        rows = ['*'*cells_in_row for i in range(self.cells//cells_in_row)]
        if self.cells % cells_in_row:
            rows.append('*'*(self.cells % cells_in_row))
        return '\n'.join(rows)


cell1 = Cell(5)
cell2 = Cell(5)
cell3 = Cell(5)

print(cell1.make_order(4))
print(cell2.make_order(5))
print(cell3.make_order(2))

cell4 = (cell1 + cell2) / cell3
print(cell4.make_order(2))