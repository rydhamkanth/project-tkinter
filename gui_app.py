#import tkinter library for gui interface.......
import tkinter as tk
from tkinter import ttk    #for more attractive buttons and radiobuttons etc...
win = tk.Tk()
win.title("covid_19 DATA" )

#create lables....... like : lables, buttons, radio buttons 
name_label = ttk.Label(win, text="Enter your full name : ").grid(row=0, column=0, sticky=tk.W)
age_label = ttk.Label(win, text="Enter your age : ").grid(row=1,column=0, sticky=tk.W)
contact_label = ttk.Label(win, text="Enter your contact number : ").grid(row=2,column=0, sticky=tk.W)
email_label = ttk.Label(win, text="Enter your E-MAIL : ").grid(row=3,column=0, sticky=tk.W)
gender_label = ttk.Label(win, text="Select your gender : ").grid(row=4, column=0, sticky=tk.W)
address_label = ttk.Label(win, text="Enter your current address : ").grid(row=5, column=0, sticky=tk.W)
occupation_label = ttk.Label(win, text="Select your occupation : ").grid(row=6, column=0, sticky=tk.W) 
tavel_label = ttk.Label(win, text="Any travel history ? (IF YES ENTER CITY NAME !): ").grid(row=7, column=0, sticky=tk.W)
transport_label = ttk.Label(win, text="Mode of transportation : ").grid(row=8, column=0, sticky=tk.W)
symptom_label = ttk.Label(win, text="Please select the symptoms if any... : ").grid(row=9, column=0, sticky=tk.W)
fever_label = ttk.Label(win, text="FEVER : ").grid(row=10, column=0, sticky=tk.W)
cough_label = ttk.Label(win, text="DRY COUGH : ").grid(row=11, column=0, sticky=tk.W)
tiredness_label = ttk.Label(win, text="TIREDNESS : ").grid(row=12, column=0, sticky=tk.W)
pain_label = ttk.Label(win, text="ACHES AND PAINS : ").grid(row=13, column=0, sticky=tk.W)
sorethroat_label = ttk.Label(win, text="SORE THROAT : ").grid(row=14, column=0, sticky=tk.W)
headache_label = ttk.Label(win, text="HEADACHE : ").grid(row=15, column=0, sticky=tk.W)
chest_label = ttk.Label(win, text="CHEST PAIN AND PRESSURE : ").grid(row=16, column=0, sticky=tk.W)
breath_label = ttk.Label(win, text="SHORTNESS OF BREATH : ").grid(row=17, column=0, sticky=tk.W)
diabetic_label = ttk.Label(win, text="Are u a DIABETIC person ?  : ").grid(row=18, column=0, sticky=tk.W)
facing_label = ttk.Label(win, text="From how many days you are facing symptoms ?  : ").grid(row=19, column=0, sticky=tk.W)
screening_label = ttk.Label(win, text="Have u consulted to Doctor yet ?  : ").grid(row=20, column=0, sticky=tk.W)
stay_label = ttk.Label(win, text="STAY HOME, STAY SAFE !!!! ").grid(row=22, column=1)

#create entry box.................
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win, width=20, textvariable= name_var).grid(row=0, column=1)

age_var = tk.StringVar()
age_entrybox = ttk.Entry(win, width=20, textvariable= age_var).grid(row=1, column=1)

contact_var = tk.StringVar()
contact_entrybox = ttk.Entry(win, width=20, textvariable= contact_var).grid(row=2, column=1)

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win, width=20, textvariable= email_var).grid(row=3, column=1)

address_var = tk.StringVar()
address_entrybox = ttk.Entry(win, width=20, textvariable= address_var).grid(row=5, column=1)

travel_var = tk.StringVar()
travel_entrybox = ttk.Entry(win, width=20, textvariable= travel_var).grid(row=7, column=1)






#create combobox............
gender_var= tk.StringVar()
gender_combobox = ttk.Combobox(win , width=17, textvariable= gender_var , state = "readonly")
gender_combobox['values'] = ('MALE' , 'FEMALE' , 'OTHERS')
gender_combobox.current(0)
gender_combobox.grid(row=4, column=1)

facing_symptoms= tk.StringVar()
facing_combobox = ttk.Combobox(win , width=17, textvariable= facing_symptoms , state = "readonly")
facing_combobox['values'] = ('NO SYMPTOMS' , '1 DAY' , '2 DAYS' , '3 DAYS' , '4 DAYS' , '5 DAYS', '1 WEEK' , '2WEEKS', 'MORE THAN A 15 DAYS')
facing_combobox.current(0)
facing_combobox.grid(row=19, column=1)


#adding radio button>....................
user_ocuupation = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win , text="Student",value= "Student", variable= user_ocuupation).grid(row=6,column=1)
radiobtn2 = ttk.Radiobutton(win , text="Teacher      ",value= "Teacher", variable= user_ocuupation).grid(row=6,column=2)
radiobtn3 = ttk.Radiobutton(win , text="Others",value= "Others", variable= user_ocuupation).grid(row=6,column=3)


