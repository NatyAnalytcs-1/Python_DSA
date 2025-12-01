# 🧭 Guia de Versionamento com Git + GitHub

Este guia mostra os passos essenciais para iniciar um repositório, enviar o primeiro commit e manter novos estudos organizados no mesmo projeto.

## 🚀 1. Criando o Repositório Local

Dentro da pasta principal pythondsa/, execute:
```
git init
```
## ➕ 2. Adicionando Arquivos ao Controle de Versão

Sempre que você criar um novo EstudoCaso, ou modificar arquivos, adicione tudo com:
```
git add .
```

Verifique o que será enviado:
```
git status
```
## 💾 3. Realizando o Primeiro Commit
```
git commit -m "primeiro commit"
```
## 🌱 4. Criando / Renomeando a Branch Principal

Você pode usar main ou principal.
Exemplo com principal:
```
git branch -M main
```
## 🔗 5. Conectando ao Repositório do GitHub

Pegue a URL HTTPS do repositório que você criou no GitHub:
```
git remote add origin https://github.com/SEU_USUARIO/SEU_REPO.git
```
## 🚀 6. Enviando Para o GitHub (Primeiro Push)
```
git push -u origin principal
```

## Depois disso, só precisa usar:
```
git push
```

## 🔄 Adicionar um Novo EstudoCaso (02, 03, 04...)

Sempre que você criar uma nova pasta:

📁 EstudoCaso02/
📁 EstudoCaso03/


## Faça:

```
git add .
```
```
git commit -m "Adiciona EstudoCaso02"
```
```
git push
```


Simples assim! 😎

## 🗂 Estrutura do Projeto
```
📁 pythondsa/
│
├── 📁EstudoCaso01/
├── 📁EstudoCaso02/ (em construção)
├── 📁EstudoCaso03/ (em construção)
└── ... 

```


## 📌 Resumo Ultra Rápido do Fluxo Diário

Sempre que fizer alterações:
```
git add .
git commit -m "Descrição do que mudou"
git push

```
| Ação               | Comando               |
| ------------------ | --------------------- |
| Criar repo local   | `git init`            |
| Ver mudanças       | `git status`          |
| Adicionar arquivos | `git add .`           |
| Criar commit       | `git commit -m "msg"` |
| Enviar para GitHub | `git push`            |
| Baixar projeto     | `git clone URL`       |
| Atualizar local    | `git pull`            |
