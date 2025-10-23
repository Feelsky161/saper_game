"""
1-бомба
0- пусто
"""
def create_field(size):
    field=[[0 for j in range(size)] for i in range(size)]
    for i in range(size):
        field.append([])
        for j in range (size):
            field[i].append(0)
    return field

def show_field(size):

if __name__=='__main__':
    for i in field:
        for j in i:
            print(j,end=" ")

if __name__=='__main__':
    field = create_field(4)
    show_field(field)