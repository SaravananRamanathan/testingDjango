
    $('#display-table > tbody > tr').click(function() {
        //alert("you are being redirected to id: "+$(this).data("display-table-id"))
        //window.location =("/id/"+$(this).data("display-table-id"));
        //alert("testing id : "+$(this).data("display-table-id"));
        $('.dataid'+$(this).data("display-table-id")).collapse('toggle');
        
    });