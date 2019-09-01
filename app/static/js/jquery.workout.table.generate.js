
$jq = jQuery.noConflict();

$jq(document).ready(function ($) {
});

$jq("#workout-button").click(function () {
    console.log($jq("#table-title").html());
    $jq("#table-title").html("ÇALIŞMA PROGRAMI");
    $jq.get("/data/workout", function (data) {
        console.log($jq.parseJSON(data));

        fill_workout($jq.parseJSON(data));
    });
});


$jq("#supplement-button").click(function () {
    console.log($jq("#table-title").html());
    $jq("#table-title").html("SUPPLEMENT PROGRAMI");

});


function create_workout_table_row(name, body_parts, sets, reps) {
    result =
        `
        <a>
    <tbody>
        <tr>
            <td> ${name} </td>
            <td> ${body_parts} </td>
            <td> ${sets} </td>
            <td> ${reps} </td>
        </tr>
    </tbody>
    </a>
    `
    return result;
}


function body_parts_to_string(body_parts_array) {
    var result = "";

    for (part in body_parts_array) {
        result += body_parts_array[part] + " "; // might be part.name in the future 
    }

    return result;
}


function create_workout_day_table(day) {
    var result = "<table>"
    result += workout_header_row
    for (exercise in day) {
        exercise_template = get_exercise_data(day[exercise].exercise_id.$oid)
        console.log(exercise_template)
        result += create_workout_table_row(exercise_template.name, body_parts_to_string(day[exercise].body_parts), day[exercise].sets, day[exercise].reps);
    }
    result += "</table>"

    return result;
}


var workout_header_row = `
    <thead>
        <tr>
            <th style="width:30%"> İSİM </th>
            <th style=""> BÖLGE </th>
            <th style="width:8%"> SET </th>
            <th style="width:8%"> TEKRAR </th>
        </tr>
    </thead>

`


function fill_workout(workout) {
    $jq(".workout-tables").html("");
    for (day in workout.days) {
        console.log(workout.days[day]);
        $jq(".workout-tables").append(create_workout_day_table(workout.days[day]));

    }

}


function get_exercise_data(id) {
    var result_data = ""
    $jq.ajax({
        type: "GET",
        url: "/data/exercise?exercise_id=" + id,
        async: false,
        success: function (data) { result_data = $jq.parseJSON(data) }
    });

    return result_data;
}
