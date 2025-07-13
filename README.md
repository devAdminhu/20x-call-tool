# 20xbuild – Loop Interativo de Tarefas com Feedback do Usuário

Este repositório implementa um fluxo interativo para entrada de imagens ou prompts de texto, ideal para aplicações de IA que exigem interação contínua com o usuário.

## 🧠 Visão Geral

- O usuário pode enviar uma imagem ou um texto a cada ciclo.
- O script `userinput.py` gerencia a interface e solicita a próxima entrada após cada tarefa.
- O processo repete até que o usuário digite `stop` para encerrar.

## 📦 Requisitos

- Python 3.8 ou superior
- Instale as dependências com:

  ```bash
  pip install customtkinter CTkMessagebox Pillow
  ```

## 🚀 Como Usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/devAdminhu/20xbuild.git
   cd 20x-call-tool
   ```

2. Execute o script principal:

   ```bash
   python userinput.py
   ```

3. Siga as instruções na interface para:
   - Enviar uma imagem (será salva em `20xbuild/img`)
   - Adicionar um prompt opcional
   - Ou apenas enviar um texto

4. Após cada envio, uma nova solicitação será feita automaticamente.

5. Digite `stop` quando quiser encerrar o ciclo.

## 📁 Estrutura do Projeto
