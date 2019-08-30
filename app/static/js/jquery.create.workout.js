$jq = jQuery.noConflict();

exercises = ["test0", "test1", "test2", "test3", "test4"];

var workouts =
    [
        "name0",
        "name1",
        "name2",
        "name3",
        "name4"
    ]

var workout_header_row = `
    <thead>
        <tr>
            <th> İSİM </th>
            <th style="width:15%"> SET </th>
            <th style="width:15%"> TEKRAR </th>
            <th style="width:8%"> SİL </th>
        </tr>
    </thead>

`;

function create_workout_day_table(id) {
    var result = `<div class="create-panel" id=${id}>`
    result += `<table class="create-panel-table" id=${id}>`
    result += workout_header_row

    result += "</table>"
    result += `
    <div class="add-exercise-button" id="${id}">
        <a id="add-exercise-button" class="dt-sc-button medium first" data-hover="SUPPLEMENT">ADD EXERCISE </a>
    </div>
    <div class="delete-day-button" id="${id}">
        <a id="delete-day-button" class="dt-sc-button medium" data-hover="SUPPLEMENT">DELETE DAY </a>
    </div>
    <div class="dt-sc-hr-invisible-medium"></div>
    `
    result += "</div>"
    return result;
}

$jq(document).ready(function()
{    $jq.get("/data/exercises", function(data)
    {
        console.log(data);
        exercises = $jq.parseJSON(data)
    });
})

function create_options() {
    var result = `<select name="cmbsubject" class="valid">`;

    for (exercise in exercises) {
        result += `
            <option value="${exercises[exercise].id}">${exercises[exercise].name}</option>
        `; 
    }

    result += "</select>";

    return result;
}


function create_row() {
    result = `
    <tbody>
        <tr>
            <td> ${create_options()} </td>
            <td> ${`<input id="set" type="text" name="txtname" placeholder="SET" required="">`} </td>
            <td> ${`<input id="reps" type="text" name="txtname" placeholder="TEKRAR" required="">`} </td>
            <td> ${`<a id="delete-button" class="dt-sc-button small danger bordered" data-hover="Delete"> <i class="fa fa-times-circle"> </i> Delete </a>`} </td>
        </tr>
    </tbody>
    `;

    return result;
}


$jq("#delete-button").live("click", function () {
    $jq(this).parent().parent().parent().remove();
});


$jq(".add-exercise-button").live("click", function () {
    $jq("#" + $jq(this).attr("id") + ".create-panel-table").append(create_row());

});
var id = 0;

$jq(".add-day-button").live("click", function () {
    id += 1;
    $jq(".workout-tables").append(create_workout_day_table(id));
});


$jq(".delete-day-button").live("click", function () {
    $jq("#" + $jq(this).attr("id") + ".create-panel").remove();

});

$jq.fn.postJSON = function(url, data) {
    return $jq.ajax({
            type: 'POST',
            url: url,
            data: data,
            contentType: "application/json; charset=utf-8",
            dataType: "json",
        });
    }


$jq("#post-button").live("click", function () {
    var workout = {"name": "null", "user_id": null, days: []}
    workout.user_id = getUrlParameter("user_id");

    $jq(".create-panel-table").each(function () {
        var day = []
        $jq(this).find("tbody").each(function () {
            day.push(table_to_json($jq(this)));
        });
        workout.days.push(day);

    }
    )
    workout.name = $jq("#workout-name").val();
    console.log(JSON.stringify(workout));
    $jq.fn.postJSON("/workout", JSON.stringify(workout));
});


function table_to_json(table) {
    return { "exercise": table.find("option:selected").val(), "sets": table.find("#set").val(), "reps": table.find("#reps").val() };
}



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
