good = r"""
                                   ___
                               ,-""   `.
                             ,'  _   e )`-._
                            /  ,' `-._<.===-'
                           /  /
                          /  ;
              _          /   ;
 (`._    _.-"" ""--..__,'    |
 <_  `-""                     \
  <`-                          :
   (__   <__.                  ;
     `-.   '-.__.      _.'    /
        \      `-.__,-'    _,'
         `._    ,    /__,-'
            ""._\__,'< <____
                 | |  `----.`.
                 | |        \ `.
                 ; |___      \-``
                 \   --<
                  `.`.<
             hjw    `-'
"""

bad = r"""

                          *  *       *  * 
                        *      *   *      *
                        *       * *       *
                         *       *       *   
                           *           *
                             *       *
                               *   *
                                * *             arm
                                 *
"""













drawbridge_raised = True
print(good)
outcome = ("Doom: We're caught, RUNNNN!!!!")
if not drawbridge_raised:
    outcome = ("Thunder: We have to cross!")
    print(bad)
print(outcome)