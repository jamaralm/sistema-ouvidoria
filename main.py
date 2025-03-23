from models import add_user, add_complaint, remove_user, remove_complaint, list_complaints, list_user_complaints, mark_as_done

mark_as_done(24)

def main():
    while True:
        print("\nSISTEMA DE OUVIDORIA")
        print("1. Adicionar Reclamação")
        print("2. Remover Reclamação")
        print("3. Listar Reclamações")
        print("4. Listar Reclamacoes de Usuario")
        print('5. Marcar Como Concluido')
        print("6. Sair")

        opcao = input("Escolha uma opção: ")
 
        if opcao == "1":
            name = input("Título da Reclamação: ")
            description = input("Descrição: ")
            user_id = input("ID do Usuário: ")
            if not user_id: #Caso o usuario não especifique o ID, a reclamacao constara como anonima
                user_id = None
            add_complaint(name, description, user_id)
        elif opcao == "2":
            complaint_id = input("ID da Reclamação a ser removida: ")
            remove_complaint(complaint_id)
        
        elif opcao == "3":
            list_complaints()

        elif opcao == "4":
            user_id = int(input("ID do usuario: "))

            list_user_complaints(user_id)
        elif opcao == '5':
            complaint_id = int(input('Digite o id da reclamacao que deseja marcar como concluida: '))
            mark_as_done(complaint_id)

        elif opcao == "6":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()