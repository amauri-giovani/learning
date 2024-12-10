from rich.table import Table
from rich.console import Console


console = Console()
table = Table(title='Filmes favoritos')

table.add_column('Nome', justify='left')
table.add_column('Data de lançamento', style='green')
table.add_column('Faturamento', style='blue')

table.add_row('Piratas do Caribe', '2005', '1599999')
table.add_row('Star Wars', '2009', '3412551')
table.add_row('Avatar', '2009', '5655555')
table.add_row('Vingadores', '2020', '20000')

console.print(table)
