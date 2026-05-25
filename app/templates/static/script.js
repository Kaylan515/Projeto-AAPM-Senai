document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');

    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            // Evita o comportamento padrão de recarregar a página ao clicar em "Entrar"
            event.preventDefault();

            // Captura os valores digitados nos inputs
            const email = document.getElementById('email').value.trim();
            const nome = document.getElementById('nome').value.trim();
            const senha = document.getElementById('senha').value;

            // Cria o objeto com os dados obtidos
            const dadosLogin = {
                email: email,
                nome: nome,
                senha: senha
            };

            console.log('Tentando fazer login com os dados:', dadosLogin);

            try {
                // Prepara a requisição para a sua rota de autenticação do FastAPI
                // OBS: Ajuste a URL '/auth/login' caso sua rota tenha outro nome
                const response = await fetch('/auth/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(dadosLogin)
                });

                if (response.ok) {
                    const resultado = await response.json();
                    alert('Login realizado com sucesso!');
                    
                    // Redireciona o usuário para o dashboard do sistema
                    window.location.href = '/dashboard'; 
                } else {
                    const erro = await response.json();
                    alert(`Erro ao entrar: ${erro.detail || 'Credenciais inválidas.'}`);
                }

            } catch (error) {
                console.error('Erro na comunicação com o servidor:', error);
                alert('Não foi possível conectar ao servidor. Verifique se o FastAPI está rodando!');
            }
        });
    }
});
// login