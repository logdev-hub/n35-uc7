# Auditoria de conteúdo — UC7

## Fontes primárias

| Arquivo | Páginas | Uso na plataforma |
|---|---:|---|
| `Base_Conceitual_UC7.pdf` | 43 | Capítulos 1–13, fundamentos, indicadores, fórmulas, glossário e referências |
| `Cases_por_Aula_UC7_Aluno.pdf` | 94 | 21 cases, dados, fórmulas, tarefas e orientações do caderno do aluno |

Os PDFs originais foram copiados sem alteração para `documents/` e permanecem disponíveis para visualização e download.

## Cobertura estruturada

| Fonte | Páginas | Conteúdo | Rota/implementação | Status |
|---|---:|---|---|---|
| Base Conceitual | 5–6 | Competência, conhecimentos, habilidades, atitudes e mapa das aulas | Home, indicadores e `#conceitos` | Implementado |
| Base Conceitual | 7–12 | Contabilidade de custos | 9 fundamentos individuais e fórmulas relacionadas | Implementado |
| Base Conceitual | 13–15 | Matemática financeira e investimentos | 7 fundamentos individuais | Implementado |
| Base Conceitual | 16–19 | Cálculos logísticos, câmbio, estatística e previsão | 6 fundamentos individuais + calculadoras | Implementado |
| Base Conceitual | 20–21 | Custo logístico total | 5 fundamentos individuais | Implementado |
| Base Conceitual | 22–24 | Suprimentos e estoque | 7 fundamentos individuais + EOQ/ES/PP | Implementado |
| Base Conceitual | 25–26 | Armazenagem e contratos | 5 fundamentos individuais | Implementado |
| Base Conceitual | 27–30 | Transporte e distribuição | 7 fundamentos individuais + cubagem/frete | Implementado |
| Base Conceitual | 31–33 | Produção, qualidade e reversa | 4 fundamentos individuais | Implementado |
| Base Conceitual | 34–36 | Tributos e importação | 6 fundamentos individuais | Implementado; legislação sinalizada como didática |
| Base Conceitual | 37–38 | Sistemas, dados e relatórios | 5 fundamentos individuais | Implementado |
| Base Conceitual | 39–40 | Redução e decisão | 5 fundamentos individuais | Implementado |
| Base Conceitual | 41–43 | Glossário, formulário e referências | Glossário, catálogo de fórmulas e biblioteca | Implementado |
| Cases | 5–10 | Aula 01 · Café Serra Alta | `#case/1`, dados essenciais, 6 tarefas e prompt | Implementado |
| Cases | 11–14 | Aula 02 · Eletrolar Nordeste | `#case/2`, dados essenciais, 6 tarefas e prompt | Implementado |
| Cases | 15–94 | Aulas 03–21 | Uma rota por case, dados essenciais, tarefas e referência às páginas | Implementado |

## Fórmulas catalogadas

Foram estruturadas 15 fórmulas reutilizáveis: margem de contribuição, ponto de equilíbrio, margem de segurança, markup, cubagem, frete, EOQ, estoque de segurança, ponto de pedido, custo logístico total, VPL, depreciação, câmbio, giro e cost-to-serve. As calculadoras usam implementação numérica, validação básica e formatação pt-BR.

## Decisões e limitações

- A referência visual `https://logdev-hub.github.io/n33-uc9/` foi acessível e orientou o uso de hero azul, laranja de destaque, Bootstrap, cards, trilha e progresso local. O CSS não foi copiado: foi reimplementado para a identidade da UC7.
- A plataforma usa rotas hash para funcionar em GitHub Pages sem configuração de servidor. Cada fundamento e cada case tem URL própria.
- Os PDFs foram preservados como fonte primária e os dados essenciais/tarefas foram estruturados no app. Quadros extensos continuam acessíveis por página no PDF oficial, inclusive pelo botão contextual em cada case.
- Valores, empresas e alíquotas dos materiais são didáticos. O app não atualiza legislação tributária nem pretende substituir conferência docente ou normativa.
- Não foram corrigidos silenciosamente cálculos ou divergências do material original. A auditoria técnica deve ser ampliada caso o docente queira validar cada linha numérica contra um gabarito institucional.

## Validação realizada

- Sintaxe JavaScript verificada com `node --check` em `assets/js/app.js` e `assets/js/data.js`.
- PDFs conferidos por leitura programática: 43 e 94 páginas.
- Links dos PDFs e estrutura de documentos conferidos no workspace.
- Calculadoras revisadas para divisores inválidos, taxas, percentuais, valores negativos e formatação monetária.
- Teste manual recomendado antes da publicação: percorrer todas as 21 rotas de case, testar viewport de 320 px, limpar localStorage e abrir a aplicação a partir de um subdiretório GitHub Pages.
