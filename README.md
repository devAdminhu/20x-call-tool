# 20x-call-tool – Loop Interativo com Feedback do Usuário

Este projeto oferece um fluxo interativo para envio de imagens ou prompts de texto, ideal para aplicações de IA que requerem interação contínua e feedback do usuário.

## 🧠 Como Funciona

- A cada ciclo, o usuário pode enviar uma imagem ou um texto.
- O script `userinput.py` gerencia a interface gráfica e solicita a próxima entrada após cada tarefa.
- O ciclo se repete automaticamente até que o usuário digite `stop` para finalizar.

## 📦 Requisitos

- Python 3.8 ou superior
- Instale as dependências necessárias:

  ```bash
  pip install customtkinter CTkMessagebox Pillow
  ```

## 🚀 Passos para Utilização

1. Clone o repositório:

   ```bash
   git clone https://github.com/devAdminhu/20xbuild.git
   cd 20xbuild
   ```

2. Execute o script principal:

   ```bash
   python userinput.py
   ```

3. Siga as instruções na interface para:
   - Enviar uma imagem (ela será salva em `20xbuild/img`)
   - Adicionar um prompt opcional
   - Ou apenas enviar um texto

4. Após cada envio, uma nova solicitação será apresentada automaticamente.

5. Para encerrar o ciclo, digite `stop` quando solicitado.

## 📁 Estrutura do Projeto
