import pytest

from libpythonpro.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['silvajarlan@gmail.com', 'jarlan.silva@sodine.com.br']
)
def test_remetente(destinatario):
    enviador = Enviador()
    resultado = enviador.enviar(
        destinatario,
        'vitoria.lima1994@gmail.com',
        'Cursos Python Pro',
        'Aula da turma Henrique Bastos',
    )
   assert destinatario in resultado