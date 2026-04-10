def adicionar_tarefas(lista_tarefas,nome_tarefa):
<<<<<<< HEAD
=======

#tarefa: vai armazenar o nome da tarefa
#completa: vai indicar se tarefa foi completada
>>>>>>> 24484294be98e6deb988d0f0892b5ad10ec631a5
  tarefa = {"nome": nome_tarefa, "completada":False}
  lista_tarefas.append(tarefa)
  print(f"tarefa {nome_tarefa} foi adicionada com sucesso!")
  return 

<<<<<<< HEAD
def ver_tarefas(lista_tarefas):
  print("\nLista de tarefas:\n")
  
  for indice, tarefa in enumerate(lista_tarefas):
    status = "✓" if tarefa["completada"] else " "
    print(f"{indice}. [{status}] {tarefa['nome']}")

lista_tarefas = []


=======
lista_tarefas = []

>>>>>>> 24484294be98e6deb988d0f0892b5ad10ec631a5
while True:
  print("\n Menu do gerenciador lista de tarefas:")
  print("1. Adicionar tarefa")
  print("2. ver tarefas")
  print("3. Atualizar tarefas")
  print("4. Completar tarefas")
  print("5. Deletar tarefas completadas")
  print("6. Sair")

  escolha = input("Digite a sua escolha:")

  if escolha == "1":
    nome_tarefa = input("Digite o nome da tarefa que deseja adicionar:")
    adicionar_tarefas(lista_tarefas,nome_tarefa)
<<<<<<< HEAD
  elif escolha == "2":
     ver_tarefas(lista_tarefas)
  elif escolha == "6":
    break

print("Programa finalizado")
=======
  elif escolha == "6":
    break

print("Programa finalizado")
>>>>>>> 24484294be98e6deb988d0f0892b5ad10ec631a5
