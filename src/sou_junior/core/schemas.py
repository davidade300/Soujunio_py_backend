from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class WorkBlockCreate(BaseModel):
    nivel_foco: int = Field(ge=1, le=5)
    tempo_minutos: int = Field(gt=0)
    comentario: str


class WorkBlockResponse(BaseModel):
    id: int
    nivel_foco: int
    tempo_minutos: int
    comentario: str
    criado_em: datetime

    model_config = ConfigDict(from_attributes=True)


class DiagnosticoResponse(BaseModel):
    media_foco: float
    tempo_total_minutos: int
    mensagem: str

    model_config = ConfigDict(from_attributes=True)
