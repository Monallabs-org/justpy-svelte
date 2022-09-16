"""
create two submit buttons. One within form object; another without.
Check if complete page reload is being done. 

"""
import sys                      # 
import justpy as jp

def button_click(dbref, msg):
    pass

def wp_testForm(request):
    wp = jp.WebPage()
    div = jp.Div(classes="flex m-4", a=wp)
    form = jp.Form(a=div)
    button = jp.Button(a=form, text="Submit", on_click=button_click)
    button2 = jp.Button(a=div, text="Submit2", on_click=button_click)
    
    return wp
        

app = jp.build_app()
app.add_jproute("/", wp_testForm)

    
