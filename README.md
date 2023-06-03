# code_challenge
code challenge about company org chart API


# API de Organograma

Este é um projeto de API que gerencia informações de empresas, colaboradores e organogramas. A API permite criar, listar e manipular organogramas, com validações adicionais para garantir a integridade dos dados.

## Tecnologias utilizadas

- Django: framework de desenvolvimento web em Python
- Django REST Framework: biblioteca para construção de APIs RESTful em Django

## Configuração do ambiente

1. Clone o repositório em sua máquina local:

~~~linux

git clone https://github.com/santosgv/code_challenge.git

~~~
2. Instale as dependências do projeto:

~~~linux
pip install -r requirements.txt
~~~

3. Configure as variáveis de ambiente necessárias, como SECRET_KEY e DEBUG no arquivo .env


4. Execute as migrações do banco de dados:

~~~linux
python3 manage.py makemigrations

python3 manage.py migrate
~~~

5. Inicie o servidor de desenvolvimento:

~~~linux
python3 manage.py runserver
~~~

A API estará disponível em http://localhost:8000/

## Endpoints

A API fornece os seguintes endpoints para interação:

### Empresas

- `GET /api/empresas/`: Retorna a lista de empresas cadastradas.
- `POST /api/empresas/`: Cria uma nova empresa.
- `GET /api/empresas/{id}/`: Retorna os detalhes de uma empresa específica.
- `PUT /api/empresas/{id}/`: Atualiza os detalhes de uma empresa específica.
- `DELETE /api/empresas/{id}/`: Remove uma empresa específica.
- `GET /api/{id.empresas}/colaboradores/`: Retorna a lista de colaboradores de uma empresa específica.

### Colaboradores

- `GET /api/colaboradores/`: Retorna a lista de colaboradores cadastrados.
- `POST /api/colaboradores/`: Cria um novo colaborador.
- `GET /api/colaboradores/{id}/`: Retorna os detalhes de um colaborador específico.
- `PUT /api/colaboradores/{id}/`: Atualiza os detalhes de um colaborador específico.
- `DELETE /api/colaboradores/{id}/`: Remove um colaborador específico.


### Organogramas

- `GET /api/organogramas/`: Retorna a lista de organogramas cadastrados.
- `POST /api/organogramas/`: Cria um novo organograma.
- `GET /api/organogramas/{id}/`: Retorna os detalhes de um organograma específico.
- `PUT /api/organogramas/{id}/`: Atualiza os detalhes de um organograma específico.
- `DELETE /api/organogramas/{id}/`: Remove um organograma específico.
- `GET /api/organogramas/{id}/colaboradores/`: Retorna a lista de colaboradores associados a um organograma específico.
- `GET /api/organogramas/{id}/gestores_diretos/`: Retorna os detalhes do gestor direto de um organograma específico.

## Validações adicionais

O código implementa algumas validações adicionais para garantir a integridade dos dados. Aqui estão as principais validações:

1. Ao criar um organograma, é verificado se o gestor e os colaboradores pertencem à mesma empresa.
2. Cada usuário pode ter no máximo 1 gestor
3. Uma pessoa abaixo de um líder na hierarquia não pode ser líder desse líder (não permitir loops)

## Para rodar os Testes

~~~linux
python3 manage.py test
~~~