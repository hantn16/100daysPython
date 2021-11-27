from prettytable import PrettyTable
x = PrettyTable()
x.add_column("PokemonName", ["Pikachu", "Squirtle", "Charmander"])
x.add_column("Type", ["Electric", "water", "Fire"])
x.align["PokemonName"] = "l"
x.align["Type"] = "r"
print(x)
