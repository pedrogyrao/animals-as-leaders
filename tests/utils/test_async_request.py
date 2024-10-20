import pytest
from unittest.mock import AsyncMock, patch
from aiohttp import ClientSession
from src.utils.async_requests import async_request, HttpMethod, MAX_RETRIES

TEST_URL = 'http://test-url.com'


@pytest.mark.asyncio
@patch('aiohttp.ClientSession.get', new_callable=AsyncMock)
async def test_get_request_success(mock_get):
    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.ok = True
    mock_response.json.return_value = {'key': 'value'}
    mock_get.return_value = mock_response

    async with ClientSession() as session:
        result = await async_request(
            HttpMethod.GET, session, TEST_URL, params={'param': 'test'})

    assert result == {'key': 'value'}
    mock_get.assert_called_once_with(TEST_URL, params={'param': 'test'})


@pytest.mark.asyncio
@patch('aiohttp.ClientSession.get', new_callable=AsyncMock)
async def test_get_request_retry(mock_get):
    mock_response_retry = AsyncMock()
    mock_response_retry.status = 500
    mock_response_retry.ok = False

    mock_response_success = AsyncMock()
    mock_response_success.status = 200
    mock_response_success.ok = True
    mock_response_success.json.return_value = {'key': 'value'}

    mock_get.side_effect = [
        mock_response_retry, mock_response_retry, mock_response_success]

    async with ClientSession() as session:
        result = await async_request(
            HttpMethod.GET, session, TEST_URL, params={'param': 'test'})

    assert result == {'key': 'value'}
    assert mock_get.call_count == 3


@pytest.mark.asyncio
@patch('aiohttp.ClientSession.post', new_callable=AsyncMock)
async def test_post_request_failure(mock_post):
    mock_response = AsyncMock()
    mock_response.status = 502
    mock_response.ok = False

    mock_post.return_value = mock_response

    async with ClientSession() as session:
        result = await async_request(
            HttpMethod.POST, session, TEST_URL, json={'data': 'test'})

    assert result is None
    assert mock_post.call_count == MAX_RETRIES


@pytest.mark.asyncio
@patch('aiohttp.ClientSession.get', new_callable=AsyncMock)
async def test_get_request_exception(mock_get):
    mock_get.side_effect = Exception('Test exception')

    async with ClientSession() as session:
        result = await async_request(HttpMethod.GET, session, TEST_URL)

    assert result is None
    mock_get.assert_called_once_with(TEST_URL, params={})
