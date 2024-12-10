from random import randint
import barcode

code_id = str(randint(100000000000, 999999999999))
ean = barcode.get('ean13', code_id)
ean.save(code_id)
