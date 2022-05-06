from starlette.applications import Starlette
from starlette.responses import JSONResponse, Response
from starlette.routing import Route


async def homepage(request):
    print(request)
    return JSONResponse({'hello': 'world'})


async def home_response(response: Response):
    return Response(response)


app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/res', home_response),
])