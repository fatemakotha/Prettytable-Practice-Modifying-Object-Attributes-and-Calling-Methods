import prettytable

from prettytable import PrettyTable #from prettytable import the class Prettytablw
table = PrettyTable() #this creates an empty table


table.add_column("Pokemon Name", ["Celebi", "Pikachu", "Onix"]) #adds Pokemon Name to heading and "Celebi", "Pikachu", "Onix" as items in column
table.add_column("Type", "ggg")
print(table)