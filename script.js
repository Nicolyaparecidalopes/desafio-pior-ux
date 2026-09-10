
function continuar() {
    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;
    const senha = document.getElementById("senha").value;

    if (nome === "" || email === "" || senha === "") {
        alert("Erro! Talvez esteja tudo certo, mas alguns campos parecem estar vazios.");
        return;
    }

    alert("Cadastro aparentemente concluído com sucesso... ou não.");
    window.location.href = "final.html";
}
