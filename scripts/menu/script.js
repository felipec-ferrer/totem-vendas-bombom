// declaração de variáveis
const estoque = JSON.parse(localStorage.getItem("estoque"));
const div = {
  morango: document.getElementById("divMorango"),
  uva: document.getElementById("divUva"),
  brigadeiro: document.getElementById("divBrigadeiro"),
  casadinho: document.getElementById("divCasadinho"),
  maracuja: document.getElementById("divMaracuja"),
  trufa: document.getElementById("divTrufa"),
};
let bombom = {
  brigadeiro: 0,
  casadinho: 0,
  maracuja: 0,
  morango: 0,
  trufa: 0,
  uva: 0,
};
let numeroBombom = 0;

// script
gerarBotao("morango", div["morango"]);
gerarBotao("uva", div["uva"]);
gerarBotao("brigadeiro", div["brigadeiro"]);
gerarBotao("casadinho", div["casadinho"]);
gerarBotao("maracuja", div["maracuja"]);
gerarBotao("trufa", div["trufa"]);

// funções
function adicionarBombom(sabor) {
  bombom[sabor]++;
  numeroBombom++;
  totalBombomMenu();
  // console.log("Aumentou");
  console.log(numeroBombom);
  console.log(bombom);
}

function totalBombomMenu() {
  let valor = document.getElementById("totalBombom");
  valor.innerText = numeroBombom;
}

function salvarJSON(bombom, numeroBombom) {
  localStorage.setItem("bombom", JSON.stringify(bombom));
  localStorage.setItem("numeroBombom", numeroBombom);
  console.log("Salvo no local storage");
}

function gerarBotao(sabor, div) {
  const botao = document.createElement("button");

  if (estoque[sabor] > 0) {
    botao.className = "botaoCarrinho";
    botao.textContent = "Adicionar ao carrinho";
    botao.onclick = () => adicionarBombom(sabor);
    div.appendChild(botao);
  } else {
    botao.className = "botaoSemEstoque";
    botao.textContent = "Sem estoque";
    div.appendChild(botao);
  }
}
