# desafio-pior-ux

## 🎨 Desafio Prático de UI e UX - A Engenharia do Erro

## 📌 Sobre o Projeto

Este projeto foi desenvolvido para a atividade **“UI vs. UX & A Engenharia do Erro”**, com o objetivo de criar uma interface propositalmente confusa e desagradável para o usuário.

A proposta foi desenvolver um fluxo de cadastro que utiliza elementos de **má experiência do usuário (UX)** e uma **interface visualmente caótica (UI)**, permitindo compreender, na prática, por que boas práticas de usabilidade são importantes.

O fluxo foi desenvolvido de forma funcional, permitindo que o usuário consiga chegar até o final da experiência.

---

## 🧩 Fluxo do Projeto

O usuário passa por diferentes etapas de um cadastro:

1. Página inicial;
2. Preenchimento dos dados;
3. Criação de senha;
4. Confirmação final;
5. Tela de erro 404 simulada;
6. Mensagem educativa sobre phishing.

Durante o fluxo, são apresentados elementos propositalmente confusos para dificultar a navegação.

---

## ❌ Princípios e Heurísticas Violados

### 1. Botões confusos

Os botões possuem textos contraditórios ou pouco claros, dificultando a decisão do usuário.

**Princípio violado:** Consistência e padrões.

**Como deveria ser:** Os botões deveriam possuir textos objetivos, como “Continuar”, “Voltar” e “Cancelar”, deixando clara a ação de cada um.

### 2. Mensagens confusas

Algumas mensagens apresentam informações contraditórias ou pouco úteis para o usuário.

**Princípio violado:** Visibilidade do status do sistema.

**Como deveria ser:** O sistema deveria apresentar mensagens claras, informando exatamente o que aconteceu e o que o usuário deve fazer.

### 3. Validações e regras confusas

O formulário utiliza comportamentos que podem deixar o usuário em dúvida sobre o que deve fazer.

**Princípio violado:** Prevenção de erros.

**Como deveria ser:** As regras deveriam ser apresentadas de maneira simples, com orientações claras antes e durante o preenchimento.

### 4. Interface visualmente exagerada

Foram utilizadas cores fortes, elementos chamativos e uma organização propositalmente pouco agradável.

**Princípio violado:** Estética e design minimalista.

**Como deveria ser:** Uma interface profissional deveria utilizar cores equilibradas, boa organização, espaçamento adequado e hierarquia visual.

### 5. Botão que se movimenta

Na tela final da simulação, o botão “Cancelar” se movimenta quando o usuário tenta interagir com ele.

**Princípio violado:** Controle e liberdade do usuário.

**Como deveria ser:** O usuário deve conseguir clicar nos botões e cancelar uma ação quando desejar.

### 6. Tela de erro simulada

Depois de uma determinada ação, o usuário é direcionado para uma tela de erro 404 que informa que ele caiu em uma simulação de phishing.

**Princípio violado:** Correspondência entre o sistema e o mundo real.

**Como deveria ser:** Uma página de erro real deveria explicar claramente o problema e oferecer uma maneira simples de voltar ou continuar navegando.

---

## 💡 Proposta de Correção / Versão Ideal

Em uma versão profissional do sistema, os problemas apresentados seriam corrigidos da seguinte forma:

* Utilizar botões com nomes claros e objetivos;
* Manter os mesmos padrões visuais em todas as telas;
* Utilizar cores com bom contraste;
* Informar claramente os erros e orientar o usuário sobre como corrigi-los;
* Evitar mensagens contraditórias;
* Não movimentar ou esconder botões;
* Permitir que o usuário tenha controle sobre suas ações;
* Organizar melhor os campos e informações;
* Utilizar uma interface simples, acessível e fácil de entender.

Dessa forma, o usuário conseguiria completar o cadastro de maneira rápida, clara e sem frustração.

---

## 🎯 Objetivo da Atividade

O objetivo foi compreender, na prática, a diferença entre **UI (Interface do Usuário)** e **UX (Experiência do Usuário)**.

Ao criar uma interface propositalmente ruim, foi possível perceber como cores, textos, botões, mensagens e comportamentos podem influenciar diretamente a experiência de quem utiliza um sistema.

A atividade também demonstra que uma interface visualmente chamativa não significa necessariamente uma boa experiência de uso.

---

## ▶️ Como Executar

Para executar o projeto localmente:

1. Faça o download ou clone este repositório;
2. Abra a pasta do projeto no Visual Studio Code;
3. Instale as dependências necessárias;
4. Execute o arquivo principal da aplicação;
5. Acesse o endereço local disponibilizado pela aplicação;
6. Siga o fluxo do cadastro até a tela final.

---

## 🛠️ Tecnologias Utilizadas

* HTML5
* CSS3
* JavaScript
* Python
* Flask

---

## 👥 Integrantes

* Nicoly
* Beatryz
* Maria Eduarda
* Wérica

---

## 📚 Conclusão

O projeto mostrou que pequenos problemas de interface podem gerar uma experiência confusa e frustrante para o usuário.

Através da construção da pior experiência possível, foi possível identificar a importância de princípios de UX, acessibilidade, clareza, consistência e controle do usuário no desenvolvimento de sistemas.

A experiência reforça que um bom sistema deve ser **claro, funcional, acessível e fácil de utilizar**.
