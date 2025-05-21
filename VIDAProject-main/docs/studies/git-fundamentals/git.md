# Estudo: Git, GitHub e GitHub Pages

## Índice
1. [Instalação do Git](#instalação-do-git)
2. [Configuração Inicial](#configuração-inicial)
3. [Comandos Básicos do Git](#comandos-básicos-do-git)
4. [Commit Guidelines](#commit-guidelines)
5. [GitHub Pages](#github-pages)
6. [Solução de Problemas](#solução-de-problemas)
7. [Dicas Adicionais](#dicas-adicionais)

---

## Instalação do Git

### Windows
- Baixe e execute o instalador do [Git for Windows](https://git-scm.com/download/win).

### Linux (Debian/Ubuntu)
```bash
sudo apt update && sudo apt install git
```

### macOS
```bash
brew install git
```

---

## Configuração Inicial
Configure seu nome e e-mail globalmente:
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
git config --global init.defaultBranch main
```

---

## Comandos Básicos do Git
- Iniciar um repositório: `git init`
- Clonar: `git clone [URL]`
- Ver status: `git status`
- Adicionar arquivo(s): `git add [arquivo]`
- Registrar alterações: `git commit -m "mensagem"`
- Visualizar histórico: `git log`
- Enviar para o remoto:
  ```bash
  git push -u origin main
  ```
- Atualizar repositório: `git pull`

---

## Commit Guidelines

Use as diretrizes abaixo e emojis para padronizar suas mensagens de commit:

- ✨ feat: Nova funcionalidade.
- 🐛 fix: Correção de bug.
- 📝 docs: Atualizações na documentação.
- 💄 style: Ajustes de formatação ou estilo.
- ♻️ refactor: Refatoração de código.
- ✅ test: Adição ou modificação de testes.
- 🔧 chore: Manutenção ou ajustes sem impacto funcional.
- 📚: Adicionar estudos


Formato sugerido:
```plaintext
<emoji> <tipo>: <descrição breve>
```

Exemplo:
```plaintext
✨ feat: adiciona login social via Google
```

---

## GitHub Pages

1. Crie um repositório chamado `[usuário].github.io` ou use a branch `gh-pages` de outro repositório.
2. Adicione seus arquivos (HTML/CSS/JS).
3. Habilite o GitHub Pages nas configurações do repositório.

Exemplo:
```bash
echo "Olá, Mundo!" > index.html
git add index.html
git commit -m "📝 docs: adiciona página inicial"
git push origin main
```

Acesse: https://[usuário].github.io

---

## Solução de Problemas

- Autenticação: Prefira usar chave SSH ou Personal Access Token.
- Merge Conflicts:
  1. Ajuste os arquivos com conflitos.
  2. Adicione e registre as mudanças:
     ```bash
     git add [arquivo]
     git commit -m "resolve conflitos"
     ```

---

## Dicas Adicionais

- Use um arquivo .gitignore para ignorar arquivos/pastas desnecessárias (ex: node_modules/).
- Crie aliases no .gitconfig para comandos comuns:
  ```ini
  [alias]
    st = status
    co = checkout
  ```
- Explore o GitHub CLI para uma gestão mais dinâmica dos repositórios.

