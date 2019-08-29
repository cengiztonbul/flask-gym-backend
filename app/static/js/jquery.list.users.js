$jq = jQuery.noConflict()


var users_header_row =
    `
    <thead>
        <tr>
            <th> AD </th>
            <th> SOYAD </th>
        </tr>
    </thead>
`


var user_list =
    [
        {
            "first_name": "test_name_0",
            "last_name": "test_lname_0",
            "id": "0",
        },
        {
            "first_name": "test_name_1",
            "last_name": "test_lname_1",
            "id": "1",
        },
        {
            "first_name": "test_name_2",
            "last_name": "test_lname_2",
            "id": "2",
        }
    ]



function create_row(user) {
    result =
        `
        <tbody id="${user.id}" class="user-row" >
            <tr>
                <td> ${user.first_name} </td>
                <td> ${user.last_name} </td>
            </tr>
        </tbody>
        `
    return result;
}


function fill_table(user_list)
{
    $jq("#user-list").append(create_table(user_list))
}



function create_table(user_list)
{
    result = `<table>`;
    result += users_header_row;
    
    for(user in user_list)
    {
        result += create_row(user_list[user]);
    }

    result += `</table>`;

    return result;
}


$jq().ready(function()
{
    $jq.get("/test/student_list", function(data)
    {
        // console.log(data);
        fill_table($jq.parseJSON(data));
    });
});

$jq(".user-row").live("click", function () 
{
    console.log($jq(this).attr("id"));
    id = $jq(this).attr("id")
    window.location.href = "/test/edit_profile?user_id=" + $jq(this).attr("id")
});

