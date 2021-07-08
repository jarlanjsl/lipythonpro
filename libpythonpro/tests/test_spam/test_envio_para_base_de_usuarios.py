from unittest.mock import Mock

import pytest

# from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.modelos import Usuario
from libpythonpro.tests.test_spam.main import EnviadorDeSpam


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Jarlan', email='silvajarlan@gmail.com'),
            Usuario(nome='Vitoria', email='vitoria.lima1994@gmail.com')
        ],
        [
            Usuario(nome='Jarlan', email='silvajarlan@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'silvajarlan@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Jarlan', email='silvajarlan@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'vinicios@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'vinicios@gmail.com',
        'silvajarlan@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
