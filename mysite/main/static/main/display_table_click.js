
    $('#display-table > tbody > tr').click(function() {
        //alert("you are being redirected to id: "+$(this).data("display-table-id"))
        //window.location =("/id/"+$(this).data("display-table-id"));
        //alert("testing id : "+$(this).data("display-table-id"));
        if($(this).data("display-table-id")){
            //alert("testing display id");
            $('.dataid'+$(this).data("display-table-id")).collapse('toggle');
        }
        else if($(this).data("show-id")){
            window.location =("/id/"+$(this).data("show-id"));
            //alert("show clicked: "+$(this).data("show-id"));
        }
        else if($(this).data("delete-id")){
            
            id=$(this).data("delete-id");
            alert("delete clicked: "+id);
            
            /*$.ajax({
                type: "POST",
                url: "http://192.168.68.138:8000/delete/",
                data: { id: id },
                beforeSend: function(xhr) {
                    xhr.setRequestHeader('X-CSRF-Token', getCSRFTokenValue());
                }
           });*/
            /*$.ajax({
                url: "{% url 'delete' %}",
                data: { 'id' : id },
                beforeSend: function(xhr) {
                    xhr.setRequestHeader("X-CSRFToken", "{{% csrf_token %}}" );
                },
                success: function(response){
                }
            });*/

        }
        
         
    });
