from typing import List

from fastapi import FastAPI, Form, HTTPException, Query

app = FastAPI()

pecas = []  # Lista de peças
carros = []  # Lista de carros

@app.get("/carros")
async def listar_carros():
    """
    Retorna a lista de carros cadastrados.
    """
    return {
        "status": "success",
        "message": "Carros recuperados com sucesso.",
        "data": carros
    }

@app.post("/carros")
async def criar_carro(
    nome: str = Form(...),
    modelo: str = Form(...)
):
    """
    Adiciona um novo carro à lista.
    """
    carro = {
        "id": len(carros) + 1,  # Gera um ID simples
        "nome": nome,
        "modelo": modelo
    }
    carros.append(carro)
    return {
        "status": "success",
        "message": "Carro adicionado com sucesso.",
        "data": carro
    }

@app.get("/pecas")
async def listar_pecas():
    """
    Retorna a lista de peças cadastradas.
    """
    return {
        "status": "success",
        "message": "Peças recuperadas com sucesso.",
        "data": pecas
    }

@app.get("/pecas/{peca_id}")
async def buscar_peca_por_id(peca_id: int):
    """
    Recupera uma peça pelo ID.
    """
    for peca in pecas:
        if peca["id"] == peca_id:
            return {
                "status": "success",
                "message": "Peça recuperada com sucesso.",
                "data": peca
            }
    raise HTTPException(status_code=404, detail="Peça não encontrada.")

@app.post("/pecas")
async def criar_peca(
    nome: str = Form(...),
    descricao: str = Form(...),
    preco: float = Form(...),
    carro_id: int = Form(...)
):
    """
    Adiciona uma nova peça à lista.
    """
    # Verifica se o carro existe
    carro = next((carro for carro in carros if carro["id"] == carro_id), None)
    if not carro:
        raise HTTPException(status_code=404, detail="Carro associado não encontrado.")

    peca = {
        "id": len(pecas) + 1,
        "nome": nome,
        "descricao": descricao,
        "preco": preco,
        "carro": carro
    }
    pecas.append(peca)
    return {
        "status": "success",
        "message": "Peça adicionada com sucesso.",
        "data": peca
    }

@app.put("/pecas/{peca_id}")
async def atualizar_peca(
    peca_id: int,
    nome: str = Form(...),
    descricao: str = Form(...),
    preco: float = Form(...),
    carro_id: int = Form(...)
):
    """
    Atualiza os detalhes de uma peça pelo ID.
    """
    for peca in pecas:
        if peca["id"] == peca_id:
            # Verifica se o carro associado existe
            carro = next((carro for carro in carros if carro["id"] == carro_id), None)
            if not carro:
                raise HTTPException(status_code=404, detail="Carro associado não encontrado.")
            
            peca.update({"nome": nome, "descricao": descricao, "preco": preco, "carro": carro})
            return {
                "status": "success",
                "message": "Peça atualizada com sucesso.",
                "data": peca
            }
    raise HTTPException(status_code=404, detail="Peça não encontrada.")

@app.delete("/pecas/{peca_id}")
async def deletar_peca(peca_id: int):
    """
    Remove uma peça pelo ID.
    """
    for index, peca in enumerate(pecas):
        if peca["id"] == peca_id:
            deletada = pecas.pop(index)
            return {
                "status": "success",
                "message": "Peça removida com sucesso.",
                "data": deletada
            }
    raise HTTPException(status_code=404, detail="Peça não encontrada.")
