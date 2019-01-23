#!/usr/bin/python3

from PIL import Image, ImageDraw
import Table

data = [
    {
        'table': 'Persons',
        'cols': [
            {
                'name' => 'id',
                'is_primary' => true,
                'type' => 'int'
            },
            {
                'name' => 'name',
                'type' => 'string',
            },
            {
                'name' => 'age',
                'type' => 'int',
                'nullable' => true,
            },
            {
                'name' => 'school_id',
                'type' => 'integer',
                'nullable' => true,
            }
        ]
    },
    {
        'table': 'Schools',
        'cols': [
            {
                'name' => 'id',
                'is_primary' => true,
                'type' => 'int'
            },
            {
                'name' => 'name',
                'type' => 'string'
            }
        ]
    }
]
img = Image.new('RGB',(60,30),color = 'black')

draw = ImageDraw.Draw(img)
new DrawClass(draw,data[0])->draw
del draw

img.save("output.png")
