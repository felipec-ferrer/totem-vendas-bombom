const bombom = JSON.parse(localStorage.getItem("bombom"));
const nomeCliente = localStorage.getItem("nomeCliente");
const valorTotal = localStorage.getItem("valorTotal");

if (bombom && nomeCliente && valorTotal) {
  fetch("http://localhost:5000/realizarPedidos", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      nomeCliente: nomeCliente,
      bombom: bombom,
      valorTotal: valorTotal,
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      console.log("Resposta do servidor:", data);

      localStorage.removeItem("bombom");
      localStorage.removeItem("nomeCliente");
      localStorage.removeItem("valorTotal");
      localStorage.removeItem("estoque");
    });
}
