$(document).ready(function(){
    $('.alert-warning').hide();
    $('.alert-success').hide();
});
    function validate(){
        var getname = document.getElementById("uname").value;
        var getpass = document.getElementById("upass").value;
        var emailcheck = /^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;
        var password = "shivam";
        if(getname == "" && getpass == "")
        {
            $('.alert-warning').text("Please enter the email & password");
            $('.alert-warning').show();
            return false;
        }
        if(getname != "")
        {
            if(getname.match(emailcheck))
            {
                if(getpass != "")
                {
                    if(getpass == password)
                    {
                        $('.alert-warning').hide();
                        $('.alert-success').text("Login Successfully");
                        $('.alert-success').show();      
                    }
                    else
                    {
                        $('.alert-warning').text("Incorrect password");
                        $('.alert-warning').show();
                        return false;
                    }
                }
                else
                {
                    $('.alert-warning').text("Please enter the password");
                    $('.alert-warning').show();
                    return false;
                }
            }
            else
            {
                $('.alert-warning').text("Incorrect email");
                $('.alert-warning').show();
                return false;
            }
        }
        else
        {
            $('.alert-warning').text("Please enter the email");
            $('.alert-warning').show();
            return false;
        }
    };
/*time and date */
       function startTime() {
        var today = new Date();
        var twoDigitMonth = ((today.getMonth().length+1) === 1)? (today.getMonth()+1) : '0' + (today.getMonth()+1);
        var currentDate = today.getDate() + "/" + twoDigitMonth + "/" + today.getFullYear();
        $('.dateshow').html("Date&nbsp;"+currentDate);
        var h = today.getHours();
        var m = today.getMinutes();
        var s = today.getSeconds();
        m = checkTime(m);
        s = checkTime(s);
       var time =  document.getElementById('timeshow').innerHTML =
       "Time&nbsp;" + h + ":" + m + ":" + s;
        var t = setTimeout(startTime, 500);
        var day = today.getDay();
        if(day == 0)
        {
            $('#day').html("Sunday");
        }
        if(day == 1)
        {
            $('#day').html("Monday");
        }
        if(day == 2)
        {
            $('#day').html("Tuesday");
        }
        if(day == 3)
        {
            $('#day').html("Wednesday");
        }
        if(day == 4)
        {
            $('#day').html("Thrusday");
        }
        if(day == 5)
        {
            $('#day').html("Friday");
        }
        if(day == 6)
        {
            $('#day').html("Saturday");
        }
      }
      function checkTime(i) {
        if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
        return i;
      }