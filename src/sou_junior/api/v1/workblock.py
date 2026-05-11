from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from sou_junior.core.dependencies import get_db
from sou_junior.core.schemas import (
    DiagnosticoResponse,
    WorkBlockCreate,
    WorkBlockResponse,
)
from sou_junior.services.work_block_service import criar_registro, obter_diagnostico

router: APIRouter = APIRouter()


@router.post("/registro-foco", response_model=WorkBlockResponse, status_code=201)
async def registrar_foco(data: WorkBlockCreate, db: AsyncSession = Depends(get_db)):
    return await criar_registro(db, data)


@router.get("/diagnostico-produtividade", response_model=DiagnosticoResponse)
async def diagnostico_produtividade(db: AsyncSession = Depends(get_db)):
    return await obter_diagnostico(db)
