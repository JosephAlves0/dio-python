contatos = {
    "teste1@teste1.com": {
        "nome": "Teste1",
        "telefone": "1111-1111"
    },
    "teste2@teste2.com": {
        "nome": "Teste2",
        "telefone": "2222-2222"
    },
    "teste3@teste3.com": {
        "nome": "Teste3",
        "telefone": "3333-3333",
    },
};

resultado = contatos.pop("teste1@teste1.com");
print(resultado);
print(contatos);