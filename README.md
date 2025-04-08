# FastAPI structure folders and factory template

## 🧪 Pré-requisitos e configuração do ambiente

Para configurar corretamente o ambiente de desenvolvimento, siga os passos abaixo:

#### 1. Instale o `pipx` (gerenciador de ferramentas Python isoladas)


```bash
python3 -m pip install --user pipx 
pipx ensurepath
```

> Feche e reabra o terminal após executar `pipx ensurepath`.

#### 2. Instale o `poetry` com `pipx`


```bash
pipx install poetry
```

#### 3. Instale o Python 3.12 (caso ainda não tenha)

> Utilize sua ferramenta de gerenciamento de versões preferida, como `pyenv` ou instale manualmente. Exemplo com `pyenv`:


```bash
pyenv install 3.12.2
```

#### 4. Configure o projeto para usar o Python 3.12


```bash
poetry env use 3.12
```

> Certifique-se de que o Python 3.12 esteja disponível no seu PATH.

#### 5. Instale as dependências do projeto

```bash
poetry install
```


# 🔧 Task Automation com Taskipy

Este projeto utiliza [Taskipy](https://github.com/illBeRoy/taskipy) para automatizar tarefas comuns de desenvolvimento, como lint, testes, formatação e execução do servidor.

### 📦 Instalação

O Taskipy já está incluído como dependência de desenvolvimento no `pyproject.toml`. Para instalá-lo:

```bash
poetry install
```
Para ativar o poetry shell
```bash
poetry self add poetry-plugin-shell
```

---

### 📋 Comandos disponíveis

|Tarefa|Comando|Descrição|
|---|---|---|
|`lint`|`poetry run task lint`|Executa verificação de código com `ruff`.|
|`format`|`poetry run task format`|Formata o código com `ruff format`.|
|`pre_format`|`poetry run task pre_format`|Aplica correções automáticas com `ruff check --fix`.|
|`run`|`poetry run task run`|Inicia o servidor FastAPI em modo desenvolvimento.|
|`test`|`poetry run task test`|Executa testes com `pytest`, incluindo cobertura.|
|`pre_test`|`poetry run task pre_test`|Executa lint antes dos testes.|
|`post_test`|`poetry run task post_test`|Gera relatório HTML da cobertura de testes com `coverage html`.|

---

### 💡 Exemplo de uso
#### SEM POETRY SHELL
```bash
 poetry run task format      # Formata seu código 
 poetry run task test        # Roda testes + cobertura 
 poetry run task run         # Sobe o servidor FastAPI
```

#### COM POETRY SHELL
```bash
 task format      # Formata seu código 
 task test        # Roda testes + cobertura 
 task run         # Sobe o servidor FastAPI
```
