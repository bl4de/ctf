document.addEventListener('DOMContentLoaded', function() {
    const [_, query] = [window.location, QueryArg.parseQuery(window.location.search)];
    const { note: n } = query;

    const actions = [
        () => console.debug(n), 
        () => {
            const el = document.getElementById('notesPlaceholder');
            if (n) {
                const renderNote = txt => `<div class="note-item">${sanitizeHtml(txt)}</div>`;
                el.innerHTML += renderNote(n);
            }
        }
    ];

    actions.forEach(fn => fn());
});