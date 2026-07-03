let pedidos = [];

function processarPedido() {
    // Captura os elementos do DOM
    const campoCliente = document.getElementById('cliente');
    const campoProduto = document.getElementById('produto');
    const campoQuantidade = document.getElementById('quantidade');
    const txtMensagem = document.getElementById('mensagem');

    // Limpa mensagens anteriores
    txtMensagem.innerText = "";
    txtMensagem.style.color = "";

    // 1. Validação de Campo Obrigatório
    if (campoCliente.value.trim() === "" || campoProduto.value.trim() === "" || campoQuantidade.value.trim() === "") {
        txtMensagem.innerText = "Erro: Todos os campos são obrigatórios!";
        txtMensagem.style.color = "red";
        return;
    }

    // 2. Operação realizada com sucesso
    const novoPedido = {
        cliente: campoCliente.value,
        produto: campoProduto.value,
        quantidade: campoQuantidade.value
    };

    // Adiciona ao "banco de dados" temporário
    pedidos.push(novoPedido);

    // Exibe mensagem de sucesso
    txtMensagem.innerText = "Pedido realizado com sucesso!";
    txtMensagem.style.color = "green";

    // Limpa os campos do formulário para o próximo input
    campoCliente.value = "";
    campoProduto.value = "";
    campoQuantidade.value = "";

    // 3. Atualiza a tabela na interface
    atualizarTabela();
}

function atualizarTabela() {
    const listaPedidos = document.getElementById('lista-pedidos');

    // Limpa a tabela antes de redesenhar
    listaPedidos.innerHTML = "";

    // Adiciona cada pedido na tabela
    pedidos.forEach(pedido => {
        const linha = `
            <tr>
                <td>${pedido.cliente}</td>
                <td>${pedido.produto}</td>
                <td>${pedido.quantidade}</td>
            </tr>
        `;
        listaPedidos.innerHTML += linha;
    });
}