Plataforma cultural interativa que transforma os 12 Territórios de Desenvolvimento do Piauí em experiências digitais. Combina um mapa jogável, missões culturais e a **Jurema IA**  uma assistente que gera roteiros turísticos personalizados com base em atrativos ambientais, culturais, históricos, religiosos e produtivos de cada território.

## Funcionalidades

- **Piauí World** — mapa interativo com os 12 Territórios de Desenvolvimento
- **Roteiro IA (Jurema)** — geração de roteiros turísticos com inteligência artificial
- **Missões culturais** — desafios e conquistas por território
- **Jogo web** — experiência jogável integrada (Godot Engine exportado para Web)

## Tecnologias

| Camada | Tecnologia |
|---|---|
| Frontend | HTML5, CSS3, JavaScript (vanilla) |
| Tipografia | Google Fonts — Sora + Crimson Pro |
| IA | [Groq API](https://console.groq.com) — modelo `llama-3.3-70b-versatile` |
| Servidor | Python 3 (http.server — biblioteca padrão) |
| Jogo | Godot Engine 4 exportado para Web (WebAssembly) |
| Hospedagem | Render.com (servidor) + GitHub Pages (estático) |

## Como executar
## Deploy (Render.com)

O servidor está hospedado no Render. Acesse o link
https://raizes-do-piaui.onrender.com/

## Como executar localmente
```



### Pré-requisitos

- Python 3 instalado
- Chave de API do Groq (gratuita em [console.groq.com](https://console.groq.com))

### 1. Configure a chave da API

Crie um arquivo `.env` na raiz do projeto (um nível acima desta pasta) com o conteúdo:

```
GROQ_KEY=gsk_a_gente_vai_mandar_se_for_o_caso_de_rodar_localmente
```

### 2. Inicie o servidor

```bash
python server.py
```

### 3. Acesse no navegador

```
http://localhost:3000
```

> A Jurema IA funciona com o servidor Python rodando. O jogo e o painel funcionam sem o servidor.




## Versão

**v1.2 MVP — PIT 2026**
# Raízes do Piauí — Plataforma SaaS de gamifição com inteligência artificial para valorização cultural, economia criativa e turismo.



https://drive.google.com/drive/folders/1H2ZXzQmQw6quDxXI1t2ApFfZ79KV86NE?usp=sharing
<img width="1198" height="673" alt="DiagramaDeArquitetura" src="https://github.com/user-attachments/assets/aac029fe-d41b-4c16-bd53-e1aa1e56edf1" />
