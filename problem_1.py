def main(cargo, salario):

    if cargo == 'junior':
        aumento = salario * 0.15
    elif cargo == 'senior':
        aumento = salario * 0.34
    elif cargo == 'pleno':
        aumento = salario * 0.26
    else:
        return -1

    return salario + aumento