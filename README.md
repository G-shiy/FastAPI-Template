# FastAPI structure folders and factory template

## 🔧 Task Automation com Taskipy

Este projeto utiliza [Taskipy](https://github.com/illBeRoy/taskipy) para automatizar tarefas comuns de desenvolvimento, como lint, testes, formatação e execução do servidor.

### 📦 Instalação

O Taskipy já está incluído como dependência de desenvolvimento no `pyproject.toml`. Para instalá-lo:

bash

`poetry install`

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

bash

`poetry run task format      # Formata seu código poetry run task test        # Roda testes + cobertura poetry run task run         # Sobe o servidor FastAPI`
