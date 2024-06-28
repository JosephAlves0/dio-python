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

for chave in contatos:
    print(chave, contatos[chave]);


for chave, valor in contatos.items():
    print(chave, valor);