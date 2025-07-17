fetch("http://localhost:5000/carregarEstoque")
  .then((res) => res.json())
  .then((estoque) => {
    localStorage.setItem("estoque", JSON.stringify(estoque));
    console.log("Estoque recebido: ", estoque);
  });
