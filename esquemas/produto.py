from pydantic import BaseModel

class ProdutoEntrada(BaseModel):
    nome: str
    preco: float
    estoque: int

class ProdutoResposta(BaseModel):
    id: int
    nome: str
    preco: float
    estoque: int

    class Config:
        from_attributes = True
if __name__ == "__main__":
    p = ProdutoEntrada(nome="Teste", preco=10.5, estoque=100)
    print(p)