from flask import jsonify


def test_get_workout():
    return jsonify(workout_data)


def test_get_diet():
    return jsonify(diet)


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

diet = [
    [
        {  # meal 1
            "name": "meal_0",
            "food_list":
                [
                    {
                        "name": "test_food_3",
                        "cal": "test_cal_3",
                        "ingredients":
                            [
                                "protein",
                            ]
                    },
                    {
                        "name": "test_food_4",
                        "cal": "test_cal_4",
                        "ingredients":
                            [
                                "yağ",
                            ]
                    },
                    {
                        "name": "test_food_5",
                        "cal": "test_cal_5",
                        "ingredients":
                            [
                                "protein",
                            ]
                    }
                ]
        },
        {  # meal 1
            "name": "meal_1",
            "food_list":
                [
                    {
                        "name": "test_food_3",
                        "cal": "test_cal_3",
                        "ingredients":
                            [
                                "protein",
                            ]
                    },
                    {
                        "name": "test_food_4",
                        "cal": "test_cal_4",
                        "ingredients":
                            [
                                "yağ",
                            ]
                    },
                    {
                        "name": "test_food_5",
                        "cal": "test_cal_5",
                        "ingredients":
                            [
                                "protein",
                            ]
                    }
                ]
        },
        {  # meal 1
            "name": "meal_2",
            "food_list":
                [
                    {
                        "name": "test_food_3",
                        "cal": "test_cal_3",
                        "ingredients":
                            [
                                "protein",
                            ]
                    },
                    {
                        "name": "test_food_4",
                        "cal": "test_cal_4",
                        "ingredients":
                            [
                                "yağ",
                            ]
                    },
                    {
                        "name": "test_food_5",
                        "cal": "test_cal_5",
                        "ingredients":
                            [
                                "yağ",
                            ]
                    }
                ]
        }

    ],
    [
        {  # meal 1
            "name": "meal_0",
            "food_list":
                [
                    {
                        "name": "test_food_13",
                        "cal": "test_cal_13",
                        "ingredients":
                            [
                                "protein",
                            ]
                    },
                    {
                        "name": "test_food_14",
                        "cal": "test_cal_4",
                        "ingredients":
                            [
                                "yağ",
                            ]
                    },
                    {
                        "name": "test_food_5",
                        "cal": "test_cal_5",
                        "ingredients":
                            [
                                "protein",
                            ]
                    }
                ]
        },
        {  # meal 1
            "name": "meal_1",
            "food_list":
                [
                    {
                        "name": "test_food_3",
                        "cal": "test_cal_3",
                        "ingredients":
                            [
                                "protein",
                            ]
                    },
                    {
                        "name": "test_food_4",
                        "cal": "test_cal_4",
                        "ingredients":
                            [
                                "yağ",
                            ]
                    },
                    {
                        "name": "test_food_5",
                        "cal": "test_cal_5",
                        "ingredients":
                            [
                                "protein",
                            ]
                    }
                ]
        },
        {  # meal 1
            "name": "meal_1",
            "food_list":
                [
                    {
                        "name": "test_food_3",
                        "cal": "test_cal_3",
                        "ingredients":
                            [
                                "protein",
                            ]
                    },
                    {
                        "name": "test_food_4",
                        "cal": "test_cal_4",
                        "ingredients":
                            [
                                "yağ",
                            ]
                    },
                    {
                        "name": "test_food_5",
                        "cal": "test_cal_5",
                        "ingredients":
                            [
                                "protein",
                            ]
                    }
                ]
        }

    ]

]
