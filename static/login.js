document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('loginForm');

  loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const email = document.getElementById('email').value;
    const senha = document.getElementById('senha').value;

    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    const raw = JSON.stringify({
      "email": email,
      "passwd": senha
    });

    const requestOptions = {
      method: "POST",
      headers: myHeaders,
      body: raw,
      redirect: "follow"
    };

    try {
      const response = await fetch("http://localhost:3000/login", requestOptions);
      const result = await response.text();

      if (response.ok) {
        window.location.href = "http://localhost:3000/home";
      } else {
        console.log('Login falhou:', result);
      }
    } catch (error) {
      console.log('Erro ao fazer login:', error);
    }
  });
});
