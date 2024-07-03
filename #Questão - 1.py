#Questão - 1
def main():
 fila_atendimento = []  
    
 while True:
        print("\nOpções:")
        print("1. Adicionar cliente à fila")
        print("2. Atender cliente")
        print("3. Mostrar fila de atendimento")
        print("4. Sair")
        
        opcao = input("Escolha uma opção (1/2/3/4): ")
        
        if opcao == '1':
            cliente = input("Digite o nome do cliente a ser adicionado à fila: ")
            fila_atendimento.append(cliente)
            print(f"Cliente '{cliente}' adicionado à fila.")
        
        elif opcao == '2':
            if fila_atendimento:
                cliente_atendido = fila_atendimento.pop(0)
                print(f"Cliente '{cliente_atendido}' foi atendido e removido da fila.")
            else:
                print("Não há clientes na fila para atender.")
        
        elif opcao == '3':
            if fila_atendimento:
                print("Fila de atendimento:")
                for indice, cliente in enumerate(fila_atendimento, start=1):
                    print(f"{indice}. {cliente}")
            else:
                print("Fila de atendimento está vazia.")
        
        elif opcao == '4':
            print("Encerrando o programa...")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
