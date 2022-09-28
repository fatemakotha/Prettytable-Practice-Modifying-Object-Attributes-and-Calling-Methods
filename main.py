import prettytable

from prettytable import PrettyTable #from prettytable import the class Prettytablw
table = PrettyTable() #this creates an empty table


table.add_column("Pokemon Name", ["Celebi", "Pikachu", "Onix"]) #adds Pokemon Name to heading and "Celebi", "Pikachu", "Onix" as items in column
table.add_column("Type", ["Legendary", "Electric", "Rock"]) #adds Type to heading and "Legendary", "Electric", "Rock" as items in column

print(table.align) #prints: {'base_align_value': 'c', 'Pokemon Name': 'c', 'Type': 'c'} which means align is set to c, center
table.align = "l" #Aligns attributes to the left
print(table)