transportation_mode = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win , text="Bus",value= "Bus", variable= transportation_mode).grid(row=8,column=1)
radiobtn2 = ttk.Radiobutton(win , text="Car       ",value= "Car", variable= transportation_mode).grid(row=8,column=2)
radiobtn3 = ttk.Radiobutton(win , text="Train                ",value= "Train", variable= transportation_mode).grid(row=8,column=3)
radiobtn4 = ttk.Radiobutton(win , text="Plane               ",value= "Plane", variable= transportation_mode).grid(row=8,column=4)
radiobtn5 = ttk.Radiobutton(win , text="no_where",value= "no_where", variable= transportation_mode).grid(row=8,column=5)

fever_var = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win , text="YES",value= "yes", variable= fever_var).grid(row=10,column=1)
radiobtn2 = ttk.Radiobutton(win , text="NO      ",value= "no", variable= fever_var).grid(row=10,column=2)

cough_var = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win , text="YES",value= "yes", variable= cough_var).grid(row=11,column=1)
radiobtn2 = ttk.Radiobutton(win , text="NO      ",value= "no", variable= cough_var).grid(row=11,column=2)

tiredness_var = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win , text="YES",value= "yes", variable= tiredness_var).grid(row=12,column=1)
radiobtn2 = ttk.Radiobutton(win , text="NO      ",value= "no", variable= tiredness_var).grid(row=12,column=2)

pain_aches = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win , text="YES",value= "yes", variable= pain_aches).grid(row=13,column=1)
radiobtn2 = ttk.Radiobutton(win , text="NO      ",value= "no", variable= pain_aches).grid(row=13,column=2)

sore_throat = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win , text="YES",value= "yes", variable= sore_throat).grid(row=14,column=1)
radiobtn2 = ttk.Radiobutton(win , text="NO      ",value= "no", variable= sore_throat).grid(row=14,column=2)

headache_var = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win , text="YES",value= "yes", variable= headache_var).grid(row=15,column=1)
radiobtn2 = ttk.Radiobutton(win , text="NO      ",value= "no", variable= headache_var).grid(row=15,column=2)

chest_pain = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win , text="YES",value= "yes", variable= chest_pain).grid(row=16,column=1)
radiobtn2 = ttk.Radiobutton(win , text="NO      ",value= "no", variable= chest_pain).grid(row=16,column=2)

shortness_in_breath = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win , text="YES",value= "yes", variable= shortness_in_breath).grid(row=17,column=1)
radiobtn2 = ttk.Radiobutton(win , text="NO      ",value= "no", variable= shortness_in_breath).grid(row=17,column=2)

diabetic_person = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win , text="YES",value= "yes", variable= diabetic_person).grid(row=18,column=1)
radiobtn2 = ttk.Radiobutton(win , text="NO      ",value= "no", variable= diabetic_person).grid(row=18,column=2)

doctor_screening = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win , text="YES",value= "yes", variable= doctor_screening).grid(row=20,column=1)
radiobtn2 = ttk.Radiobutton(win , text="NO      ",value= "no", variable= doctor_screening).grid(row=20,column=2)





#adding check button .............
check_var = tk.IntVar()
checkbtn = ttk.Checkbutton(win, text="select if u want to subscribe to our newsletter!!", variable= check_var ).grid(row=21,columnspan=5)



#creating buttons..............

def action():
    username = name_var.get()
    user_age = age_var.get()
    user_contact = contact_var.get()
    user_email = email_var.get()
    user_gender = gender_var.get()
    user_address = address_var.get()
    occupation = user_ocuupation.get()
    travel_history = travel_var.get()
    transport_mode = transportation_mode.get()
    fever = fever_var.get()
    cough = cough_var.get()
    tiredness = tiredness_var.get()
    pain_and_aches = pain_aches.get()
    sorethroat = sore_throat.get() 
    headache = headache_var.get()
    chestpain = chest_pain.get()
    breath = shortness_in_breath.get()
    diabetic = diabetic_person.get()
    symptoms_time = facing_symptoms.get()
    screening = doctor_screening.get()

    check = check_var.get()
    if check_var.get() == 0:
        subscribed = "no"
    else:
        subscribed = "yes"
    
    print (f"{username}, {user_age} , {user_contact} , {user_email} , {user_gender} , {user_address} , {occupation} , {travel_history} , {transport_mode} , {fever} , {cough} , {tiredness} , {pain_and_aches} , {sorethroat} , {headache} , {chestpain} , {breath} , {diabetic} , {symptoms_time } , {screening} ,{subscribed}")

    with open("data.txt" , "a") as f:
        f.write(f"name is :{username},\nage is :{user_age},\ncontact number : {user_contact},\nregistered email is: {user_email} ,\ngender is: {user_gender} ,\naddress: {user_address},\noccupation is : {occupation},\ntravel history (city) : {travel_history},\nmode of transportation: {transport_mode},\nfever :{fever} ,\ncough: {cough} ,\ntiredness: {tiredness} ,\npain and aches :{pain_and_aches} ,\nsore throat : {sorethroat} ,\nheadache : {headache} ,\nchest pain : {chestpain} ,\nshortness of breath :{breath} ,\ndiabeties :{diabetic},\nFrom how many days you are facing symptoms ? : {symptoms_time } ,\nhave u consulted to doctor :{screening} ,\nsubscribed: {subscribed} . \n \n NEXT \n")


    #name_label.configure(foreground="red")
  
submit_button = ttk.Button(win , text="                SUBMIT                ", command = action).grid(row=23,column=1,sticky=tk.W)




win.mainloop()
