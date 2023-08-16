/* Acessando o json  */
fetch('clientes.json')
    .then(response => response.json())
    .then(data => {
        /* Tranformando os dados json em paragrafos em html */
        const clienteInfo = document.getElementById('cliente-info');
        clienteInfo.innerHTML = `
            <p><strong>ID:</strong> ${data.id}</p>
            <p><strong>Nome:</strong> ${data.nome}</p>
            <p><strong>Email:</strong> ${data.email}</p>
            <p><strong>Telefone:</strong> ${data.telefone}</p>
        `;
    })
    .catch(error => {
        console.error('Erro ao carregar os dados do cliente:', error);
    });