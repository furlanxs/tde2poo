from datetime import datetime

class Tarefa:
    def __init__(self, id_tarefa, titulo, descricao):
        self.id = id_tarefa
        self.titulo = titulo
        self.descricao = descricao
        self.status = "Pendente"
        self.data_criacao = datetime.now().strftime("%d/%m/%Y %H:%M")

    def __str__(self):
        return f"[{self.id}] {self.titulo} - {self.status} (Criada em: {self.data_criacao})\nDescrição: {self.descricao}"


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self.proximo_id = 1

    # C - Create (Criar)
    def criar_tarefa(self, titulo, descricao):
        nova_tarefa = Tarefa(self.proximo_id, titulo, descricao)
        self.tarefas.append(nova_tarefa)
        self.proximo_id += 1
        print(f"\nTarefa '{titulo}' criada com sucesso!")

    # R - Read (Ler/Listar)
    def listar_tarefas(self):
        if not self.tarefas:
            print("\nNenhuma tarefa cadastrada.")
            return
        print("\n--- LISTA DE TAREFAS ---")
        for tarefa in self.tarefas:
            print(tarefa)
            print("-" * 30)

    # U - Update (Atualizar status ou dados)
    def atualizar_status(self, id_tarefa):
        for tarefa in self.tarefas:
            if tarefa.id == id_tarefa:
                tarefa.status = "Concluída" if tarefa.status == "Pendente" else "Pendente"
                print(f"\nStatus da tarefa {id_tarefa} atualizado para: {tarefa.status}")
                return
        print("\nTarefa não encontrada.")

    # D - Delete (Excluir)
    def excluir_tarefa(self, id_tarefa):
        for tarefa in self.tarefas:
            if tarefa.id == id_tarefa:
                self.tarefas.remove(tarefa)
                print(f"\nTarefa {id_tarefa} excluída com sucesso!")
                return
        print("\nTarefa não encontrada.")


# --- Menu de Interação (Exemplo de uso) ---
def menu():
    gerenciador = GerenciadorTarefas()
    
    while True:
        print("\n=== GERENCIADOR DE TAREFAS ===")
        print("1. Criar Tarefa")
        print("2. Listar Tarefas")
        print("3. Alternar Status da Tarefa")
        print("4. Excluir Tarefa")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            titulo = input("Título da tarefa: ")
            descricao = input("Descrição da tarefa: ")
            gerenciador.criar_tarefa(titulo, descricao)
        elif opcao == "2":
            gerenciador.listar_tarefas()
        elif opcao == "3":
            try:
                id_tar = int(input("Digite o ID da tarefa para alternar o status: "))
                gerenciador.atualizar_status(id_tar)
            except ValueError:
                print("Por favor, digite um número válido.")
        elif opcao == "4":
            try:
                id_tar = int(input("Digite o ID da tarefa que deseja excluir: "))
                gerenciador.excluir_tarefa(id_tar)
            except ValueError:
                print("Por favor, digite um número válido.")
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()