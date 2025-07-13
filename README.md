20x-call-tool – Loop Interativo com Feedback do Usuário
Este projeto oferece um fluxo interativo para envio de imagens ou prompts de texto, ideal para aplicações de IA que requerem interação contínua e feedback do usuário.
🧠 Como Funciona

A cada ciclo, o usuário pode enviar uma imagem ou um texto.
O script userinput.py gerencia a interface gráfica e solicita a próxima entrada após cada tarefa.
O ciclo se repete automaticamente até que o usuário digite stop para finalizar.

📦 Requisitos

Python 3.8 ou superior

Instale as dependências necessárias:
pip install customtkinter CTkMessagebox Pillow



⚙️ Configuração no Cursor
Para configurar o projeto no Cursor, siga estas etapas adicionais:

Crie a pasta .cursor/rules/ no diretório raiz do projeto:
mkdir -p .cursor/rules


Renomeie o arquivo rules.md para .mdc e mova-o para a pasta .cursor/rules/:
mv rules.md .cursor/rules/.mdc


Verifique se o arquivo .mdc está na pasta .cursor/rules/ e contém o conteúdo correto (conforme fornecido no projeto).


🚀 Passos para Utilização

Clone o repositório:
git clone https://github.com/devAdminhu/20x-call-tool.git
cd 20x-call-tool


Execute o script principal:
python userinput.py


Siga as instruções na interface para:

Enviar uma imagem (ela será salva em 20xbuild/img)
Adicionar um prompt opcional
Ou apenas enviar um texto


Após cada envio, uma nova solicitação será apresentada automaticamente.

Para encerrar o ciclo, digite stop quando solicitado.


📁 Estrutura do Projeto

userinput.py: Script principal que gerencia a interface gráfica e o loop interativo.
.cursor/rules/.mdc: Arquivo de regras para configuração no Cursor (após renomeação e movimentação).
20xbuild/img/: Pasta onde as imagens enviadas são salvas.
