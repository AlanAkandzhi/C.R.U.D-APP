document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('add-form');
    const recordList = document.getElementById('record-list');
    const apiUrl = 'http://127.0.0.1:5000/records';
    async function loadRecords() {

        const response = await fetch(apiUrl);
        const records = await response.json();
        recordList.innerHTML = '';
        records.forEach(record => {
            const li = document.createElement('li');
            li.textContent = record;
            recordList.appendChild(li);
        });
    }
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const newRecord = document.getElementById('new-record').value.trim();
        if (!newRecord) return;

        await fetch(apiUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ record: newRecord })
        });

        document.getElementById('new-record').value = '';
        loadRecords();
    });

    document.getElementById('clear-records').addEventListener('click', async () => {
        await fetch(apiUrl, {
            method: 'DELETE',
        });

        loadRecords();
    });

    loadRecords();
});
