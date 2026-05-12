#!/usr/bin/bash
# ou #!/bin/bash caso o comando acima não funcione

# instala o poetry
curl -sSL https://install.python-poetry.org | python3 -

# adiciona o poetry ao PATH da sessão atual
export PATH="$HOME/.local/bin:$PATH"


poetry install

# cria o .env na raiz do projeto
cat > .env << EOF
DATABASE_URL=sqlite+aiosqlite:///./dev.db
EOF

# cd src && fastapii #  por algum motivo o script trava aqui

echo "cd src && fastapi dev main.py para executar o projeto"