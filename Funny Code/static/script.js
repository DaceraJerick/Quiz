let expression = '';

function append(char) {
    expression += char;
    document.getElementById('display').innerText = expression;
}

function clearDisplay() {
    expression = '';
    document.getElementById('display').innerText = '';
}

function calculate() {
    fetch('/calculate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ expression: expression })
    })
    .then(response => response.json())
    .then(data => {
        expression = data.result;
        document.getElementById('display').innerText = data.result;
    })
    .catch(error => console.error('Error:', error));
}
