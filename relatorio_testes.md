# Relatório de Execução dos Testes Automatizados

Este relatório apresenta os resultados obtidos na execução dos testes automatizados desenvolvidos para o sistema de Gerenciamento de Cafeteria. O objetivo deste documento é comprovar e documentar a qualidade e a cobertura dos testes de acordo com as exigências estabelecidas na atividade prática.

## Resumo dos Resultados

*   **Ferramentas Utilizadas**: Python 3, Unittest e Selenium WebDriver (Google Chrome Headless).
*   **Total de Casos de Teste Planejados**: 6
*   **Total de Casos de Teste Executados**: 6
*   **Casos de Teste com Sucesso**: 6 (100%)
*   **Casos de Teste com Falha**: 0 (0%)
*   **Tempo Total de Execução**: ~9.7 segundos

---

## Detalhamento dos Cenários de Teste

### 1. test_operacao_com_sucesso
*   **Objetivo**: Validar a inclusão bem-sucedida de um pedido quando todos os campos obrigatórios estão preenchidos de forma correta.
*   **Ações**: Preenchimento do formulário com dados válidos e clique no botão de envio.
*   **Validação**: Verificação se a linha contendo os dados inseridos foi devidamente adicionada ao elemento de exibição na interface do usuário.
*   **Resultado**: Sucesso.

### 2. test_campo_obrigatorio_vazio
*   **Objetivo**: Garantir que o sistema impeça o envio do formulário caso o nome do cliente (campo obrigatório) esteja em branco.
*   **Ações**: Deixar o campo do cliente vazio, preencher os demais campos e tentar realizar o envio.
*   **Validação**: Verificação de que nenhum registro novo foi inserido na tabela do sistema.
*   **Resultado**: Sucesso.

### 3. test_mensagem_sucesso
*   **Objetivo**: Assegurar a exibição adequada do feedback visual de sucesso após uma operação válida.
*   **Ações**: Submeter um formulário totalmente preenchido.
*   **Validação**: Verificação se a mensagem exibida na tela é "Pedido realizado com sucesso!" e se ela possui a estilização de cor correspondente (verde).
*   **Resultado**: Sucesso.

### 4. test_mensagem_erro
*   **Objetivo**: Assegurar a exibição adequada do feedback visual de erro quando a operação contém dados inválidos ou incompletos.
*   **Ações**: Tentar submeter o formulário mantendo todos os campos vazios.
*   **Validação**: Verificação se a mensagem exibida na tela é "Erro: Todos os campos são obrigatórios!" e se ela possui a estilização de cor correspondente (vermelha).
*   **Resultado**: Sucesso.

### 5. test_ordem_e_quantidade_itens
*   **Objetivo**: Validar se a quantidade total de itens inseridos está correta e se a ordem cronológica de inclusão é mantida de forma íntegra na tabela de exibição.
*   **Ações**: Inserção consecutiva de dois pedidos distintos.
*   **Validação**: Contagem das linhas geradas na tabela e verificação de que o primeiro pedido inserido precede o segundo na listagem visual.
*   **Resultado**: Sucesso.

### 6. test_navegacao_entre_paginas
*   **Objetivo**: Confirmar que a navegação do usuário entre as diferentes páginas do sistema ocorre de maneira correta e sem interrupções.
*   **Ações**: Acesso ao link para a página secundária (Cardápio) e retorno à página principal por meio do botão de retorno.
*   **Validação**: Verificação da mudança no título da página (`title`) do navegador em cada uma das etapas do trajeto.
*   **Resultado**: Sucesso.

---

## Log da Console de Execução

```text
127.0.0.1 - - [03/Jul/2026 14:30:55] "GET /index.html HTTP/1.1" 200 -
127.0.0.1 - - [03/Jul/2026 14:30:55] "GET /style.css HTTP/1.1" 200 -
127.0.0.1 - - [03/Jul/2026 14:30:56] "GET /script.js HTTP/1.1" 200 -
127.0.0.1 - - [03/Jul/2026 14:30:59] "GET /pagina_secundaria.html HTTP/1.1" 200 -
----------------------------------------------------------------------
Ran 6 tests in 9.725s

OK
```

---

## Conclusão

Todos os testes automatizados foram executados com êxito. O sistema demonstrou robustez quanto à integridade das lógicas de validação de dados exigidas e consistência na renderização de mensagens e dados na tela. O projeto atende plenamente aos critérios de testes de qualidade exigidos pela disciplina.
