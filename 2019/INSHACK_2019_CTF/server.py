from pathlib import Path
from mimetypes import guess_type
from aiohttp import web

ROOT = Path().resolve()
print(ROOT)
PUBLIC = ROOT.joinpath('public')


async def stream_file(request, filepath):
    '''Streams a regular file
    '''
    filepath = PUBLIC.joinpath(filepath).resolve()
    if filepath.is_dir():
        return web.Response(headers={'DT': 'DT_DIR'})
    if not filepath.is_file():
        raise web.HTTPNotFound(headers={'DT': 'DT_UNKNOWN'})
    try:
        filepath.relative_to(ROOT)
    except:
        raise web.HTTPForbidden(reason="You can't go beyond the universe...")
    mime, encoding = guess_type(str(filepath))
    headers = {
        'DT': 'DT_REG',
        'Content-Type': mime or 'application/octet-stream',
        'Content-Length': str(filepath.stat().st_size)
    }
    if encoding:
        headers['Content-Encoding'] = encoding
    resp = web.StreamResponse(headers=headers)
    await resp.prepare(request)
    with filepath.open('rb') as resource:
        while True:
            data = resource.read(4096)
            if not data:
                break
            await resp.write(data)
    return resp


async def handle_403(request):
    '''Stream 403 HTML file
    '''
    return await stream_file(request, '403.html')


async def handle_404(request):
    '''Stream 404 HTML file
    '''
    return await stream_file(request, '404.html')


def create_error_middleware(overrides):
    '''Create an error middleware for aiohttp
    '''
    @web.middleware
    async def error_middleware(request, handler):
        '''Handles specific web exceptions based on overrides
        '''
        try:
            response = await handler(request)
            override = overrides.get(response.status)
            if override:
                return await override(request)
            return response
        except web.HTTPException as ex:
            override = overrides.get(ex.status)
            if override:
                return await override(request)
            raise
    return error_middleware


def setup_error_middlewares(app):
    '''Setup error middleware on given application
    '''
    error_middleware = create_error_middleware({
        403: handle_403,
        404: handle_404
    })
    app.middlewares.append(error_middleware)


async def root(request):
    '''Web server root handler
    '''
    path = request.match_info['path']
    if not path:
        path = 'index.html'
    path = Path(path)
    print(f"client requested: {path}")
    return await stream_file(request, path)


def app():
    app = web.Application()
    setup_error_middlewares(app)
    app.add_routes([web.get(r'/{path:.*}', root)])
    web.run_app(app)


if __name__ == '__main__':
    app()
