# Log de Performance API

API para registrar e analisar sessões de foco e produtividade.

## Requisitos

- Python 3.14.4
- [Poetry](https://python-poetry.org/docs/#installation)

## Instalação

```bash
git clone https://github.com/davidade300/Soujunio_py_backend
cd sou-junior
poetry install
```

## Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
DATABASE_URL=sqlite+aiosqlite:///./dev.db
```

## Rodando o projeto

```bash
cd src
fastapi dev main.py
```

## Endpoints

### `POST /registro-foco`

Registra uma sessão de trabalho.

**Body:**

```json
{
  "nivel_foco": 4,
  "tempo_minutos": 50,
  "comentario": "Implementei o endpoint de autenticação sem interrupções"
}
```

- `nivel_foco`: inteiro de 1 a 5 (1 = muito distraído, 5 = estado de flow)
- `tempo_minutos`: duração da sessão em minutos
- `comentario`: descrição do que foi feito ou o que causou distração

---

### `GET /diagnostico-produtividade`

Retorna um diagnóstico baseado em todos os registros salvos.

**Response:**

```json
{
  "media_foco": 3.75,
  "tempo_total_minutos": 200,
  "mensagem": "Bom ritmo! Continua."
}
```

## Documentação interativa

Com o servidor rodando, acesse:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Redoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)