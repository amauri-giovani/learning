from random import choice
import json

lista = [
    "Albert Einstein",
    "Alexander Graham Bell",
    "Alexander Fleming",
    "Benjamim Banneker",
    "Bartolomeu de Gusmão",
    "Benjamin Franklin",
    "Brian David Josephson",
    "Charles Babbage",
    "Charles Goodyear",
    "Charles Darwin",
    "Carl Sagan",
    "Dmitri Mendeleiev",
    "Douglas Hartree",
    "Dennis Hayes",
    "David Paul Gregg",
    "Enrico Fermi",
    "Ernest Rutherford",
    "Edmund Germer",
    "Frederick McKinley Jones",
    "Ferdinand von Zeppelin",
    "Francis Crick",
    "Friedrich Bergius",
    "Galileu Galilei",
    "Gabriel Fahrenheit",
    "Guglielmo Marconi",
    "Heinrich Gobel",
    "Hedy Lamarr",
    "Heinrich Hertz",
    "Hugo Tetrode",
    "Isaac Newton",
    "Ian Wilmut",
    "Ian Hector Frazer",
    "Ivan Fyodorov",
    "Joahannes Gutenberg",
    "John Deere",
    "Joseph Henry",
    "James Watt",
    "Ken Thompson",
    "Karl Benz",
    "Karl Ferdinand Braun",
    "King Camp Gillette",
    "Louis Pasteur",
    "Leonardo da Vinci",
    "Linus Pauling",
    "Ludwig Boltzmann",
    "Ludwig Elsbett",
    "Michael Faraday",
    "Max Planck",
    "Marie Curie",
    "Nikola Tesla",
    "Nicholas Callan",
    "Nicolau Copérnico",
    "Niels Bohr",
    "Otto Lilienthal",
    "Otis Boykin",
    "Orville Wright",
    "Oswaldo Cruz",
    "Percy Julian",
    "Patricia Era Bath",
    "Pierre Curie",
    "Paul Daimler",
    "Quentin Stafford",
    "Richard Feynman",
    "Rudolf Diesel",
    "Ray Dolby",
    "Roger Apéry",
    "Santos Dumont",
    "Samuel Morse",
    "Steve Jobs",
    "Samuel Colt",
    "Thomas Edison",
    "Tim Berners-Lee",
    "Temple Grandin",
    "Terry Keith Ashwin",
    "Ugo Cerletti",
    "Ub Iwerks",
    "Valerian Abakovsky",
    "Vital BraZil",
    "Vladimir Zworykin",
    "Vasily Zvyozdochkin",
    "Wilhelm Schickard",
    "William Bullock",
    "Wilbur Wright",
    "Willis Carrier",
    "Yuri Nikolaevich Denisyuk",
    "Yves Klein",
    "Yury Lomonosov"
]

lista2 = []

for item in lista:
    nome_completo = item
    nome = item.split()[0]
    sobrenome = item.split(nome)[1].strip()
    email = f"{'.'.join(nome_completo.lower().split())}@teste.amauri.com"
    login = email
    status = choice(["Ativo", "Inativo"])

    novo_item = {
        "nome_completo": nome_completo,
        "nome": nome,
        "sobrenome": sobrenome,
        "email": email,
        "login": login,
        "status": status
    }
    lista2.append(novo_item)

# print(lista2)
lista_json = json.dumps(lista2)

print(lista_json)

with open("inventores_e_cientistas_famosos.json", "w") as f:
    f.write(lista_json)
