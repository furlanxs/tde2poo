# Sistema de Gerenciamento de Tarefas (TDE 2 - POO)

## Descrição do Projeto
Este é um sistema em linha de comando desenvolvido em Python para aplicar conceitos iniciais de Programação Orientada a Objetos (POO). O objetivo principal é gerenciar tarefas diárias permitindo operações completas de CRUD (Create, Read, Update, Delete) em memória.

## Estrutura do Código
O sistema foi estruturado utilizando duas classes principais:
*   **Classe `Tarefa`**: Representa a entidade da tarefa, contendo os atributos `id`, `titulo`, `descricao`, `status` (iniciado como Pendente) e `data_criacao`.
*   **Classe `GerenciadorTarefas`**: Responsável por manipular a lista que armazena as tarefas, contendo os métodos para criar, listar, atualizar o status e deletar os objetos.

## Exemplo de Uso
Ao rodar o script `gerenciador.py`, o usuário interage através de um menu numérico:
1.  **Criar Tarefa**: Solicita título e descrição, gerando um ID automático e registrando a data/hora atual.
2.  **Listar Tarefas**: Exibe todas as tarefas cadastradas na sessão.
3.  **Alternar Status**: Altera o estado de "Pendente" para "Concluída" informando o ID.
4.  **Excluir Tarefa**: Remove a tarefa da memória com base no ID digitado.