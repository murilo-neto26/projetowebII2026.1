# projetowebII2026.1

## Nome do projeto

**RetroToons**

---

## Descrição

O RetroToons é uma plataforma web voltada para fãs de desenhos animados clássicos e nostálgicos. O sistema permite explorar uma biblioteca inteligente de desenhos antigos, criar listas personalizadas de favoritos, participar de quizzes interativos e acessar conteúdos históricos e curiosidades sobre produções animadas marcantes de diferentes décadas.

O objetivo do projeto é reunir entretenimento, nostalgia e informação em um único ambiente interativo e intuitivo.

---

## Membros da equipe

- Karynne Mota de Abreu - karynne.abreu11@aluno.ifce.edu.br
- Maria Alice Cavalcante de Brito - alice.cavalcante11@aluno.ifce.edu.br
- Maria Jardiele Silva de Souza - jardiele.silva11@aluno.ifce.edu.br
- Murilo Silva Rodrigues - silva.murilo06@aluno.ifce.edu.br

---

## Tecnologias usadas

- Django 6.0.5
- SQLite
- Python 3.14.2

---

## Como executar (passo a passo)

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
```

### 2. Entrar na pasta do projeto

```bash
cd projetowebII2026.1
```

### 3. Criar o ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### 5. Instalar as dependências

```bash
pip install django
```

### 6. Executar as migrações

```bash
python manage.py migrate
```

### 7. Criar um superusuário

```bash
python manage.py createsuperuser
```

### 8. Iniciar o servidor

```bash
python manage.py runserver
```

### 9. Acessar no navegador

```text
http://127.0.0.1:8000/
```

---

## Funcionalidades (checklist)

### 🧠 1. Biblioteca inteligente de desenhos

_Uma base de dados interativa._

#### Funcionalidades:

- [ ] Busca por década (anos 60, 70, 80, etc.)
- [ ] Filtro por gênero (comédia, aventura, mistério…)
- [ ] Estúdios
- [ ] Sessões temáticas (“desenhos esquecidos”, “clássicos dos sábados”)

---

### 🎨 2. Criador de listas personalizadas

_Uma funcionalidade onde o usuário pode criar listas com seus desenhos favoritos, funcionando como um “portfólio pessoal de nostalgia”._

#### Funcionalidades:

- [ ] Criar listas como “Top 10 da infância”
- [ ] Criar listas de “Melhores vilões”
- [ ] Adicionar e remover desenhos das listas

---
