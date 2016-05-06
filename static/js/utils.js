/* ==========================================================
 * ========================================================== */

 $(function () {
    $("#pagesize").val('20');
})

/* 全选全不选*/
$("#checkAll").click(function(){
    var num = $(":input[name=checkbox]:checked").length;
    $("[id*='inputCheckbox']").prop('checked',this.checked);
});


function show_change_passwd(){
    $('#change_passwd').modal('show')
}

//密码修改
function change_passwd_sumint(){
    $.post('/user/change_password/', {
        oldps: $('#oldps').val(),
        newps1: $('#newps1').val(),
        newps2: $('#newps2').val()
    }, function (e) {
        if(e == "ok"){
            $('#change_passwd').modal('hide')
        }else{
            alert(e)
        }
    });

}

//邮件地址修改
function mailserver(){
    $.post('/user/mail_server_index/', {
        action: 'get'
    }, function (e) {
        var words = e.split('|')
        $('#mailserver').val(words[0])
        $('#mailuser').val(words[1])
        $('#mailpasswd').val(words[2])
    });
    $('#exampleModal').modal('show')
}

//邮件地址修改
function save_mail_server(){
    $.post('/user/mail_server_index/', {
        action: 'post',
        mailserver:$('#mailserver').val(),
        mailuser:$('#mailuser').val(),
        mailpasswd:$('#mailpasswd').val()
    }, function (e) {
        if (e=="ok"){

        }else{
            alert(e)
        }
    });
    $('#exampleModal').modal('hide')
}


function checkReturn(){
    var flag = true;
    $(".require").each(function(i,n){
        var value = $(this).val();
        flag = typeof(value)!='undefined'&&value!='' ? true : false;
    });
    return flag
}

/* 获取当前选中订单 */
function del_batch(url){
    if (!confirm("确认要删除？")) {
        return false;
    }

    var chk_value = [];
    $("input[id*='inputCheckbox']:checked").each(function () {
        chk_value.push($(this).val())
    });
    if (chk_value.length != 0) {
        $.post(url, {
            pk: chk_value.join(",")
        }, function (e) {
            if (e == 'ok') {
                window.location.reload();
            } else {
                alert(e)
            }
        });
    }
}

/* 获取当前选中订单 */
function new_del_batch(url, tables){
    if (!confirm("确认要删除？")) {
        return false;
    }

    var chk_value = [];
    $("input[id*='inputCheckbox']:checked").each(function () {
        chk_value.push($(this).val())
    });
    if (chk_value.length != 0) {
        $.post(url, {
            pk: chk_value.join(","),
            tables: tables
        }, function (e) {
            if (e == 'ok') {
                window.location.reload();
            } else {
                alert(e)
            }
        });
    }
}

/* 批量暂停与开启 */
function stop_batch(status, url){
    if (!confirm("确认？")) {
        return false;
    }
    var chk_value = [];
    $("input[id*='inputCheckbox']:checked").each(function () {
        chk_value.push($(this).val())
    });
    if (chk_value.length != 0) {
        $.post(url, {
            pk: chk_value.join(","),
            status: status
        }, function (e) {
            if (e == 'ok') {
                window.location.reload();
            } else {
                alert(e)
            }
        });
    }
}

function del_user(id, url){
    if (!confirm("确认要删除？")) {
        return false;
    }
    $.post(url, {
        pk: id
    }, function (e) {
        if (e == 'ok') {
            $("#tr_id_" + id).hide()
        } else {
            alert(e)
        }
    });
}

function del_data(id, url, tables){
    if (!confirm("确认要删除？")) {
        return false;
    }
    $.post(url, {
        pk: id,
        tables:tables
    }, function (e) {
        if (e == 'ok') {
            $("#tr_id_" + id).hide()
        } else {
            alert(e)
        }
    });
}

function search_name(){
    var search  = $('#search').val()
    window.location.href = "?search=" + search;
}

function create_monitor_button(url){
    location.href = url;
}


function add_class(){
    alert("等待开通!")
}

function last_status(url){
    window.location.href = url+ "?status=1";

}

function pagesizeSelect(selObj){
    var selectd = selObj.options[selObj.selectedIndex].value;
    if (location.search == '' ){
        window.location.href = '?pagesize=' + selectd;
    }else{
        window.location.href = location.search+ '&pagesize=' + selectd;
    }
}

function one_stop_status(url, id, status){
    var contents=$("#one_stop_status_" + id).html();
    if (status == 'start'){
        $.post(url, {
            pk: id,
            status: 'yes'
        }, function (e) {
            if (e == 'ok') {
                $("#one_stop_status_" + id).empty().html("<a href=\"javascript:void(0);\" onclick=\"one_stop_status('" + url + "','"+ id + "','stop')\"> <li class=\"glyphicon glyphicon glyphicon-play\"></li></a>");
            } else {
            }
        });

    }else{
        $.post(url, {
            pk: id,
            status: 'no'
        }, function (e) {
            if (e == 'ok') {
                $("#one_stop_status_" + id).empty().html("<a href=\"javascript:void(0);\" onclick=\"one_stop_status('" + url + "','"+ id +"','start')\"> <li class=\"glyphicon glyphicon glyphicon-pause\"></li></a>");
            } else {
                alert(e)
            }
        });

    }
}

function get_code_id(ip){
    $.post('/geoip/get_ip_code/', {
        ip: $('#host_id').val()
    }, function (e) {
          $("#id_geoip").val(e)
    });
}




