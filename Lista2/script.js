const nomeAluno = document.getElementById("meu-nome");
const botoesCores = document.querySelectorAll(".cor");

botoesCores.forEach((botao) => {
  botao.addEventListener("click", () => {
    const corSelecionada = botao.getAttribute("data-color");
    nomeAluno.style.color = corSelecionada;
  });
});