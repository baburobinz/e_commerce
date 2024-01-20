$(document).ready(function(){

// function to show message asper the response
    function add_message(msg){
        msg_container = $('.message_container')
        msg_container.text(msg)
        msg_container.css({
            'opacity':1,
            
        })
        if(msg=='Registration Success'){
            msg_container.removeClass('error_message')
            msg_container.addClass('success_message')
        }

        else{
            msg_container.removeClass('success_message')
            msg_container.addClass('error_message')
        }
       
        setTimeout(function(){
            msg_container.css({
               'opacity':0
            })
        },2000)

    }

    // form submission regiter and login

    $('.form').submit(function(e){
        e.preventDefault()
        check_form = $(this).children(':nth-child(2)').attr('name')
        if(check_form=='register'){
            url = 'registration'
        }
        else if(check_form=='login'){
            url = 'login' 
        }  
        data = $(this).serialize()
        $.ajax({
            url:url,
            method:'POST',
            data:data,
            success:function(response){
                message = response.message;
                home_url = response.url

                if(message){
                    add_message(message)  
                }

                if(home_url){
                    window.location.href=indexUrl
                }
                    
            },
            error:function(error){
                console.log('ajx error : ',error)
            }
        })
    })
})