funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melisa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melisa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melisa']

funcionarios = set(funcionarios)
turno_dia = set(turno_dia)
turno_noite = set(turno_noite)
tem_carro = set(tem_carro)

noite_tem_carro = set(turno_noite.intersection(tem_carro))
print(f"\nFuncionários que trabalham no turno da noite e possuem carro: {', '.join(noite_tem_carro)}")

dia_tem_carro = set(turno_dia.intersection(tem_carro))
print(f"\nFuncionários que trabalham no turno do dia e possuem carro: {', '.join(dia_tem_carro)}")

sem_carro = set(funcionarios.difference(tem_carro))
print(f"\nFuncionários que não possuem carro: {', '.join(sem_carro)}\n")