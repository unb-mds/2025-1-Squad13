# 🤝 Guia de Contribuição - VIDA Project

Obrigado por considerar contribuir com o projeto VIDA! Este documento contém diretrizes para contribuir com o projeto.

## 🎯 Áreas que Precisam de Ajuda

- **Testes**: Cobertura de testes
- **Documentação**: Tutoriais e exemplos
- **Performance**: Otimização do código
- **IA**: Melhorias no modelo de reconhecimento de voz
- **Segurança**: Segurança da API

## 📋 Como Contribuir

### 🐛 Reportando Bugs

1. **Verifique** se o bug já foi reportado nas [Issues](https://github.com/unb-mds/VIDAProject/issues)
2. **Crie uma nova issue** com as seguintes informações:
   - Descrição clara do problema
   - Passos para reproduzir
   - Comportamento esperado vs atual
   - Screenshots (se aplicável)
   - Informações do ambiente (OS, Python version, etc.)

### ✨ Sugerindo Melhorias

1. **Abra uma issue** com a tag `enhancement`
2. **Descreva** a melhoria proposta
3. **Explique** por que seria útil para o projeto
4. **Forneça** exemplos de uso, se possível

### 🔧 Desenvolvendo

#### Configuração do Ambiente

1. **Fork** o repositório
2. **Clone** seu fork:

   ```bash
   git clone https://github.com/SEU-USERNAME/VIDAProject.git
   cd VIDAProject
   ```

3. **Configure** o ambiente:

   ```bash
   cd vida_project_api
   poetry install
   poetry shell
   ```

4. **Configure** o pre-commit:
   ```bash
   pre-commit install
   ```

#### Padrões de Código

- **Python**: Seguimos PEP 8
- **Linting**: Usamos Ruff
- **Formatação**: Black
- **Type Hints**: Obrigatório para funções públicas
- **Docstrings**: Google style

#### Executando Testes

```bash
# Executar todos os testes
poetry run pytest

# Executar com coverage
poetry run pytest --cov=vida_project_api

# Executar testes específicos
poetry run pytest tests/test_voiceRecording.py
```

#### Commits

Usamos [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

**Tipos:**

- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Mudanças na documentação
- `style`: Formatação, sem mudança de código
- `refactor`: Refatoração de código
- `test`: Adição ou correção de testes
- `chore`: Tarefas de manutenção

**Exemplos:**

```
feat(auth): add voice authentication endpoint
fix(recording): resolve audio buffer overflow
docs: update installation instructions
```

### 🔄 Processo de Pull Request

1. **Crie** uma branch descritiva:

   ```bash
   git checkout -b feat/voice-authentication
   ```

2. **Faça** suas mudanças seguindo os padrões
3. **Teste** suas mudanças
4. **Commit** seguindo as convenções
5. **Push** para seu fork:

   ```bash
   git push origin feat/voice-authentication
   ```

6. **Abra** um Pull Request com:
   - Título claro e descritivo
   - Descrição detalhada das mudanças
   - Referência às issues relacionadas
   - Screenshots (se aplicável)

### ✅ Checklist do PR

- [ ] Código segue os padrões do projeto
- [ ] Testes foram adicionados/atualizados
- [ ] Documentação foi atualizada
- [ ] Todos os testes passam
- [ ] Linting passou sem erros
- [ ] Commits seguem o padrão estabelecido

---

_Obrigado por contribuir com o VIDA Project! 🚀_
