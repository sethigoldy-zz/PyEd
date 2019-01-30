#!/usr/bin/python3

from PIL import Image, ImageDraw
import table
import coloumn

# ~ data = [
    # ~ {
        # ~ 'table': 'Persons',
        # ~ 'cols': [
            # ~ {
                # ~ 'name' => 'id',
                # ~ 'is_primary' => true,
                # ~ 'type' => 'int'
            # ~ },
            # ~ {
                # ~ 'name' => 'name',
                # ~ 'type' => 'string',
            # ~ },
            # ~ {
                # ~ 'name' => 'age',
                # ~ 'type' => 'int',
                # ~ 'nullable' => true,
            # ~ },
            # ~ {
                # ~ 'name' => 'school_id',
                # ~ 'type' => 'integer',
                # ~ 'nullable' => true,
            # ~ }
        # ~ ]
    # ~ },
    # ~ {
        # ~ 'table': 'Schools',
        # ~ 'cols': [
            # ~ {
                # ~ 'name' => 'id',
                # ~ 'is_primary' => true,
                # ~ 'type' => 'int'
            # ~ },
            # ~ {
                # ~ 'name' => 'name',
                # ~ 'type' => 'string'
            # ~ }
        # ~ ]
    # ~ }
# ~ ]

baseImageSize = [1000,700]

img = Image.new('RGB',baseImageSize,'white')

parent = [10,20]
draw = ImageDraw.Draw(img)

col = coloumn.Coloumn('Name','String',12,0)
col.draw(parent,100,draw)

col = coloumn.Coloumn('Email','String',100,1)
col.draw(parent,100,draw)

del draw

img.save("output.png")
