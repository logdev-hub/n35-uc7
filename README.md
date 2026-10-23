# UC7 — Mapear e Estimar Custos Logísticos

Site-caderno estático para a Unidade Curricular 7 do Técnico em Logística, turma LOG N35, Senac Guarulhos.

## Executar no VS Code

Abra a pasta no VS Code e inicie um servidor HTTP local. Uma opção é a extensão Live Server; outra é executar `python -m http.server 8000` na raiz e abrir `http://localhost:8000`.

Não abra apenas `index.html` pelo caminho `file://`: os navegadores podem bloquear recursos locais e os PDFs não terão o mesmo comportamento.

## Estrutura

- `index.html`: shell da aplicação e navegação global.
- `assets/css/main.css`: design system responsivo inspirado na referência UC9.
- `assets/js/data.js`: capítulos, fundamentos, cases, fórmulas, glossário e relações.
- `assets/js/app.js`: roteamento hash, renderização, calculadoras, progresso, busca, favoritos e exportação.
- `documents/`: cópias dos dois PDFs oficiais.
- `CONTENT_AUDIT.md`: inventário de origem, cobertura e limitações verificadas.

## Rotas

As rotas são compatíveis com hospedagem estática e podem ser acessadas diretamente após o carregamento da home:

- `#inicio`, `#conceitos`, `#cases`, `#formulas`, `#calculadoras`, `#glossario`, `#biblioteca`, `#logi-a`.
- `#conceito/2-1` para um fundamento individual.
- `#case/1` para um case individual.

## Publicar no GitHub Pages

1. Publique todos os arquivos deste diretório em um repositório.
2. Em Settings → Pages, selecione a branch e a pasta publicada.
3. Mantenha os caminhos relativos e a pasta `documents/` no mesmo nível de `index.html`.

A aplicação não requer backend, banco de dados ou build. Bootstrap, Bootstrap Icons, Chart.js e a fonte visual são carregados por CDN; para uma publicação sem dependência externa, baixe essas bibliotecas e ajuste os links do HTML.

## Conteúdo e manutenção

Edite `assets/js/data.js` para incluir novos fundamentos, cases, fórmulas ou termos. Preserve `pages`/referências e diferencie conteúdo oficial de explicações adicionais. Ao alterar uma fórmula, atualize também a calculadora correspondente e registre a decisão em `CONTENT_AUDIT.md`.

O progresso, respostas, favoritos e última rota ficam somente no `localStorage` do navegador. O botão Exportar JSON cria uma cópia local; isso não constitui registro acadêmico institucional.

## LOGI-A

O acesso abre a URL oficial do agente em nova aba e oferece prompts contextualizados. Não existe API simulada nem integração automática. É necessário login com conta educacional Microsoft autorizada.
