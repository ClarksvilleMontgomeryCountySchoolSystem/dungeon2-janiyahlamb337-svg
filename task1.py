bad = r"""
                     888               d8b     888 
                     888               Y8P     888 
                     888                       888 
 8888b. 88888b.  .d88888888d888 .d88b. 888 .d88888 
    "88b888 "88bd88" 888888P"  d88""88b888d88" 888 
.d888888888  888888  888888    888  888888888  888 
888  888888  888Y88b 888888    Y88..88P888Y88b 888 
"Y888888888  888 "Y88888888     "Y88P" 888 "Y88888 

"""

good = r"""

     __//
cf  /.__.\
    \ \/ /
 '__/    \
  \-      )
   \_____/
_____|_|____
     " "
"""






torch_lit = True
print(bad)
outcome = "Doom: What should we do? "
if torch_lit:
    outcome = "Flicker: Let's go out there."
    print(good)

print(outcome)