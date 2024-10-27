//Seleciona todos os corpos do menu
const listarItens = document.querySelectorAll(".corpo__listagem");

// Adiciona o evento "CLICK" em todos os itens
listarItens.forEach((rastreio) => {
    rastreio.addEventListener("click", () => {
        removerAbertoNav();
        const pegarIdMenu = buscarID(rastreio);
        adicionarAbertoNav(pegarIdMenu);
    });
});

function adicionarAbertoNav(pegarIdMenu) {
    const abrirNav = document.getElementById(pegarIdMenu);
    abrirNav.classList.add('aberta');
}

function removerAbertoNav() {
    const selecionarNavParaRemover = document.querySelector(".aberta");
    if (selecionarNavParaRemover) {
        selecionarNavParaRemover.classList.remove("aberta");
    }
}

// Função para buscar o ID do botão selecionado
function buscarID(rastreio) {
    return rastreio.attributes.id.value;
}
