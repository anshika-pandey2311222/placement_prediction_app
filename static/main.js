const btn = document.getElementById('predictBtn');
const resultEl = document.getElementById('result');

btn.addEventListener('click', async () => {
  const iq = document.getElementById('iq').value;
  const cgpa = document.getElementById('cgpa').value;
  resultEl.style.display = 'none';
  resultEl.textContent = '';

  try {
    const res = await fetch('/predict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ iq, cgpa })
    });

    const data = await res.json();
    if (!res.ok) throw new Error(data.error || 'Request failed');

    let html = `<strong>${data.message}</strong>`;
    if (data.probability !== null && data.probability !== undefined) {
      html += `<div>Probability: ${(data.probability*100).toFixed(1)}%</div>`;
    }
    resultEl.innerHTML = html;
    resultEl.style.display = 'block';
  } catch (err) {
    resultEl.innerHTML = `<span style='color:red'>Error: ${err.message}</span>`;
    resultEl.style.display = 'block';
  }
});
