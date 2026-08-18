from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nome: Mapped[str]
    preco: Mapped[float]
    estoque: Mapped[int]