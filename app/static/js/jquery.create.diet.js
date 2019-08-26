$jq = jQuery.noConflict();

food_list = ["test0", "test1", "test2", "test3", "test4"];

var workouts =
    [
        "name0",
        "name1",
        "name2",
        "name3",
        "name4"
    ]

var diet_header_row = `
    <thead>
        <tr>
            <th> İSİM </th>
            <th style="width:15%"> PORSİYON </th>
            <th style="width:8%"> SİL </th>
        </tr>
    </thead>

`;

function create_diet_day_table(id) {
    var result = `<div class="create-panel" id=${id}>`
    result += `<table class="create-panel-table" id=${id}>`
    result += diet_header_row

    result += "</table>"
    result += `
    <div class="add-food-button" id="${id}">
        <a id="add-food-button" class="dt-sc-button medium first" data-hover="SUPPLEMENT">ADD FOOD </a>
    </div>
    <div class="add-meal-button" id="${id}">
    <a id="add-meal-button" class="dt-sc-button medium" data-hover="SUPPLEMENT">ADD MEAL </a>
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

    for (food in food_list) {
        result += `
            <option value="${food_list[food]}">${food_list[food]}</option>
        `; // value will be replaced by food id
    }

    result += "</select>";

    return result;
}


function create_row() {
    var result = `
    <tbody>
        <tr>
            <td> ${create_options()} </td>
            <td> ${`<input id="set" type="text" name="txtname" placeholder="PORSİYON" required="">`} </td>
            <td> ${`<a id="delete-button" class="dt-sc-button small danger bordered" data-hover="Delete"> <i class="fa fa-times-circle"> </i> Delete </a>`} </td>
        </tr>
    </tbody>
    `;

    return result;
}

function meal_row() {
    var result =
        `    <tbody id="meal-row">
            <tr>
                <td colspan="2"> ${`<input id="meal" type="text" name="txtname" placeholder="ÖĞÜN ADI" required="">`} </td>
                <td> ${`<a id="delete-button" class="dt-sc-button small danger bordered" data-hover="Delete"> <i class="fa fa-times-circle"> </i> Delete </a>`} </td>
            </tr>
        </tbody>`
    return result;
}

$jq("#delete-button").live("click", function () {
    $jq(this).parent().parent().parent().remove();
});


$jq(".add-food-button").live("click", function () {
    console.log("clicked");
    $jq("#" + $jq(this).attr("id") + ".create-panel-table").append(create_row());

});
var id = 0;

$jq(".add-day-button").live("click", function () {
    id += 1;
    $jq(".workout-tables").append(create_diet_day_table(id));
});
$jq(".add-meal-button").live("click", function () {
    $jq("#" + $jq(this).attr("id") + ".create-panel-table").append(meal_row());
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
        var meal = []

        $jq(this).find("tbody").each(function () {
            if ($jq(this).attr("id") != null && $jq(this).attr("id") == "meal-row") {
                console.log("found a meal row");
                if (meal.length != 0) {
                    day.push(meal);
                    meal = [];
                }
            }
            else {
                console.log("there is food here");
                meal.push(table_to_json($jq(this)));
            }
        });
        day.push(meal);
        days.push(day);

    }
    )
    console.log(days);

});


function table_to_json(table) {
    return { "food": table.find("option:selected").val(), "portion": table.find("#portion").val() };
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