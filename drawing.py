import time
import os

frameList = ['''
 ------^-__
        *  \\
        *  /
 ______ _--
       v

 ''',
 '''
 -----------^-__
             *  \\
             *  /
 ___________ _--
            v

 ''',
 '''
  __-----------^-__
<|              *  \\
<|              *  /
  --___________ _--
               v
''',
'''
      __-----------^-__
->  <|              *  \\
->  <|              *  /
      --___________ _--
                   v
''',
'''
         __-----------^-__
>-->   <|              *  \\
>-->   <|              *  /
         --___________ _--
                      v
''',
'''
              __-----------^-__
->  >-->    <|              *  \\
->  >-->    <|              *  /
              --___________ _--
                           v
''',
'''
                    __-----------^-__
   >-->  >-->     <|              *  \\
   >-->  >-->     <|              *  /
                    --___________ _--
                                 v
''',
'''          
------^-__                      __-----------^-__
       *  \\   >-->  >-->     <|              *  \\
       *  /    >-->  >-->     <|              *  /
______ _--                      --___________ _--
      v                                      v
''',
'''

'''
 ]

while True:
	os.system("cls")
	for frame in frameList:
		print(frame)
		time.sleep(.1)
		os.system("cls")
