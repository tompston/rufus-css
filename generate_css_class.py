import os

# taking inspiration from tailwind, we can define one class to have this type of form (in one line)
#       .w-1 {width: 1px;}
# converting the values to variables would look something like this
#       .class_name-value {css_property: value;}

css = {
    # file_name
    # Do NOT choose a file_name that already exists in the ./css directory, if you want to preserve it
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
        ['gap-h', 'row-gap'],
        ['gap-w', 'column-gap'],
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

# values for the loop that will generate the auto-incrementing css classes
# adjusted to personal needs
first_loop_first_value = 0
first_loop_last_value = 102
first_loop_increment = 2


second_loop_first_value = 100
second_loop_last_value = 602
second_loop_increment = 5

css_unit = "px"


# for key, value
for file_name, key_value in css.items():
    # on each run, check if the file already exists
    # if file exist, delete so that the appends would not duplicate
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

            for x in range(first_loop_first_value, first_loop_last_value, first_loop_increment):
                single_css_class = ".%s-%d{%s : %d%s;}" % (
                    class_name, x, css_property, x, css_unit)
                # at this point, you have access to a single generated css class, so append / save it to thr file
                file_object.write(single_css_class)

            for x in range(second_loop_first_value, second_loop_last_value, second_loop_increment):
                single_css_class = ".%s-%d{%s : %d%s;}" % (
                    class_name, x, css_property, x, css_unit)
                file_object.write(single_css_class)

            file_object.close()

         # if you provide 3 values / 2 css properties  in the array,
        elif len(array) == 3:
            css_property_2 = array[2]
            file_object = open(f'./css/{file_name}.css', 'a')

            for x in range(first_loop_first_value, first_loop_last_value, first_loop_increment):
                single_css_class = ".%s-%d{%s : %d%s; %s : %d%s;}" % (
                    class_name, x, css_property, x, css_unit, css_property_2, x, css_unit)
                file_object.write(single_css_class)

            for x in range(second_loop_first_value, second_loop_last_value, second_loop_increment):
                single_css_class = ".%s-%d{%s : %d%s; %s : %d%s;}" % (
                    class_name, x, css_property, x, css_unit, css_property_2, x, css_unit)
                file_object.write(single_css_class)

        else:
            print("Too many or too little values in the array.")
