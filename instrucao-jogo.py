## ============================================================
## Quiz Game - versão guiada (em dupla)
## ============================================================
## Vocês vão construir um quiz simples, JUNTOS, num arquivo só,
## versionando tudo no GitHub.
##
## O arquivo tem duas partes:
##   PASSO 0  -> como começar (GitHub, pasta, trabalho em dupla)
##   BLOCOS 1-5 -> o código do jogo (comentários são PERGUNTAS
##                 para guiar vocês; pensem e escrevam)
## ============================================================
 
 
## ============================================================
## PASSO 0 — ANTES de escrever qualquer código
## ============================================================
##
## Pergunta que todo mundo faz: "eu crio a pasta no meu PC
## primeiro, ou crio o projeto no GitHub primeiro?"
##   -> Resposta: comece NO GITHUB. Quando são dois, é mais fácil.
##
## ------------------------------------------------------------
## (A) UMA pessoa da dupla cria o repositório no site:
##     1. Entre em github.com e clique no botão verde "New"
##     2. Repository name: quiz   |   marque "Public"
##     3. marque "Add a README file"
##     4. clique em "Create repository"
##
## (B) Essa MESMA pessoa dá acesso ao colega (é isso que deixa
##     o outro ajudar e aprovar coisas no repositório):
##     - dentro do repo: aba "Settings" -> "Collaborators"
##     - clique em "Add people" e convide o usuário do colega
##     - o colega aceita o convite (chega no e-mail dele)
##
## (C) AGORA os DOIS trazem o projeto para o PC (passo igual p/ os dois):
##     - no repo do GitHub, clique no botão verde "Code" e copie o link
##     - no VS Code: Cmd/Ctrl + Shift + P -> digite "Git: Clone"
##     - cole o link, escolha uma pasta e abra
##
##   > Por que GitHub primeiro? Assim os dois clonam o MESMO repo e
##     já ficam conectados. Se um criasse só no PC, o outro ficaria
##     de fora até alguém "subir" o projeto.
## ------------------------------------------------------------
##
## COMO UM AJUDA E APROVA O TRABALHO DO OUTRO
## (a parte que parece mágica, mas é simples)
##
## Regra de ouro: ninguém escreve direto na branch principal (main).
## Cada um trabalha na SUA branch e PEDE para juntar.
##
##     1. Crie sua branch: na barra de baixo do VS Code, clique no
##        nome "main" -> "Create new branch" -> dê um nome (ex: parte-ana)
##     2. Faça sua parte e vá salvando: painel Source Control (🌿)
##        -> escreva a mensagem -> Commit -> "Sync"
##     3. No GitHub, abra um "Pull Request" (Compare & pull request):
##        é o pedido "olha o que eu fiz, podem juntar?"
##     4. O COLEGA abre esse Pull Request e:
##        - clica em "Files changed" para ver o que mudou
##        - clica em "Review changes" -> "Approve" para aprovar
##     5. Aprovado, clique em "Merge pull request" para juntar na main
##
##   > É por aqui que um "libera e aprova" o trabalho do outro: pelo
##     Pull Request, o colega vira revisor antes de o código entrar.
##
## Combinem quem faz o quê: por exemplo, uma pessoa cuida dos blocos
## 1-2-3 e a outra dos blocos 4-5. Cada um na sua branch.
## ============================================================
 
 
 
## ============================================================
## AGORA O JOGO — escrevam o código respondendo as perguntas
## ============================================================
 
 
## ------------------------------------------------------------
## 1) Guardar as perguntas
##
## Pensa comigo: um quiz tem VÁRIAS perguntas, e cada pergunta
## tem partes diferentes (o enunciado, as opções e qual é a certa).
##
##  > Que estrutura do Python guarda vários itens em sequência?
##  > E para juntar as partes de UMA pergunta, cada uma com seu
##    "rótulo" (enunciado, opcoes, correta), o que usaríamos?
##
## Crie abaixo uma lista com 50 perguntas
## ------------------------------------------------------------
 
perguntas = {pergunta1 = {
    "enunciado":   "Qual é a capital do Brasil?",
    "opcoes":      ["São Paulo", "Brasília", "Rio", "Salvador"],
    "correta":     1,            # índice (começa em 0) da opção certa
    "categoria":   "Geografia",
    "dificuldade": "facil"}
}
 
 
## ------------------------------------------------------------
## 2) Mostrar UMA pergunta na tela
##
##  > Como você mostraria o enunciado de uma pergunta?
##  > E como mostrar cada opção com um número na frente
##    (1, 2, 3...) para a pessoa escolher?
##      (pensa: o que um `for` faz com a lista de opções?
##       e como numerar enquanto percorre?)
##  > Depois de mostrar, como capturar o que a pessoa digitou?
##      (qual função lê algo do teclado?)
## ------------------------------------------------------------

 
 
 
## ------------------------------------------------------------
## 3) Descobrir se a pessoa acertou
##
##  > A resposta certa está guardada como a POSIÇÃO da opção
##    correta na lista. Se a pessoa digita "1", a que posição
##    isso corresponde? (lembra em que número uma lista começa?)
##  > Como comparar a escolha da pessoa com a resposta certa
##    para saber se acertou?
## ------------------------------------------------------------
 
 
 
 
## ------------------------------------------------------------
## 4) Jogar TODAS as perguntas e somar os pontos
##
##  > Como repetir "mostrar pergunta + conferir resposta" para
##    CADA pergunta da lista? (qual laço percorre a lista toda?)
##  > Onde guardar quantos acertos a pessoa fez ao longo do jogo?
##    (que tal uma variável que começa em 0 e cresce a cada acerto?)
## ------------------------------------------------------------
 
 
 
 
## ------------------------------------------------------------
## 5) Mostrar o resultado final
##
##  > Terminadas as perguntas, como mostrar quantos pontos a
##    pessoa fez, de quantas perguntas no total?
##  > (bônus) Como dar uma mensagem diferente para quem foi muito
##    bem e para quem foi mal? (qual estrutura escolhe entre
##    caminhos diferentes?)
## ------------------------------------------------------------
 
 
 
## ------------------------------------------------------------
## Terminou? Então vocês já têm o coração do jogo no ar, no GitHub,
## feito a quatro mãos! No projeto maior a gente vai:
##   - tirar as perguntas daqui e colocar num CSV (feito por IA)
##   - separar "guardar perguntas" de "rodar o jogo" (banco x motor)
##   - somar um ranking
## ------------------------------------------------------------