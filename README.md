# Gerenciamento de Cafeteria

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