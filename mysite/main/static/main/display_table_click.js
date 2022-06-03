
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
            
            function getCookie(name) {
                let cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    const cookies = document.cookie.split(';');
                    for (let i = 0; i < cookies.length; i++) {
                        const cookie = cookies[i].trim();
                        // Does this cookie string begin with the name we want?
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            const csrftoken = getCookie('csrftoken');

            id=$(this).data("delete-id");
            //alert("delete clicked: "+id); //testing ok.

            $.ajax({
                url: '/ajax/',
                type: "POST",
                data: {
                    id:id
                },
                beforeSend: function (xhr) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                },
                success: function (data) {
                    console.log(data);
                    location.reload(true)
                },
                error: function (error) {
                    console.log(error);
                }
            });

            /*fetch('/ajax') //get using fetch api
                .then(function(response){
                    return response.json();
                })
                .then(function(data){
                    //alert("data received: "+parsedResponse)
                    alert("testing ok: "+data.msg);
                    console.log(data);
                })
                .catch(function(err){
                    console.log(err);
                });*/
                /*$.ajax({ //jquery method get
                    url: '/ajax/',
                    success: function (data) {
                        console.log(data);
                        alert("testing: "+data.msg);
                    }
                });*/




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
