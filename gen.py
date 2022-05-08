import os

"""
taking inspiration from tailwind, we can define one class to have this type of form (in one line)
      .w-1 {width: 1px;}
converting the values to variables would look something like this
      .class_name-value {css_property: value;}
"""

css = {
    # file_name
    # !!! Do not choose a file_name that already exists in the ./css directory, if you want to preserve it
    "margin": [
        # [class_name, css_property]
        ['m', 'margin'],
        ['mt', 'margin-top'],
        ['mb', 'margin-bottom'],
        ['ml', 'margin-left'],
        ['mr', 'margin-right'],
        # [class_name, css_property, css_property]
        ['mx', 'margin-right', 'margin-left'],
        ['my', 'margin-top', 'margin-bottom'],
    ],
    "padding": [
        ['p', 'padding'],
        ['pt', 'padding-top'],
        ['pb', 'padding-bottom'],
        ['pl', 'padding-left'],
        ['pr', 'padding-right'],
        ['px', 'padding-right', 'padding-left'],
        ['py', 'padding-top', 'padding-bottom'],
    ],
    "gap": [
        ['gap', 'gap'],
    ],
    "height": [
        ['h', 'height'],
        ['max-h', 'max-height'],
        ['min-h', 'min-height'],
    ],
    "width": [
        ['w', 'width'],
        ['max-w', 'max-width'],
        ['min-w', 'min-width'],
    ],
}


class_value_range = [
    # values for the loop that will generate the auto-incrementing css classes
    # start , end, increment
    [0,     102,    2],
    [100,   402,    5],
    [400,   802,    10]
]

# if include_unit_in_name is set to true,
# the css unit is appeded to the class name
# ( For tailwind compatibility )
include_unit_in_name = False
css_unit = "px"


for file_name, key_value in css.items():
    # on each run, check if the file (name of the key) already exists
    # if file exist, delete it so that the appends would not duplicate
    file_path = f'./css/{file_name}.css'
    if os.path.exists(file_path):
        os.remove(file_path)

    for array in key_value:
        # the first value defined in the array is the class name
        class_name = array[0]
        # the second value in the array is the css property
        css_property = array[1]

        # if two values are provided in the array
        if len(array) == 2:
            # create / open the file that will hold the generated class names
            file_object = open(f'./css/{file_name}.css', 'a')

            # loop over each array in the class_value_range array and use the defined values for the for loop
            for value_range in class_value_range:
                for x in range(value_range[0], value_range[1], value_range[2]):

                    if include_unit_in_name:
                        single_css_class = f".{class_name}-{x}{css_unit}{{{css_property}:{x}{css_unit};}}"
                        file_object.write(single_css_class)
                    else:
                        single_css_class = f".{class_name}-{x}{{{css_property}:{x}{css_unit};}}"
                        file_object.write(single_css_class)

            # file_object.close()

        # if you provide 3 values / 2 css properties  in the array,
        elif len(array) == 3:
            css_property_2 = array[2]
            file_object = open(f'./css/{file_name}.css', 'a')

            for value_range in class_value_range:
                for x in range(value_range[0], value_range[1], value_range[2]):

                    if include_unit_in_name:
                        single_css_class = f".{class_name}-{x}{css_unit}{{{css_property}:{x}{css_unit};{css_property_2}:{x}{css_unit};}}"
                        file_object.write(single_css_class)
                    else:
                        single_css_class = f".{class_name}-{x}{{{css_property}:{x}{css_unit};{css_property_2}:{x}{css_unit};}}"
                        file_object.write(single_css_class)

        else:
            print("Too many or too little values in the array.")
