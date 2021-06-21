import unittest
from unittest.mock import MagicMock
import pytest
from server import init

@pytest.fixture
def scan_port_mock():
    with unittest.mock.patch('server.scan_port', return_value=True) as _mock:
        yield _mock

@pytest.fixture
async def test_app(aiohttp_client):
    app = await init()
    yield await aiohttp_client(app)


async def test_open_ports(test_app, scan_port_mock):
    resp = await test_app.get("/scan/151.101.1.69/79/82")
    assert resp.status == 200
    json = await resp.json()
    assert json == [{"port": 79, "state": "open"}, {"port": 80, "state": "open"}, {"port": 81, "state": "open"}]


async def test_closed_ports(test_app, scan_port_mock):
    scan_port_mock.return_value = False
    resp = await test_app.get("/scan/151.101.1.69/79/82")
    assert resp.status == 200
    json = await resp.json()
    assert json == [{"port": 79, "state": "close"}, {"port": 80, "state": "close"}, {"port": 81, "state": "close"}]


async def test_order_ports(test_app, scan_port_mock):
    resp = await test_app.get("/scan/151.101.1.69/79/76")
    assert resp.status == 400
    text = await resp.text()
    assert text == 'Начальый порт больше чем конечный'

