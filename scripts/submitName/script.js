document.getElementById("formCliente").addEventListener("submit", function (e) {
  e.preventDefault();

  const nome = document.getElementById("nome").value;

  if (nome.length === 0) {
    alert("Por favor, insira seu nome para continuar");
  } else {
    localStorage.setItem("nomeCliente", nome);
    window.location.href = "sucess.html";
  }
});

document.addEventListener("DOMContentLoaded", () => {
  const Keyboard = window.SimpleKeyboard.default;

  const myKeyboard = new Keyboard({
    onChange: (input) => {
      document.getElementById("nome").value = input;
    },
    onKeyPress: (button) => {
      console.log("Botão pressionado", button);
    },
  });

  document.getElementById("nome").addEventListener("input", (event) => {
    myKeyboard.setInput(event.target.value);
  });
});
