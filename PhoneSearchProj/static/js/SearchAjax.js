<script>
    var append_increment = 0;
    $('#searchForm').submit(function(event) {
        $.ajax({
            type: "GET",
            url: {% url 'search_results' %},  // URL to your view that serves new info
            data: $('#searchForm').serialize(),
        })
        .done(function(response) {
            var table = $('#phoneResults');
            table.find("td").remove();
            table.append(response);
        });
    })
</script>