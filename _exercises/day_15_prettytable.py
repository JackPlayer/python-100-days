from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["City", "Country"]

table.add_row(["Ottawa", "Canada"])
table.add_row(["Vienna", "Austria"])
table.align = "l"
print(table)
