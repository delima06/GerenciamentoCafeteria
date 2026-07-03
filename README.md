# Gerenciamento de Cafeteria

**Disciplina**: Gestão de Qualidade de Software
**Professora**: Carla da Costa Fernandes Curvelo
**Dupla**: Pedro Davi e Thiago de Lima

Este projeto foi desenvolvido como parte de uma atividade prática de desenvolvimento de software e testes automatizados. O sistema simula o controle simples de pedidos de uma cafeteria, permitindo o cadastro de novos registros e a validação das operações por meio de testes automatizados com Selenium e unittest.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos principais:

*   **src/index.html**: Página principal que contém o formulário de cadastro de pedidos (nome do cliente, produto e quantidade) e a tabela que exibe os pedidos registrados.
*   **src/pagina_secundaria.html**: Página do cardápio do estabelecimento, servindo como destino para demonstrar a navegação interna do sistema.
*   **src/script.js**: Arquivo responsável pela lógica de manipulação do DOM, validação de campos obrigatórios, cadastro de novos pedidos e renderização dinâmica na tabela.
*   **src/style.css**: Folha de estilos para a formatação visual e layout básico das páginas do sistema.
*   **test_sistema.py**: Arquivo contendo a suíte de testes automatizados integrada com Selenium WebDriver em modo headless.

## Requisitos Atendidos

O sistema implementa e atende aos seguintes requisitos da atividade:

1.  Interface contendo pelo menos duas páginas integradas por links de navegação.
2.  Formulário com três campos de entrada (cliente, produto e quantidade).
3.  Validação de obrigatoriedade nos campos com retorno visual de erro.
4.  Feedback de sucesso na operação em cor verde e feedback de erro em cor vermelha.
5.  Listagem em tabela que preserva a quantidade e ordem dos itens cadastrados.

## Execução dos Testes

Os testes cobrem seis cenários específicos de validação:

*   Cadastro de pedido com dados válidos.
*   Bloqueio de envio de pedido com campo obrigatório em branco.
*   Exibição da mensagem de sucesso formatada na tela.
*   Exibição da mensagem de erro adequada em caso de falha.
*   Manutenção da ordem e quantidade de múltiplos itens na tabela.
*   Navegação bidirecional entre as páginas do sistema.

Para executar os testes automatizados, é necessário ter o Python instalado. É possível instalar as dependências do projeto com o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

Execute o comando de testes a partir do diretório raiz:

```bash
python test_sistema.py
```

Durante a execução dos testes, um servidor HTTP local é iniciado automaticamente na porta 8000 para hospedar os arquivos estáticos e possibilitar as validações do Selenium WebDriver.

---

## Relatório de Execução dos Testes Automatizados

Este relatório apresenta os resultados obtidos na execução dos testes automatizados desenvolvidos para o sistema de Gerenciamento de Cafeteria. O objetivo deste documento é comprovar e documentar a qualidade e a cobertura dos testes de acordo com as exigências estabelecidas na atividade prática.

### Resumo dos Resultados

*   **Ferramentas Utilizadas**: Python 3, Unittest e Selenium WebDriver (Google Chrome Headless).
*   **Total de Casos de Teste Planejados**: 6
*   **Total de Casos de Teste Executados**: 6
*   **Casos de Teste com Sucesso**: 6 (100%)
*   **Casos de Teste com Falha**: 0 (0%)
*   **Tempo Total de Execução**: ~9.7 segundos

### Detalhamento dos Cenários de Teste

#### 1. test_operacao_com_sucesso
*   **Objetivo**: Validar a inclusão bem-sucedida de um pedido quando todos os campos obrigatórios estão preenchidos de forma correta.
*   **Ações**: Preenchimento do formulário com dados válidos e clique no botão de envio.
*   **Validação**: Verificação se a linha contendo os dados inseridos foi devidamente adicionada ao elemento de exibição na interface do usuário.
*   **Resultado**: Sucesso.

#### 2. test_campo_obrigatorio_vazio
*   **Objetivo**: Garantir que o sistema impeça o envio do formulário caso o nome do cliente (campo obrigatório) esteja em branco.
*   **Ações**: Deixar o campo do cliente vazio, preencher os demais campos e tentar realizar o envio.
*   **Validação**: Verificação de que nenhum registro novo foi inserido na tabela do sistema.
*   **Resultado**: Sucesso.

#### 3. test_mensagem_sucesso
*   **Objetivo**: Assegurar a exibição adequada do feedback visual de sucesso após uma operação válida.
*   **Ações**: Submeter um formulário totalmente preenchido.
*   **Validação**: Verificação se a mensagem exibida na tela é "Pedido realizado com sucesso!" e se ela possui a estilização de cor correspondente (verde).
*   **Resultado**: Sucesso.

#### 4. test_mensagem_erro
*   **Objetivo**: Assegurar a exibição adequada do feedback visual de erro quando a operação contém dados inválidos ou incompletos.
*   **Ações**: Tentar submeter o formulário mantendo todos os campos vazios.
*   **Validação**: Verificação se a mensagem exibida na tela é "Erro: Todos os campos são obrigatórios!" e se ela possui a estilização de cor correspondente (vermelha).
*   **Resultado**: Sucesso.

#### 5. test_ordem_e_quantidade_itens
*   **Objetivo**: Validar se a quantidade total de itens inseridos está correta e se a ordem cronológica de inclusão é mantida de forma íntegra na tabela de exibição.
*   **Ações**: Inserção consecutiva de dois pedidos distintos.
*   **Validação**: Contagem das linhas geradas na tabela e verificação de que o primeiro pedido inserido precede o segundo na listagem visual.
*   **Resultado**: Sucesso.

#### 6. test_navegacao_entre_paginas
*   **Objetivo**: Confirmar que a navegação do usuário entre as diferentes páginas do sistema ocorre de maneira correta e sem interrupções.
*   **Ações**: Acesso ao link para a página secundária (Cardápio) e retorno à página principal por meio do botão de retorno.
*   **Validação**: Verificação da mudança no título da página (`title`) do navegador em cada uma das etapas do trajeto.
*   **Resultado**: Sucesso.

### Log da Console de Execução

```text
127.0.0.1 - - [03/Jul/2026 14:30:55] "GET /index.html HTTP/1.1" 200 -
127.0.0.1 - - [03/Jul/2026 14:30:55] "GET /style.css HTTP/1.1" 200 -
127.0.0.1 - - [03/Jul/2026 14:30:56] "GET /script.js HTTP/1.1" 200 -
127.0.0.1 - - [03/Jul/2026 14:30:59] "GET /pagina_secundaria.html HTTP/1.1" 200 -
----------------------------------------------------------------------
Ran 6 tests in 9.725s

OK
```

### Conclusão

Todos os testes automatizados foram executados com êxito. O sistema demonstrou robustez quanto à integridade das lógicas de validação de dados exigidas e consistência na renderização de mensagens e dados na tela. O projeto atende plenamente aos critérios de testes de qualidade exigidos pela disciplina.