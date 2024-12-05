// scripts.js

// Seleciona o elemento do título e os botões de cor
const nomeAluno = document.getElementById("meu-nome");
const botoesCores = document.querySelectorAll(".cor");

// Adiciona evento de clique aos botões
botoesCores.forEach((botao) => {
  botao.addEventListener("click", () => {
    const corSelecionada = botao.getAttribute("data-color");
    nomeAluno.style.color = corSelecionada;
  });
});
