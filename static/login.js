document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
  
    loginForm.addEventListener('submit', async (e) => {
      e.preventDefault();
  
      const email = document.getElementById('email').value;
      const senha = document.getElementById('senha').value;
  
      try {
        const response = await fetch('http://localhost:3000/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ email, senha }),
        });
  
        if (!response.ok) {
          throw new Error('Login falhou');
        }
  
        const data = await response.json();
        console.log('Login bem-sucedido:', data);
  
  
        //alert(Bem-vindo(a), ${data.nome || 'usuário'});
  
  
      } catch (error) {
        console.error('Erro ao fazer login:', error);
        alert('Email ou senha inválidos!');
      }
    });
  });