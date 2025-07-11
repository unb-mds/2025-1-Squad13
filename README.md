# 🗣️ VIDA Project

## Voice, ID, Detection, Authentication

<div align="center">

![GitHub repo size](https://img.shields.io/github/repo-size/unb-mds/VIDAProject)
![GitHub language count](https://img.shields.io/github/languages/count/unb-mds/VIDAProject)
![GitHub top language](https://img.shields.io/github/languages/top/unb-mds/VIDAProject)
![GitHub](https://img.shields.io/github/license/unb-mds/VIDAProject)

_Revolucionando a autenticação através da biometria de voz_

[🚀 Página do Projeto](#https://unb-mds.github.io/VIDAProject)

</div>

---

## 🎯 Sobre o Projeto

O **VIDA** é uma plataforma inovadora de autenticação biométrica baseada em reconhecimento de voz, desenvolvida com foco em **segurança**, **acessibilidade** e **inovação**. Utilizando tecnologias de ponta em Machine Learning e processamento de áudio, o sistema oferece uma alternativa moderna e segura aos métodos tradicionais de autenticação.

### ⬇️ Acesse nossa Landing Page pelo link abaixo

[https://unb-mds.github.io/VIDAProject/](https://unb-mds.github.io/VIDAProject/)

### 🌟 Por que VIDA?

- **🔒 Segurança Avançada**: Autenticação baseada em características únicas da voz
- **♿ Acessibilidade**: Interface inclusiva e fácil de usar
- **⚡ Performance**: Processamento em tempo real com alta precisão
- **🌐 Escalabilidade**: Arquitetura moderna preparada para crescimento
- **🔄 Confiabilidade**: Sistema robusto com validação contínua

---

## ✨ Funcionalidades

### 🎤 Reconhecimento de Voz

- Captura e processamento de áudio em tempo real
- Análise de características vocais únicas
- Algoritmos de ML para identificação precisa

### 🔐 Autenticação Segura

- Sistema de cadastro de perfis vocais
- Verificação de identidade em tempo real
- Proteção contra tentativas de falsificação

### 🌐 API RESTful

- Endpoints para cadastro e autenticação
- Documentação interativa com FastAPI
- Integração fácil com sistemas existentes

---

## 🛠️ Tecnologias

### Backend

- **Python 3.12** - Linguagem principal
- **FastAPI** - Framework web moderno e rápido
- **SpeechBrain** - Biblioteca de ML para processamento de áudio
- **PostgreSQL** - Banco de dados relacional

### Frontend

- **React 18** - Biblioteca para interfaces de usuário
- **Vite** - Build tool e dev server
- **JavaScript (ES6+)** - Linguagem principal do frontend
- **Axios** - Cliente HTTP para API
- **CSS3** - Estilização responsiva

### DevOps & Infraestrutura

- **Docker** - Containerização
- **Docker Compose** - Orquestração de serviços
- **Poetry** - Gerenciamento de dependências
- **Pytest** - Framework de testes

### Machine Learning

- **TorchAudio** - Processamento de áudio
- **HuggingFace** - Modelos pré-treinados

---

## 📁 Arquitetura do Projeto

```
VIDAProject/
├── docs/                          # 🌐 Landing Page
│   ├── index.html                 # Página principal do projeto
│   └── assets/                    # Imagens e recursos estáticos
├── frontend/                      # 💻 Frontend React
│   ├── src/                       # Código fonte da aplicação
│   ├── public/                    # Arquivos públicos
│   └── package.json               # Dependências do frontend
├── vida_project_api/              # 🚀 Backend API
│   ├── vida_project_api/          # Código da API FastAPI
│   ├── migrations/                # Migrações do banco de dados
│   ├── tests/                     # Testes automatizados
│   └── pyproject.toml             # Dependências do backend
└── documentation/                 # 📚 Documentações e Estudos
    ├── meetings/                  # Atas das reuniões
    └── studies/                   # Estudos e pesquisas realizadas
```

---

## ⚡ Início Rápido

### Pré-requisitos

- Python 3.12
- Node.js (v18 ou superior)
- npm ou yarn
- Docker & Docker Compose
- Git

### � Instalação

1. **Clone o repositório**

   ```bash
   git clone https://github.com/unb-mds/VIDAProject.git
   cd VIDAProject
   ```

2. **Configure o ambiente**

   ```bash
   cd vida_project_api
   poetry install
   ```

3. **Inicie os serviços backend**

   ```bash
   cd vida_project_api
   docker-compose up -d
   ```

4. **Acesse a aplicação backend**

   - API: `http://localhost:8000`
   - Documentação: `http://localhost:8000/docs`

5. **Inicie os serviços frontend**

   ```bash
   cd ../frontend
   npm install
   npm run dev
   ```

6. **Acesse a aplicação frontend**
   - Frontend: `http://localhost:3000`

### 🧪 Executando Testes

```bash
poetry run pytest
```

---

## 📚 Documentação

- [Guia de Contribuição](./docs/contributing.md)

---

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Veja nosso [Guia de Contribuição](./CONTRIBUTING.md) para começar.

### 📋 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feat/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feat/AmazingFeature`)
5. Abra um Pull Request

---

## 👨‍💻 Squad 13 - Equipe de Desenvolvimento

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/osakareaper">
        <img src="https://github.com/osakareaper.png" width="100px;" alt="Marcus"/><br>
        <sub><b>Marcus</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/vhcsdev">
        <img src="https://github.com/vhcsdev.png" width="100px;" alt="Victor Hugo"/><br>
        <sub><b>Victor Hugo</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/Pablo-R-L">
        <img src="https://github.com/Pablo-R-L.png" width="100px;" alt="Pablo"/><br>
        <sub><b>Pablo</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/IsaacMPereira">
        <img src="https://github.com/IsaacMPereira.png" width="100px;" alt="Isaac"/><br>
        <sub><b>Isaac</b></sub>
      </a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://github.com/Rukkakun">
        <img src="https://github.com/Rukkakun.png" width="100px;" alt="Paulo"/><br>
        <sub><b>Paulo</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/leticia-oliveira">
        <img src="https://github.com/leticia-oliveira.png" width="100px;" alt="Letícia"/><br>
        <sub><b>Letícia</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/gsVieiraaa">
        <img src="https://github.com/gsVieiraaa.png" width="100px;" alt="Gabriel"/><br>
        <sub><b>Gabriel</b></sub>
      </a>
    </td>
  </tr>
</table>

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## <div align="center">

_Desenvolvido com ❤️ pelo Squad 13 na Universidade de Brasília_

</div>
