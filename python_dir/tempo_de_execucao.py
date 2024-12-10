import timeit

def comp_string(string_new, string_origin):
    for i, c in enumerate(string_origin):
        if string_new[i] != c:
            return False
    return True


def calcula_exec(string):
    #Calcula tempo de execução do código
    print(comp_string(string, "Fred"))
    tempo = timeit.timeit(f"comp_string('{string}', 'Fred')", "from __main__ import comp_string", number=1000000)
    return tempo


# print(comp_string("amauri", "amauri"))
# print(calcula_exec("rossetti"))
print(calcula_exec("Fred"))
