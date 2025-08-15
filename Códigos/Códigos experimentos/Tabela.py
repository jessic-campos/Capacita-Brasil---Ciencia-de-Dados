def converter_binario_para_decimal_passo_a_passo(binario_str):
    print(f"{'Etapa':<6} {'Valor Atual':<13} {'Bit Lido':<9} {'Operação':<30} {'Novo Valor':<11}")
    print("-" * 75)

    valor = 0
    for i, bit in enumerate(binario_str):
        bit_int = int(bit)
        operacao = f"({valor} × 2) + {bit_int}"
        novo_valor = valor * 2 + bit_int
        print(f"{i+1:<6} {valor:<13} {bit:<9} {operacao:<30} {novo_valor:<11}")
        valor = novo_valor

    print("\nResultado final em decimal:", valor)

# Exemplo de uso:
binario = "011001100110101"
converter_binario_para_decimal_passo_a_passo(binario)
