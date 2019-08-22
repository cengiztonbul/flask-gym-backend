var y = 
{
    "diet": 
    [
        [ // day 1
            [ // meal 1
                {
                    "name": "test_food_0",
                    "cal" : "test_cal_0",
                    "ingredients":
                    [
                        "yağ",
                    ]
                },
                {
                    "name": "test_food_1",
                    "cal" : "test_cal_1",
                    "ingredients":
                    [
                        "karbonhidrat",
                    ]
                },
                {
                    "name": "test_food_2",
                    "cal" : "test_cal_2",
                    "ingredients":
                    [
                        "protein",
                    ]
                }
            ],
            [ // meal 1
                {
                    "name": "test_food_0",
                    "cal" : "test_cal_0",
                    "ingredients":
                    [
                        "yağ",
                    ]
                },
                {
                    "name": "test_food_1",
                    "cal" : "test_cal_1",
                    "ingredients":
                    [
                        "karbonhidrat",
                    ]
                },
                {
                    "name": "test_food_2",
                    "cal" : "test_cal_2",
                    "ingredients":
                    [
                        "protein",
                    ]
                }
            ]

        ],
        [
            [ // meal 1
                {
                    "name": "test_food_3",
                    "cal" : "test_cal_3",
                    "ingredients":
                    [
                        "protein",
                    ]
                },
                {
                    "name": "test_food_4",
                    "cal" : "test_cal_4",
                    "ingredients":
                    [
                        "yağ",
                    ]
                },
                {
                    "name": "test_food_5",
                    "cal" : "test_cal_5",
                    "ingredients":
                    [
                        "protein",
                    ]
                }
            ]
        ]
        
    ]
}


var diet_header_row = 
`
    <thead>
        <tr>
            <th style="width:30%"> İSİM </th>
            <th style=""> İÇERİK </th>
            <th style="width:8%"> KALORİ </th>
        </tr>
    </thead>
`


$jq = jQuery.noConflict()



$jq("#diet-button").click(function()
{
    $jq("#table-title").html("DİYET PROGRAMI");
    fill_diet(y);
});


function create_diet_table_row(name, ingredients, cal)
{
    result =
    `
    <tbody>
        <tr>
            <td> ${name} </td>
            <td> ${ingredients} </td>
            <td> ${cal} </td>
        </tr>
    </tbody>
    `
    return result;
}


function ingredients_to_string(ingredients)
{
    var result = "";
    
    for(ingredient in ingredients)
    {
        result += ingredients[ingredient] + " "; // might be ingredients.name in the future 
    }

    return result;
}


function meal_to_table(meal)
{
    var result = "";
    for(food in meal)
    {
        result += create_diet_table_row(meal[food].name, ingredients_to_string(meal[food].ingredients), meal[food].cal);
        
    }
    return result;
}


function create_diet_day_table(day)
{
    var result = "<table>"
    result += diet_header_row
    for(meal in day)
    {
        result += `<td colspan="3">${meal}</td>`
        result += meal_to_table(day[meal]);
    }
    result += "</table>"

    return result;
}

function fill_diet(diet)
{
    $jq(".workout-tables").html("");
    for(day in diet.diet)
    {
        console.log(diet.diet[day]);
        $jq(".workout-tables").append(create_diet_day_table(diet.diet[day]));
        
    }

}
