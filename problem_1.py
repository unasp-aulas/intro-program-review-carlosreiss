def main(cargo, salario):

    if cargo == 'junior':
        aumento = salario * 0.15
    elif cargo == 'senior':
        aumento = salario * 0.26
    elif cargo == 'pleno':
        aumento = salario * 0.34
    else:
        return -1

    return salario + aumento


# print(main('junior', 1000))