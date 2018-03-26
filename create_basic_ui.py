from tkinter import *
def create_ui(address):
    create_ui_root=Tk()
    create_ui_root.attributes('-fullscreen',True)
    create_ui_root.configure(background='white')

    
    create_ui_logo_res_image=PhotoImage(master=create_ui_root,file=address)
    create_ui_logo=Label(create_ui_root,image=create_ui_logo_res_image)  
    create_ui_logo.grid(row=0,column=0,pady=100,columnspan=2,padx=200)

    
    create_ui_search_bar=Entry(create_ui_root,width=70,font=('Verdana',22))
    create_ui_search_bar.config(highlightbackground='black',highlightthickness=3)
    create_ui_search_bar.grid(row=1,column=0,padx=(75,0))

    create_ui_perform_search=Button(create_ui_root,font=('Arial Black',14),bg='blue',fg='white',text='SEARCH',relief="raised")
    # to add: command=
    create_ui_perform_search.grid(row=1,column=1)


    
    create_ui_root.mainloop()


#This is a basic function to create the start page ui of the search engine
