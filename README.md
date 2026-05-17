# 🏥 Sistema Profissional para Corretores de Saúde

Sistema desktop profissional desenvolvido em **Python**, utilizando **Tkinter + ttkbootstrap**, com foco em gestão comercial para corretores de planos de saúde.

O projeto possui interface moderna, dashboard administrativo, métricas em tempo real, cadastro de clientes, exportações profissionais e estrutura modular organizada para evolução SaaS.

---

# 🚀 Tecnologias Utilizadas

- Python 3.11+
- Tkinter
- ttkbootstrap
- SQLite
- Pandas
- Matplotlib
- ReportLab
- OpenPyXL

---

# 🎨 Interface Moderna

O sistema utiliza:

- Tema Dark Profissional
- Dashboard Comercial
- Sidebar moderna
- Cards de métricas
- Tabela dinâmica
- Interface estilo CRM/SaaS

---

# 📦 Funcionalidades Implementadas

## ✅ Login Administrativo

Sistema de autenticação inicial:

```txt
Usuário: admin
Senha: 123
```

---

## ✅ Dashboard Comercial

Painel principal contendo:

- Total de clientes
- Cadastros do mês
- Quantidade de planos vendidos
- Atualização em tempo real

---

## ✅ CRUD Completo de Clientes

O sistema permite:

- Cadastrar clientes
- Editar clientes
- Excluir clientes
- Pesquisar clientes
- Atualizar dados

---

## ✅ Cadastro Completo

Campos disponíveis:

- Nome
- Idade
- Plano de saúde
- Cidade
- Telefone
- Email

---

## ✅ Planos de Saúde

Suporte para:

- Amil
- Bradesco Saúde
- SulAmérica
- Unimed
- NotreDame Intermédica
- Porto Saúde

---

## ✅ Exportação Excel

Exportação automática de clientes para:

```plaintext
exports/clientes.xlsx
```

---

## ✅ Exportação PDF

Geração de relatórios profissionais em PDF:

```plaintext
reports/clientes.pdf
```

---

## ✅ Dashboard com Gráficos

Gráfico automático utilizando Matplotlib:

- Quantidade de clientes por plano
- Visualização comercial
- Métricas rápidas

---

# 🗂 Estrutura Profissional do Projeto

```plaintext
sistema_corretor_saude/
│
├── main.py
├── requirements.txt
│
├── database/
│   └── system.db
│
├── scr/
│   ├── database.py
│   ├── metrics.py
│   ├── exports.py
│   ├── services.py
│   └── graphs.py
    

│
├── ui/
│   ├── login.py
│   ├── dashboard.py
│   ├── dashboard.py
│   └── clients.py
│
├── exports/
│
└── reports/
```

---

# ⚙️ Como Instalar o Projeto

## 1️⃣ Clone o projeto

```bash
git clone https://github.com/seuusuario/sistema_corretor_saude.git
```

---

## 2️⃣ Entre na pasta

```bash
cd sistema_corretor_saude
```

---

## 3️⃣ Crie o ambiente virtual

### Windows

```bash
python -m venv venv
```

---

## 4️⃣ Ative o ambiente virtual

### Windows PowerShell

```bash
venv\Scripts\activate
```

---

## 5️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

---

# ▶️ Como Rodar o Sistema

Execute:

```bash
python main.py
```

---

# 🧠 Estrutura do Banco de Dados

Banco SQLite automático:

```plaintext
database/system.db
```

Tabela principal:

```sql
CREATE TABLE clients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    health_plan TEXT,
    city TEXT,
    phone TEXT,
    email TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
```

---

# 📊 Métricas Inteligentes

O sistema calcula automaticamente:

- Total de clientes
- Clientes cadastrados no mês
- Quantidade de planos vendidos

---

# 📈 Possíveis Melhorias Futuras

## 🔥 Melhorias SaaS

- Multiusuário
- Login com permissões
- API REST
- Hospedagem em nuvem
- Integração WhatsApp
- Sistema financeiro
- Agenda comercial
- Assinatura digital
- Integração com operadoras
- Dashboard avançado
- Relatórios BI

---

# 🏗 Arquitetura do Projeto

O projeto foi desenvolvido utilizando:

- Separação em módulos
- Estrutura escalável
- Organização MVC simplificada
- Componentização da interface
- Banco desacoplado
- Reutilização de funções

---

# 🎯 Objetivo do Projeto

Criar um sistema comercial moderno para:

- Corretores de saúde
- Gestão de clientes
- Controle comercial
- Organização de propostas
- Visualização de métricas

---

# 👨‍💻 Desenvolvedor

Projeto desenvolvido por Márcio Silva.

---

# 📄 Licença

Projeto desenvolvido para fins educacionais e profissionais.