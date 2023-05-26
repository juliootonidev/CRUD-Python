function exibirAlerta() {
    alert("Esta é uma mensagem de alerta!");
}

function disableSelectedDate(selectElement) {
    var selectedOption = selectElement.options[selectElement.selectedIndex];
    selectedOption.disabled = true;
  }