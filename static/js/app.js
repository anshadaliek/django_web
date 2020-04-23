function showSuccess(msg)
{
	alert(msg);
}

function showFailure(msg, errors)
{
	$.each(errors, function(i, err){
		msg += "\n"+err;
	});
	alert(msg);
}

function showLoading()
{	
	var html = "<div id='mzr_loading' style='background:#fff;position:fixed;top:0;bottom:0;left:0;right:0;z-index:9999;opacity:.7;font-size:100px;' ><table style='width:100%;height:100%;' ><tr><td style='text-align:center;vertical-align:middle'><i class='fa fa-spinner fa-spin' ></i></td></tr></table></div>";
	$('body').append(html);	
}
function hideLoading()
{
	$("#mzr_loading").remove();
}
$(document).ajaxStart(function(){
	showLoading();
});
$(document).ajaxComplete(function(){
	hideLoading();
});