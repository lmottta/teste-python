# Acompanhe a documentação de testes no postman, foi utilizado ngrok para teste remoto 
https://documenter.getpostman.com/view/26803888/2s93Xu2RYf
```
# magpy-nc

magpy-nc é uma API REST desenvolvida com Flask que gerencia uma coleção de projetos. 
Cada projeto tem um nome e uma lista de pacotes. Cada pacote tem um nome e uma versão.

## Instalação

Para instalar as dependências necessárias para executar este projeto, execute o seguinte comando em seu terminal:

```
pip install flask requests
```

## Uso

Para executar a API localmente, execute o seguinte comando em seu terminal:

```
python app.py
```

Isso iniciará a API na porta 5000. Você pode acessar a API em `http://localhost:5000`.

A API tem as seguintes rotas disponíveis:

### POST /api/projects

Cria um novo projeto.

```json
{
    "name": "titan",
    "packages": [
        {"name": "Django"},
        {"name": "graphene", "version": "2.0"}
    ]
}
```

Onde `name` é o nome do projeto e `packages` é uma lista de pacotes. 
Cada pacote deve ter um `name` e pode opcionalmente ter uma `version`. 
Se nenhuma versão for especificada para um pacote, a API usará a versão mais recente do pacote disponível no PyPI.

Se a solicitação for bem-sucedida, a API retornará uma resposta com o código de status HTTP 201 e os dados do projeto criado no corpo da resposta.

Se algum dos pacotes especificados não existir ou se alguma das versões especificadas for inválida, a API retornará um erro com o código de status HTTP 400.

### GET /api/projects/<project_name>

Recupera os dados de um projeto previamente criado. Substitua `<project_name>` pelo nome do projeto que deseja recuperar.

Se o projeto existir, a API retornará uma resposta com o código de status HTTP 200 e os dados do projeto no corpo da resposta.

Se o projeto não existir, a API retornará um erro com o código de status HTTP 404.

### DELETE /api/projects/<project_name>

Exclui um projeto previamente criado. Substitua `<project_name>` pelo nome do projeto que deseja excluir.

Se o projeto existir, a API excluirá o projeto e retornará uma resposta vazia com o código de status HTTP 204.

Se o projeto não existir, a API retornará um erro com o código de status HTTP 404.
```
```
### Testes
Para executar a rotina de testes para este projeto, execute o seguinte comando em seu terminal:

python -m unittest
Isso executará todos os testes definidos na classe TestApp e informará se algum dos testes falhar. 
Se todos os testes passarem, você verá uma saída semelhante a esta:

.....
----------------------------------------------------------------------
Ran 5 tests in 0.015s

OK
Isso indica que todos os testes passaram com sucesso.

Se algum dos testes falhar, você verá uma saída semelhante a esta:

..F..
======================================================================
FAIL: test_create_project_invalid_package (__main__.TestApp)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_app.py", line 27, in test_create_project_invalid_package
    self.assertEqual(response.status_code, 400)
AssertionError: 201 != 400

----------------------------------------------------------------------
Ran 5 tests in 0.017s

FAILED (failures=1)
Isso indica que um dos testes falhou e fornece informações sobre qual teste falhou e por quê.


```
