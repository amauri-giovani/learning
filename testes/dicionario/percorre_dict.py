# def get_value_in_dict(dict_name, key):
#     value = None
#     for k in dict_name.keys():
#         value = dict_name[k].get(key)
#     return value
from pprint import pprint

dict_original = {
    'letras': {
        'b': 'B',
        'c': 'C',
        'd': 'D',
        'vogais': {
            'primeira': {
                'a': 'A',
            },
            'segunda': {
                'e': 'E',
            },
            'terceira': {
                'i': 'I',
            },
            'quarta': {
                'o': 'O',
            },
            'quinta': {
                'u': 'U'
            }
        },
        'sem_valores': {
            'um': '',
            'dois': '',
            'outras_sem_valores': {
                'tres': '',
                'quatro': ''
            }
        }
    },
    'sem_valor': '',
    'lista': ['cinco', 'seis', 'sete'],
    'outras_chaves_sem_valores_e_um_int': {
        'lista_sem_valores': [],
        'tupla_sem_valores': (),
        'string': '',
        'int': 10
    }

}


# pprint(dict_original)

# new_dict = {}

def check_key(dictionary: dict, key: str):
    list_keys = []
    if hasattr(dict_original[key], 'keys'):
        print(f"{key}: {dictionary[key]}")
        # check_key(dictionary[key])
    elif not dictionary[key]:
        # del dictionary[key]
        list_keys.append(key)
    # except AttributeError:
    #     print(f"Chave '{key}' não tem outras chaves")
    #     print(f"{key}: {dictionary[key]}")
    # except KeyError:
    #     print(f"Chave não encontrada: {key}")

for k, v in outras_chaves_sem_valores_e_um_int.items():
    check_key(outras_chaves_sem_valores_e_um_int, k)

pprint(f"dict_original ===> {dict_original}")
# print(new_dict)
# del contatos['Marina']
