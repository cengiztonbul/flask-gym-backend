
$jq = jQuery.noConflict();

$jq(document).ready(function ($) {
});

$jq("#workout-button").click(function () {
    console.log($jq("#table-title").html());
    $jq("#table-title").html("ÇALIŞMA PROGRAMI");
    $jq.get("/get_test_data", function(data) 
    {
        console.log(data);
            fill_workout(data);
    });
});


$jq("#supplement-button").click(function () {
    console.log($jq("#table-title").html());
    $jq("#table-title").html("SUPPLEMENT PROGRAMI");

});


function create_workout_table_row(name, body_parts, sets, reps, duration) {
    result =
        `
    <tbody>
        <tr>
            <td> ${name} </td>
            <td> ${body_parts} </td>
            <td> ${sets} </td>
            <td> ${reps} </td>
            <td> ${duration} </td>
        </tr>
    </tbody>
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
        result += create_workout_table_row(day[exercise].name, body_parts_to_string(day[exercise].body_parts), day[exercise].sets, day[exercise].reps, day[exercise].duration);
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
            <th style="width:8%"> SÜRE </th>
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


// create jquery script
// feed with json
// 

/*
                            <table>
                                <thead>
                                    <tr>
                                        <th style="width:30%"> İSİM </th>
                                        <th style=""> BÖLGE </th>
                                        <th style="width:8%"> SÜRE </th>
                                        <th style="width:8%"> SET </th>
                                        <th style="width:8%"> TEKRAR </th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td> Deadlift </td>
                                        <td> Back, Leg, Arm</td>
                                        <td>-</td>
                                        <td>2</td>
                                        <td>25</td>
                                    </tr>
                                    <tr>
                                        <td>Item #2</td>
                                        <td>Desc</td>
                                        <td>Discount:</td>
                                        <td>$2.00</td>
                                        <td>$1.08</td>
                                    </tr>
                                    <tr>
                                        <td>Item #3</td>
                                        <td>Desc</td>
                                        <td>Shipping:</td>
                                        <td>$3.00</td>
                                        <td>$2.50</td>
                                    </tr>
                                    <tr>
                                        <td>Item #4</td>
                                        <td>Desc</td>
                                        <td>Tax:</td>
                                        <td>$4.00</td>
                                        <td>$3.00</td>
                                    </tr>
                                    <tr>
                                        <td><strong>All</strong></td>
                                        <td><strong>Desc</strong></td>
                                        <td><strong>Total:</strong></td>
                                        <td><strong>$10.00</strong></td>
                                        <td><strong>$9.00</strong></td>
                                    </tr>
                                </tbody>
							</table>

*/

