## 📘 Guia de Versionamento e Fluxo de Trabalho com Git
🚀 1. Inicializar o Repositório (somente na primeira vez)

No diretório raiz do projeto:

```
git init
git branch -M principal
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
```
## 📝 2. Adicionar Arquivos e Fazer o Primeiro Commit
```
git add .
git commit -m "Primeiro commit"
```
## 📤 3. Enviar para o GitHub (primeira vez)
```
git push -u origin principal
```

O parâmetro -u define o vínculo entre a branch local e remota, permitindo usar apenas git push nas próximas vezes.

## 🔄 4. Fluxo Diário de Versionamento

Sempre que adicionar, editar ou remover arquivos:
```
git status          # Verifica o que mudou
git add .           # Adiciona todas as alterações
git commit -m "Descrição clara do que foi feito"
git push            # Envia para o GitHub
```
## ➕ 5. Criar um Novo Estudo de Caso

Ao iniciar uma nova pasta como EstudoCaso02/:
```
mkdir EstudoCaso02
# adicionar arquivos normalmente
git add .
git commit -m "Adicionar EstudoCaso02"
git push
```
## 🧹 6. Organização

Cada estudo de caso fica em sua própria pasta.

Cada pasta contém seu próprio readme.md.


## 🗂 Estrutura do Projeto
```
📁 pythondsa/
│
├── EstudoCaso01/
├── EstudoCaso02/ (em construção)
├── EstudoCaso03/ (em construção)
└── ... 
```
