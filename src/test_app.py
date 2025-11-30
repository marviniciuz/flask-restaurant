import pytest
from app import app, db


@pytest.fixture
def cliente():
    # Configura banco em memória para teste
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()
        yield app.test_client()
        # O banco é limpo automaticamente após o teste


def test_home_page_status(cliente):
    """Testa se a página inicial carrega"""
    resposta = cliente.get('/')
    assert resposta.status_code == 200


def test_criar_restaurante(cliente):
    """Testa se consegue cadastrar um restaurante"""
    resposta = cliente.post('/adicionar', data={
        'nome': 'Teste Burger',
        'tipo_cozinha': 'Fast Food'
    }, follow_redirects=True)

    assert resposta.status_code == 200
    assert b"Teste Burger" in resposta.data
