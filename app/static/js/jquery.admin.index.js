$jq = jQuery.noConflict()


$jq("#student-list-button").click(function() {
    redirect("/students")
}
)

function redirect(link)
{
    window.location.href = link
}