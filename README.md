# Template de disciplina

Modelo de site de disciplina em página única, inspirado em
https://glauberrleite.com/curso-probabilidade-e-estatistica/ — inclui:

- uma página inicial só (`index.qmd`) com as seções: Aulas, Ementa,
  Cronograma, Avaliação, Bibliografia e Docente;
- cada aula com *slides* em `revealjs` (roda no navegador, tecla `P` entra em
  modo apresentação) e uma página de *notas* em texto normal;
- alternância automática de tema claro/escuro na navbar;
- workflow de publicação via GitHub Actions (com instalação de Python/Jupyter).

## Como usar para uma nova disciplina

1. Copie esta pasta inteira para `quarto/nome-da-disciplina/`.
2. Renomeie a pasta `aulas/00-exemplo/` para a primeira aula real
   (ex: `aulas/00-introducao/`) e edite `aula.qmd` e `notas.qmd`.
3. Em `_quarto.yml`, troque `NOME DA DISCIPLINA` pelo título real e o link do
   repositório no navbar.
4. Em `index.qmd`, edite o texto de abertura, duplique o bloco
   `.aula-card` para cada aula, e preencha Ementa, Cronograma, Avaliação,
   Bibliografia.
5. Se a disciplina **não** usar código Python, remova a linha `engine:
   jupyter` do `_quarto.yml`, o arquivo `requirements.txt`, e os passos
   "Instalar Python" / "Instalar dependências Python" do workflow em
   `.github/workflows/publish.yml`.
6. Crie o repositório no GitHub Desktop com o nome da disciplina (mesmo
   processo já usado nas outras) e siga o fluxo normal: preview local →
   commit/push → Settings → Pages → Source = GitHub Actions.
