import pywinauto
from pywinauto import application
app =application.Application()
app.start("Notepad.exe")

# 1st Method-----------------------------------------

# dialog = app.window(title='Untitled - Notepad')
# #dialog.Edit.type_keys("Hello UST global")
# dialog.Edit.type_keys("Balkumar Hello UST global ",with_spaces=True)

#2nd method
app.Notepad.Edit.type_keys("Hello Balkumar",with_spaces=True)
app.Notepad.menu_select("File->SaveAs")
app.SaveAs.Edit.set_edit_text("test.txt")
app.Save.Save.click(double=True)
