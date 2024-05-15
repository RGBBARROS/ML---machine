document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('creditForm');
    const resultDiv = document.getElementById('result');
    const loadingDiv = document.getElementById('loading'); // Adicionando a referência à div de loading

    form.addEventListener('submit', async function (e) {
        e.preventDefault();
        const formData = new FormData(form);
        const jsonData = {};
        formData.forEach((value, key) => {
            jsonData[key] = value;
        });

        try {
            loadingDiv.classList.remove('hidden'); // Mostrando a div de loading

            const response = await fetch('/analise', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(jsonData)
            });

            const data = await response.json();
            resultDiv.textContent = `Resultado: ${data.resultado}`;
            resultDiv.classList.remove('hidden'); // Mostra o resultado
            loadingDiv.classList.add('hidden'); // Esconde a div de loading após a análise
        } catch (error) {
            console.error('Erro ao enviar a solicitação:', error); // Corrigido o console.error para exibir a mensagem correta
        }
    });
});
