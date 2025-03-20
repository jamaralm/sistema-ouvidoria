from models import add_user, add_complaint, remove_user, remove_complaint, list_complaints

def main():
    while True:
        print("\nSISTEMA DE OUVIDORIA")
        print("1. Adicionar Usuário")
        print("2. Adicionar Reclamação")
        print("3. Remover Usuário")
        print("4. Remover Reclamação")
        print("5. Listar Reclamações")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            name = input("Nome: ")
            email = input("Email: ")
            password = input("Senha: ")
            add_user(name, email, password)
        
        elif opcao == "2":
            name = input("Título da Reclamação: ")
            description = input("Descrição: ")
            user_id = input("ID do Usuário: ")
            add_complaint(name, description, user_id)
        
        elif opcao == "3":
            user_id = input("ID do Usuário a ser removido: ")
            remove_user(user_id)
        
        elif opcao == "4":
            complaint_id = input("ID da Reclamação a ser removida: ")
            remove_complaint(complaint_id)
        
        elif opcao == "5":
            list_complaints()
        
        elif opcao == "6":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()