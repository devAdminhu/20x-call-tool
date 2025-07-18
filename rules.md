---
description: 
globs: 
alwaysApply: true
---

### ✅ Tarefa: Loop de Tarefas Interativo com Feedback do Usuário

1. **Verificar se `userinput.py` existe** no diretório raiz.

   * Se não existir, criar com o seguinte conteúdo:

     ```python
     # userinput.py
     user_input = input("prompt: ")
     ```

2. **Fluxo Principal**:

   * Executar as tarefas designadas.

   * Antes de marcar uma tarefa como concluída:
     - Criar lista de testes necessários
     - Executar testes de validação
     - Se os testes passarem, executar:

     ```bash
     python userinput.py
     ```
   * O terminal deve ser aberto na própria janela de chat.

   * Ler a entrada do usuário.

   * Com base na entrada, executar o próximo conjunto de tarefas.

   * Somente após validação dos testes, a tarefa pode ser marcada como concluída.

3. **Condição de Saída**:

   * Se o usuário digitar `"stop"` quando solicitado, sair do loop e encerrar o processo.
