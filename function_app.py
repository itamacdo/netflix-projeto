import azure.functions as func
import json
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# ROTA: LISTAR FILMES
@app.route(route="movies", methods=["GET"])
@app.cosmos_db_input(arg_name="movies", 
                     database_name="NetflixCatalog", 
                     container_name="Movies", 
                     connection_string_setting="CosmosDBConnectionString")
def get_movies(req: func.HttpRequest, movies: func.DocumentList) -> func.HttpResponse:
    logging.info('Listando catálogo de filmes.')
    movie_list = [movie.to_dict() for movie in movies]
    return func.HttpResponse(json.dumps(movie_list), mimetype="application/json", status_code=200)

# ROTA: ADICIONAR FILME
@app.route(route="movies", methods=["POST"])
@app.cosmos_db_output(arg_name="movieOutput", 
                      database_name="NetflixCatalog", 
                      container_name="Movies", 
                      connection_string_setting="CosmosDBConnectionString")
def add_movie(req: func.HttpRequest, movieOutput: func.Out[func.Document]) -> func.HttpResponse:
    try:
        body = req.get_json()
        if not all(k in body for k in ("id", "title", "category")):
            return func.HttpResponse("Erro: Campos 'id', 'title' e 'category' são obrigatórios.", status_code=400)
        
        movieOutput.set(func.Document.from_dict(body))
        return func.HttpResponse(f"Filme '{body['title']}' salvo com sucesso!", status_code=201)
    except Exception as e:
        return func.HttpResponse(f"Erro interno: {str(e)}", status_code=500)