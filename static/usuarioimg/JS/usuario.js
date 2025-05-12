// Simulando dados armazenados
let usuario = {
  nome: localStorage.getItem('nome') || 'Usuário Exemplo',
  email: localStorage.getItem('email') || 'usuario@exemplo.com',
  senha: localStorage.getItem('senha') || 'senha123'
};

// Atualizar a tela com os dados
document.getElementById('nomeUsuario').textContent = usuario.nome;
document.getElementById('emailUsuario').textContent = usuario.email;

function alterarUsuario() {
  const novoUsuario = prompt("Digite seu novo usuário:");
  if (novoUsuario) {
    usuario.nome = novoUsuario;
    localStorage.setItem('nome', novoUsuario);
    document.getElementById('nomeUsuario').textContent = novoUsuario;
    alert("Usuário alterado com sucesso!");
  }
}

function alterarEmail() {
  const novoEmail = prompt("Digite seu novo email:");
  if (novoEmail) {
    usuario.email = novoEmail;
    localStorage.setItem('email', novoEmail);
    document.getElementById('emailUsuario').textContent = novoEmail;
    alert("Email alterado com sucesso!");
  }
}

function alterarSenha() {
  const novaSenha = prompt("Digite sua nova senha:");
  if (novaSenha) {
    usuario.senha = novaSenha;
    localStorage.setItem('senha', novaSenha);
    alert("Senha alterada com sucesso!");
  }
}

function logout() {
  // Limpa os dados se quiser
  // localStorage.clear();

  // Redireciona para a página de login
  window.location.href = "login.html";
}
