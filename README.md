# **Rufus**

## **Self-defined, utility-first, Tailwind-inspired CSS library**

## Classes not dependent on root variables

| CLASS_NAME          | CSS_PROPERTY                | NOTES                                                                     |
| ------------------- | --------------------------- | ------------------------------------------------------------------------- |
| flex-center         |                             | center the content                                                        |
| grid-center         |                             | center the content                                                        |
| grid                | display: grid               |                                                                           |
| gtr-1-1             | grid-template-columns:      | 1fr widths (max 4) or auto (max 3)                                        |
| gtc-1-1             | grid-template-rows:         | 1fr widths (max 4) or auto (max 3)                                        |
| flex                | display: flex;              |                                                                           |
| flex-wrap           | flex-wrap: wrap;            |                                                                           |
| flex-nowrap         | flex-wrap: nowrap;          |                                                                           |
| flex-row            | flex-direction: row;        |                                                                           |
| flex-column         | flex-direction: column;     |                                                                           |
| fw-500              | font-weight:500;            | 100-900                                                                   |
| text-space-1        | letter-spacing              | 1-6                                                                       |
| text-SIDE           | text-align: SIDE;           | where SIDE can be: left, right, justify, center                           |
| op-15               | opacity: 0.15;              | 0-100, increment by 5                                                     |
| img-cover           | object-fit: cover;          |                                                                           |
| round               | border-radius: 50%;         |                                                                           |
| italic              | font-style: italic;         |                                                                           |
| underline           | text-decoration: underline; |                                                                           |
| hidden              | display: none;              |                                                                           |
| pointer             | cursor:pointer;             |                                                                           |
| disable-text-select |                             | don't allow text selection                                                |
| height-100          | height: 100%;               |                                                                           |
| width-100           | width: 100%;                |                                                                           |
| both-100            | height: 100%; width: 100%;  |                                                                           |
| z-10                | z-index                     | z-10, z-20, z-30, z-40 ,z-50                                              |
| temp-bg-col-1       |                             | used when you don't have any colors defined for the root variables. (1-5) |

## Classes generated from python script

### Current setup:

- 0-100, increment by 2px 
- 100-600, increment by 5px

| CLASS_NAME | CSS_PROPERTY  | NOTES                                       |
| ---------- | ------------- | ------------------------------------------- |
| gap-0      | gap           |                                             |
| gap-h-0    | row-gap       |                                             |
| gap-w-0    | column-gap    |                                             |
| h-0        | height        |                                             |
| max-h-0    | max-height    |                                             |
| min-h-0    | min-height    |                                             |
|            |               | same applies to width, just change h -> w   |
| m-0        | margin        |                                             |
| mr-0       | margin-right  |                                             |
| ml-0       | margin-left   |                                             |
| mt-0       | margin-top    |                                             |
| mb-0       | margin-bottom |                                             |
|            |               | same applies to padding, just change m -> p |

## Classes Dependent on root variables

| CLASS_NAME | CSS_PROPERTY            | NOTES                                     |
| ---------- | ----------------------- | ----------------------------------------- |
| font-fam-1 | font-family             | 1-6                                       |
| bg-col-1   | background-color        | 1-6                                       |
| text-col-1 | color                   | 1-6                                       |
| fs-1       | font-size               | 1-9                                       |
| bord-rad-1 | border-radius           | 1-6                                       |
| header-1   | font-size & line-height | 1-4, font-size dependent on root varaible |
| text-1     | font-size & line-height | 1-4, font-size dependent on root varaible |

## Classes defined based on project needs

| CLASS_NAME | CSS_PROPERTY | NOTES                  |
| ---------- | ------------ | ---------------------- |
| border-1   | border       | 1-3                    |
| button-1   | button       | 1                      |
| hr-1       | border       | 1-2, class added to hr |

## Other

    # centering content, while allowing full background
    <div class="flex-center">
        <div class="max-width-1">content</div>
    </div>

    # automatic grid example
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));

## Goals

1. The goal is not to stop writing css. The goal is to write css when you need

   - to specify things that are used relativley rarely
   - media queries
   - other custom classes that apply to a group of elements

2. The name of the root variable is the same as the class name

   - --font-fam-1 variable is font-fam-1 class

3. Don't create a new class if you need to specify a css property that is repeated very commonly

4. No project setup or downloads of external things -> everything is in a single file.

   - Minimal setup applies only if you don't need different css properties / values / ranges / increments for the classes generated by python

5. No Abstractions for the range values that are generated by python.

   - m-345 means margin: 345px

6. Chaning the values for the classes that are dependent on root variables is easy and highly encouraged

## Command to generate and combine css

    // from the root dir
    // using shell

    python generate_css_class.py && npm run concat-css
