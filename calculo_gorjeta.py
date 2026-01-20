def calculo_gorjeta(valor_conta:float, percentual_gorjeta:float) -> float:
    """
    Calcula o valor da gorjeta com base no valor da conta e no percentual da gorjeta.

    Parâmetros:
    valor_conta (float): O valor total da conta.
    percentual_gorjeta (float): O percentual da gorjeta a ser calculado.

    Retorna:
    float: O valor da gorjeta.
    """

    if valor_conta <= 0 or percentual_gorjeta <= 0:
        raise ValueError("O valor da conta e o percentual da gorjeta devem ser não negativos nem 0.")
    
    if percentual_gorjeta > 100:
        raise ValueError("O percentual da gorjeta não pode ser maior que 100%.")
        
    
    gorjeta = (percentual_gorjeta / 100) * valor_conta
    return gorjeta

def total_conta(valor_conta:float, gorjeta:float) -> float:
    """
    Calcula o valor total da conta incluindo a gorjeta.

    Parâmetros:
    valor_conta (float): O valor total da conta.
    gorjeta (float): O valor da gorjeta.

    Retorna:
    float: O valor total da conta incluindo a gorjeta.
    """

    if valor_conta < 0 or gorjeta < 0:
        raise ValueError("O valor da conta e o valor da gorjeta devem ser não negativos.")
    
    total = valor_conta + gorjeta
    return total