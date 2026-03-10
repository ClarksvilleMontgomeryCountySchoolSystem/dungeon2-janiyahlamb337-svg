good = r"""

                                 ___
                            ,.-"',..'"-.
                          ,' `.,' : '`'.`.
                         ;`-. " `. ``:` `.'.
                        ..   '`-.:...-:-` ' .
                        ; `.;   .      :   ' .
                        |. . ```:---...,;,, .|
                        | `:--..:    /   \ ' |
                         `.;    :```' "./##\:'
                           ``-..:___|  |####|
                                     `.|##"'
"""
bad = r"""
      ,_     _,
         '._.'
    '-,   (_)   ,-'
      '._ .:. _.'
       _ '|Y|' _
     ,` `>\ /<` `,
    ` ,-`  I  `-, `
      |   /=\   |
    ,-'   |=|   '-,
          )-(
jgs       \_/
"""























escaped = True
print(bad)
outcome = "Doom: You have not escaped."
if escaped:
    outcome = "Legend: We have escaped."
    print(good)
print(outcome)