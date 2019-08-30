$jq = jQuery.noConflict()


$jq("#workout-button").click(function() {
    redirect_with_id("/test/workout")
}
)

$jq("#diet-button").click(function() {
    redirect_with_id("/test/diet")
}
)


$jq("#supplement-button").click(function() {
    redirect_with_id("/test/supplement")
}
)

$jq("#posture-button").click(function() {
    redirect_with_id("/test/posture")
}
)

$jq("#trainer-button").click(function() {
    redirect_with_id("/test/trainer")
}
)

$jq("#delete-button").click(function() {
    redirect_with_id("/test/delete_user")
}
)

var getUrlParameter = function getUrlParameter(sParam) {
    var sPageURL = window.location.search.substring(1),
        sURLVariables = sPageURL.split('&'),
        sParameterName,
        i;

    for (i = 0; i < sURLVariables.length; i++) {
        sParameterName = sURLVariables[i].split('=');

        if (sParameterName[0] === sParam) {
            return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
        }
    }
};

function redirect_with_id(link)
{
    window.location.href = link + "?user_id=" + getUrlParameter("user_id")
}