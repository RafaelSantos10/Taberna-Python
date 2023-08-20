# Taberna Python - Projeto Flask

Bem-vindo ao projeto Taberna Python! Este é um projeto baseado em Flask que cria uma aplicação web simples, que usa SQLite para fazer um CRUD simples. Siga as etapas abaixo para configurar o ambiente e executar o servidor local.

## Pré-requisitos

Certifique-se de ter os seguintes componentes instalados antes de prosseguir:

- Python 3.x
- Virtualenv (recomendado para isolar o ambiente)

## Passos para Configuração

### 1. Clonar o Repositório

Clone o repositório do GitHub para o seu sistema local:

```bash
git clone https://github.com/seu-usuario/taberna-python.git
cd taberna-python
```

### 2. Criar e Ativar o Ambiente Virtual (Opcional, mas Recomendado)

Crie um ambiente virtual para isolar as dependências do projeto. Execute os seguintes comandos no diretório do projeto:

```bash
# Usando o virtualenv
python -m venv venv

# Ativando o ambiente virtual
# No Windows
venv\Scripts\activate
# No macOS e Linux
source venv/bin/activate
```

### 3. Instalar Dependências

Instale as dependências do projeto listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Configurar a Variável de Ambiente SECRET_KEY

Configure a variável de ambiente `SECRET_KEY` com uma senha forte e aleatória. Isso é importante para a segurança da sua aplicação. No ambiente virtual ativado, execute o seguinte comando:

```bash
# No Windows (CMD)
set SECRET_KEY=sua_senha_secreta_aqui

# No macOS e Linux
export SECRET_KEY=sua_senha_secreta_aqui
```

### 5. Iniciar o Servidor

Com todas as configurações feitas, você está pronto para iniciar o servidor local. Certifique-se de estar no diretório raiz do projeto e execute:

```bash
python run.py
```

O servidor Flask será iniciado e você verá uma mensagem indicando o endereço local em que a aplicação está rodando, geralmente em `http://127.0.0.1:5000/`.

## Conclusão

Agora você tem o projeto Taberna Python rodando localmente! Sinta-se à vontade para explorar a aplicação e fazer modificações conforme necessário. Lembre-se de que este é apenas um exemplo de arquivo README e você deve personalizá-lo de acordo com as necessidades do seu projeto. Divirta-se codificando! 🐍🍻
