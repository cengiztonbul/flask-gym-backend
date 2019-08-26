from flask import jsonify


def test_get_workout():
    return jsonify(workout_data)


def test_get_diet():
    return jsonify(diet_data)


workout_data = {
    "name": "test_name",
    "days": [
        [  # day
            {  # exercise
                "name": "test",
                "body_parts":
                    [
                        "back", "leg"
                    ],
                "sets": 4,
                "reps": 12,
                "duration": "-"
            },
            {  # exercise
                "name": "test1",
                "body_parts":
                    [
                        "back", "chest"
                    ],
                "sets": 4,
                "reps": 12,
                "duration": "-"
            },
            {  # exercise
                "name": "test2",
                "body_parts":
                    [
                        "chest", "leg"
                    ],
                "sets": 3,
                "reps": 10,
                "duration": "-"
            },
        ],
        [  # day
            {  # exercise
                "name": "test3",
                "body_parts":
                    [
                        "back", "leg"
                    ],
                "sets": 4,
                "reps": 12,
                "duration": "-"
            },
            {  # exercise
                "name": "test4",
                "body_parts":
                    [
                        "back", "leg"
                    ],
                "sets": 4,
                "reps": 12,
                "duration": "-"
            },
            {  # exercise
                "name": "test5",
                "body_parts":
                    [
                        "back", "arm"
                    ],
                "sets": 2,
                "reps": 25,
                "duration": "-"
            },
        ]
    ]
}

diet_data = {
    "diet":
    [
        [ # day 1
            [ # meal 1
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
            [ # meal 1
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
            [ # meal 1
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


