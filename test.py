import cppimport
LCDInit = cppimport.imp("LCDInit")
LCDclear = cppimport.imp("LCDclear")
LCDdrawChar = cppimport.imp("LCDdrawChar") #This will pause for a moment to compile the module
LCDdisplay = cppimport.imp("LCDdisplay")

LCDInit(14, 12, 5, 10, 4, 50)
LCDclear()
LCDdrawChar(1, 0, 'A', 0, 0)
LCDdisplay()