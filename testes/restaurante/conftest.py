import pytest

from testes.restaurante.restaurante import Restaurante


@pytest.fixture
def restaurante_fila_vazia():
    return Restaurante("Pizzaria X")


@pytest.fixture
def restaurante_com_um_pedido():
    return Restaurante("Pizzaria X", 1)