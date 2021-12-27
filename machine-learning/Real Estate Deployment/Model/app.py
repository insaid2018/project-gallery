import numpy as np
from flask import Flask, render_template, request
import pickle
import pandas as pd
app = Flask(__name__)

@app.route("/")



def homepage():
    return render_template("templates.html")
@app.route("/house_price_predictor", methods=["POST"])

def predict():
    if request.method == "POST":
       INT_SQFT= int((request.form["INT_SQFT"]).replace(" ",""))
       print(INT_SQFT)

       DIST_MAINROAD= int((request.form["DIST_MAINROAD"]).replace(" ",""))
       print(DIST_MAINROAD)

       N_BEDROOM= int((request.form["N_BEDROOM"]).replace(" ", ""))
       print(N_BEDROOM)

       N_BATHROOM = int((request.form["N_BATHROOM"]).replace(" ", ""))
       print(N_BATHROOM)

       N_ROOM= int((request.form["N_ROOM"]).replace(" ", ""))
       print(N_ROOM)

       QS_ROOMS= int((request.form["QS_ROOMS"]).replace(" ", ""))
       print(QS_ROOMS)

       QS_BATHROOM= int((request.form["QS_BATHROOM"]).replace(" ", ""))
       print(QS_BATHROOM)

       QS_BEDROOM= int((request.form["QS_BEDROOM"]).replace(" ", ""))
       print(QS_BEDROOM)

       QS_OVERALL= int((request.form["QS_OVERALL"]).replace(" ", ""))
       print(QS_OVERALL)

       COMMIS= int((request.form["COMMIS"]).replace(" ", ""))
       print(COMMIS)

       flag = 0

       #### AREA

       area = request.form["area"].replace(" ","")
       if area == "Select":
           flag = 1
       elif area == "Adyar":
           Adyar= 1
           Anna_Nagar,Chrompet, KK_Nagar ,Karapakkam, T_Nagar ,Velachery = 0,0,0,0,0,0
       elif area == "Anna Nagar":
           Anna_Nagar = 1
           Adyar, Chrompet, KK_Nagar, Karapakkam, T_Nagar, Velachery = 0,0,0,0,0,0
       elif area == "Chrompet":
           Chrompet= 1
           Adyar, Anna_Nagar , KK_Nagar, Karapakkam, T_Nagar, Velachery = 0,0,0,0,0,0
       elif area == "KK Nagar":
           KK_Nagar= 1
           Adyar, Chrompet, Anna_Nagar, Karapakkam, T_Nagar, Velachery = 0,0,0,0,0,0
       elif area == "Karapakkam":
           Karapakkam = 1
           Adyar, Chrompet, KK_Nagar, Anna_Nagar, T_Nagar, Velachery = 0,0,0,0,0,0
       elif area == "T Nagar":
           T_Nagar= 1
           Adyar, Chrompet, KK_Nagar, Karapakkam, Anna_Nagar, Velachery = 0,0,0,0,0,0
       else:
           Velachery = 1
           Adyar, Chrompet, KK_Nagar, Karapakkam, T_Nagar, Anna_Nagar = 0,0,0,0,0,0

       print(1)


      ## SALE_COND

       sale_cond = request.form["SALE_COND"].replace(" ","")
       if sale_cond == "Select":
           flag = 1
       elif sale_cond ==  "AbNormal":
           AbNormal, AdjLand, Family,  Normal_Saler, Partial = 1,0,0,0,0
       elif sale_cond == "AdjLand":
           AbNormal, AdjLand, Family, Normal_Saler, Partial = 0, 1 ,0, 0, 0

       elif sale_cond == "Family":
           AbNormal, AdjLand, Family, Normal_Saler, Partial = 0, 0,1, 0, 0

       elif sale_cond == "Normal Saler":
           AbNormal, AdjLand, Family, Normal_Saler, Partial = 0, 0, 0, 1, 0

       else:
           AbNormal, AdjLand, Family, Normal_Saler, Partial = 0, 0 ,0, 0, 1

       print(2)
      ## Park_facil

       Park_facil = request.form['PARK_FACIL'].replace(" ","")
       if Park_facil == "Select":
           flag = 1
       elif Park_facil == 'Yes':
           No, Yes = 0,1
       else:
           No, Yes = 1,0

       print(3)
       BUILDTYPE = request.form['BUILDTYPE'].replace(" ", "")
       if BUILDTYPE == "Select":
           flag = 1
       elif BUILDTYPE == 'House':
           House = 1
           Commercial, Others = 0,0
       elif BUILDTYPE == 'Commercial':
           Commercial = 1
           House, Others = 0,0
       else:
           Commercial = 0
           House, Others = 0, 1

       print(4)

       UTILITY_AVAIL = request.form['UTILITY_AVAIL'].replace(" ", "")
       if UTILITY_AVAIL == "Select":
           flag = 1
       elif UTILITY_AVAIL == 'AllPub':
           AllPub = 1
           ELO, NoSeWa, NoSewr =0,0,0
       elif UTILITY_AVAIL == 'ELO':
           AllPub = 0
           ELO, NoSeWa, NoSewr = 1, 0, 0

       elif UTILITY_AVAIL == 'NoSeWa':
           AllPub = 0
           ELO, NoSeWa, NoSewr = 0, 1, 0
       else:
           AllPub = 0
           ELO, NoSeWa, NoSewr = 0, 0, 1
       print(5)

       STREET_TYPE= request.form['STREET'].replace(" ", "")
       if STREET_TYPE == "Select":
           flag = 1
       elif STREET_TYPE == 'Gravel':
           Gravel = 1
           NoAccess, Paved=0,0
       elif STREET_TYPE == 'NoAccess':
           Gravel = 0
           NoAccess, Paved = 1, 0
       elif STREET_TYPE == 'Paved':
           Gravel = 0
           NoAccess, Paved = 0, 1
       print(6)


       MZZONE= request.form['MZZONE'].replace(" ", "")
       if MZZONE== "Select":
           flag = 1
       elif MZZONE == 'A':
           A= 1
           C=0
           I=0
           RH=0
           RL=0
           RM=0
       elif MZZONE ==  'C':
           A, C, I, RH, RL, RM = 0,1,0,0,0,0
       elif MZZONE == 'I':
           A, C, I, RH, RL, RM = 0,0,1,0,0,0
       elif MZZONE ==  'RH':
           A, C, I, RH, RL, RM = 0,0,0,1,0,0
       elif MZZONE == 'RL':
           A, C, I, RH, RL, RM = 0,0,0,0,1,0
       else:
           A, C, I, RH, RL, RM = 0,0,0,0,0,1
       print(A)

    model = open('chennai_house.pkl', 'rb')
    final_file = pickle.load(model)
    data = pd.DataFrame([[Adyar, Anna_Nagar, Chrompet, KK_Nagar, Karapakkam, T_Nagar,
    Velachery, AbNormal, AdjLand, Family, Normal_Saler, Partial,
    INT_SQFT, DIST_MAINROAD, N_BEDROOM, No, Commercial, AllPub,
    Gravel, A, C, I, RH, RL, RM, NoAccess, Paved, ELO,
    NoSeWa, NoSewr, House, Others, Yes, N_BATHROOM, N_ROOM,
    QS_ROOMS, QS_BATHROOM, QS_BEDROOM, QS_OVERALL, COMMIS]], columns = ['Adyar', 'Anna Nagar', 'Chrompet', 'KK Nagar', 'Karapakkam', 'T Nagar', 'Velachery', 'AbNormal', 'AdjLand', 'Family', 'Normal Sale', 'Partial',
    'INT_SQFT', 'DIST_MAINROAD', 'N_BEDROOM', 'No', 'Commercial', 'AllPub',
     'Gravel', 'A', 'C', 'I', 'RH', 'RL', 'RM', 'No Access', 'Paved', 'ELO',
    'NoSeWa', 'NoSewr ', 'House', 'Others', 'Yes', 'N_BATHROOM', 'N_ROOM',
    'QS_ROOMS', 'QS_BATHROOM', 'QS_BEDROOM', 'QS_OVERALL', 'COMMIS'])
    result = final_file.predict(data)

    if flag == 0:
        var1 = "Your Predicted Price is " + str(result[0])
    else:
        var1= "ERROR! Please Give a  Valid Input"

    return render_template("templates.html", predict=var1)




if (__name__ == "__main__"):
    app.run()

