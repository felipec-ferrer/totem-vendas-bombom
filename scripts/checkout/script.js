// declaração de variáveis
let bombom = restaurarLocalStorage("bombom");
let numeroBombom = restaurarLocalStorage("numeroBombom");
let itensMostrados = 0;
let valorTotal = 0;
const divCheckout = document.getElementById("checkout");
const divValorTotal = document.getElementById("valorTotal");
const divFinalizar = document.getElementById("finalizar");
const textoValorTotal = document.createElement("p");
const textoFinalizar = document.createElement("a");

// script
if (Object.keys(bombom).length === 0 || !bombom) {
  divCheckout.innerHTML = "<p>Nenhum bombom no carrinho</p>";
}

Object.entries(bombom).forEach(([sabor, quantidade]) => {
  if (quantidade > 0) {
    const elemento = document.createElement("p");
    elemento.textContent = `${
      sabor.charAt(0).toUpperCase() + sabor.slice(1)
    }: ${quantidade}`;
    divCheckout.appendChild(elemento);
    itensMostrados++;
  }
});

if (itensMostrados === 0) {
  divCheckout.innerHTML = "<p>Nenhum bombom no carrinho</p>";
} else {
  valorTotal = calcularValor(numeroBombom);
  localStorage.setItem("valorTotal", valorTotal);
  textoValorTotal.innerHTML = `<p id="textoValor">Total: R$${valorTotal.toFixed(
    2
  )}</p> `;
  divValorTotal.appendChild(textoValorTotal);
  textoFinalizar.innerHTML =
    '<a class="concluirPedido" href="/pages/submitName.html">Concluir pedido</a>';
  divFinalizar.appendChild(textoFinalizar);
}

// funções
function mostrarBombom() {
  console.log(bombom);
  console.log(typeof i);
  console.log(numeroBombom);
}

function restaurarLocalStorage(key) {
  return JSON.parse(localStorage.getItem(key));
}

function calcularValor(numeroBombom) {
  i = 0;
  while (numeroBombom > 0) {
    if (numeroBombom > 1) {
      i += 10;
      numeroBombom -= 2;
    } else {
      i += 6;
      numeroBombom -= 1;
    }
  }
  return i;
}
