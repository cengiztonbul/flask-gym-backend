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



function create_options() {
    var result = `<select name="cmbsubject" class="valid">`;

    for (exercise in exercises) {
        result += `
            <option value="${exercises[exercise]}">${exercises[exercise]}</option>
        `; // value will be replaced by exercise id
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


$jq("#post-button").live("click", function () {
    var days =
        [

        ]

    $jq(".create-panel-table").each(function () {
        var day = []
        $jq(this).find("tbody").each(function () {
            day.push(table_to_json($jq(this)));
        });
        days.push(day);

    }
    )
    console.log(days);

});


function table_to_json(table) {
    return { "exercise": table.find("option:selected").val(), "sets": table.find("#set").val(), "reps": table.find("#reps").val() };
}


/*
    0. a workout object

    1. add exercise
        a. create a new row
        b. add the row to the workout object
    2. add day
        a. clear the table
        b. add a new array to the workout object
        c. create a new table
    3. delete exercise
        a. click on the button next to it
        b. remove from the array
        c. clear the row
    4. delete day
        a. clear the table
        b. view another day
        c. remove from the array
    5. view the previous/next day
        a. keep track of current index
        b. clear the table
        c. get the other day's data
        d. fill the values with the data
    6. finish the program
        a. post the workout object
*/


/*
    1. add day will add a new table with the id of the day button
*/


/*
    day table
        table
        add exercise
        delete day
*/