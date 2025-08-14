const outrosCheckbox1 = document.getElementById('outrosCheck1');
const outrosTextoDiv1 = document.getElementById('outrosTextoDiv1');

outrosCheckbox1.addEventListener('change', () => {
    outrosTextoDiv1.style.display = outrosCheckbox1.checked ? 'block' : 'none';
});

const outrosCheckbox2 = document.getElementById('outrosCheck2');
const outrosTextoDiv2 = document.getElementById('outrosTextoDiv2');

outrosCheckbox2.addEventListener('change', () => {
    outrosTextoDiv2.style.display = outrosCheckbox2.checked ? 'block' : 'none';
});