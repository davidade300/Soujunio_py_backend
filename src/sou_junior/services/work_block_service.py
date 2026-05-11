from sqlalchemy import Result, Row, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from sou_junior.core.schemas import (
    DiagnosticoResponse,
    WorkBlockCreate,
    WorkBlockResponse,
)
from sou_junior.models.models import WorkBlock


async def criar_registro(db: AsyncSession, data: WorkBlockCreate) -> WorkBlockResponse:
    registro: WorkBlock = WorkBlock(**data.model_dump())
    db.add(registro)
    await db.flush()
    return WorkBlockResponse.model_validate(registro)


async def obter_diagnostico(db: AsyncSession) -> DiagnosticoResponse:
    result: Result = await db.execute(
        select(
            func.avg(WorkBlock.nivel_foco).label("media_foco"),
            func.sum(WorkBlock.tempo_minutos).label("tempo_total"),
        )
    )
    row: Row = result.one()

    # sem registros ainda
    if row.media_foco is None:
        return DiagnosticoResponse(
            media_foco=0.0,
            tempo_total_minutos=0,
            mensagem="Nenhum registro encontrado.",
        )

    media: float = round(float(row.media_foco), 2)
    mensagem: str = _gerar_mensagem(media)

    return DiagnosticoResponse(
        media_foco=media,
        tempo_total_minutos=int(row.tempo_total),
        mensagem=mensagem,
    )


def _gerar_mensagem(media: float) -> str:
    if media < 2:
        return (
            "Muita distração detectada. Tente de forma diferente e remova distrações."
        )
    if media < 3:
        return "Foco abaixo do ideal. Pausas mais longas e menos notificações podem ajudar."
    if media < 4:
        return "Bom ritmo! Pequenos ajustes podem te ajudar a melhorar ."
    if media < 5:
        return "Bom ritmo! Continua"
    return "Você está em uma maratona produtiva de alto nível!"
