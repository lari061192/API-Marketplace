from fastapi import FastAPI

app = FastAPI()

# Rota inicial (teste)
@app.get("/")
def raiz():
    return {"mensagem": "Marketplace funcionando!"}

# Lista de produtos (simples, só na memória)
produtos = []

@app.get("/produtos")
def listar_produtos():
    return produtos

@app.post("/produtos")
def criar_produto(nome: str, preco: float):
    produto = {"nome": nome, "preco": preco}
    produtos.append(produto)
    return produto