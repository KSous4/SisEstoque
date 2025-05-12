function abrirPagina(pagina) {
  switch (pagina) {
    case 'usuario':
      alert('Abrir tela de Usuário');
      break;
    case 'estoque':
      window.open('estoque.html', '_blank');
      break;
    case 'ordem':
      alert('Abrir tela de Ordem de Serviço');
      break;
  }
}
