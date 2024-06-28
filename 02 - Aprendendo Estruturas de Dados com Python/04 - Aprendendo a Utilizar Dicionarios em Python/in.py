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


# lista_chaves = list(contatos.keys())
# count = lista_chaves.count("teste3@teste3.com");
# index = lista_chaves.index("teste3@teste3.com")
# print(count, index);

resultado = "teste1@teste1.com" in contatos;
print(resultado);

resultado = "teste4@teste4.com" in contatos;
print(resultado);

resultado = "idade" in contatos["teste3@teste3.com"];
print(resultado);

resultado = "telefone" in contatos["teste3@teste3.com"];
print(resultado);