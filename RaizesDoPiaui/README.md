# Raízes do Piauí — SaaS Cultural

Plataforma cultural interativa que transforma os 12 Territórios de Desenvolvimento do Piauí em experiências digitais. Combina um mapa jogável, missões culturais e a **Jurema IA**  uma assistente que gera roteiros turísticos personalizados com base em atrativos ambientais, culturais, históricos, religiosos e produtivos de cada território.

## Funcionalidades

- **Piauí World** — mapa interativo com os 12 Territórios de Desenvolvimento
- **Roteiro IA (Jurema)** — geração de roteiros turísticos com inteligência artificial
- **Missões culturais** — desafios e conquistas por território
- **Dashboard institucional** — painel de gestão com clientes, licenciamento e relatórios
- **Jogo web** — experiência jogável integrada (Godot Engine exportado para Web)

## Tecnologias

| Camada | Tecnologia |
|---|---|
| Frontend | HTML5, CSS3, JavaScript (vanilla) |
| Tipografia | Google Fonts — Sora + Crimson Pro |
| IA | [Groq API](https://console.groq.com) — modelo `llama-3.3-70b-versatile` |
| Backend | Python 3 (http.server — biblioteca padrão) |
| Jogo | Godot Engine 4 exportado para Web (WebAssembly) |
| Hospedagem | Render.com (servidor) + GitHub Pages (estático) |

## Como executar localmente

### Pré-requisitos

- Python 3 instalado
- Chave de API do Groq (gratuita em [console.groq.com](https://console.groq.com))

### 1. Configure a chave da API

Crie um arquivo `.env` na raiz do projeto (um nível acima desta pasta) com o conteúdo:

```
GROQ_KEY=gsk_sua_chave_aqui
```

### 2. Inicie o servidor

```bash
python server.py
```

### 3. Acesse no navegador

```
http://localhost:3000
```

> A Jurema IA só funciona com o servidor Python rodando. O jogo e o painel funcionam sem o servidor.

## Deploy (Render.com)

O servidor está configurado para detectar a variável `PORT` automaticamente, compatível com Render, Railway e similares.

Basta configurar a variável de ambiente `GROQ_KEY` no painel da plataforma escolhida e usar o comando de start:

```
python RaizesDoPiaui/server.py
```

## Versão

**v1.2 MVP — PIT 2026**
