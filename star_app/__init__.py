from starlette.applications import Starlette
from starlette.responses import JSONResponse, Response

from . import routes




app = Starlette(debug=True, routes=routes.routes)