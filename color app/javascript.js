function getData(){
    var apiCall= 'http://127.0.0.1:5001/';
    $.getJSON(apiCall, coinData);
function coinData(cData){
    for (x=0; x < cData.length; x++){  
    var name = cData[x].COIN;
    var date = cData[x].DATE;
    var url = cData[x].URL;
    
    $('#content').append("<tr>"+"<th>"+'<input type="radio" name="coin_name" value='+x+'>'+"</th>"+"<th>"+name+"</th>"+"<th>"+date+"</th>"+"<th>" +url+"</th>"+"</tr>");
    }
}    
}

function refresh(){
    location.reload();  
}
function delete_coin(){
    var radios = document.getElementsByName('coin_name');
    var form = $('<form></form>');
    var password = document.getElementsByName("password");
    var passFeild = $("<input></input>");
    passFeild.attr("name", "password");
    passFeild.attr("value", password[0].value);
    form.append(passFeild);
    var index = 0;
    for (var i = 0, length = radios.length; i < length; i++){
    if (radios[i].checked){
        index = radios[i].value;
 }
}
    var testField = $("<input></input>");
    testField.attr("name","line");
    testField.attr("value", index);
    form.append(testField);
    form.attr("method", "post");
    form.attr("action", "http://127.0.0.1:5001/delete");
    $(document.body).append(form);
    $.getJSON(form.submit(), jsonData);
    function jsonData(Data){
        var route = Data[0].message;
        console.log(route)
        if (route === "Success"){
            $("#body_content").load("win.html");
        }

    }


}

function error(){
    window.open ('file:///C:/Users/Admin/Dropbox/My%20Programs/Python%20Programs/Coin%20widget/coinwidget.html');
}

function success(){
    window.open ('file:///C:/Users/Admin/Dropbox/My%20Programs/Python%20Programs/Coin%20widget/coinwidget.html');
}

