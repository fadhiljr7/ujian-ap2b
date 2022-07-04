#/home/mufin/.local/share/virtualenvs/My_Projects-23sAJxQN/bin/activate

import streamlit as st

# st.markdown(""" <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# </style> """, unsafe_allow_html=True)

# st.write('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("logolabti.png", width=150)

with col3:
    st.write(' ')

st.markdown("<h1 style='text-align: center; color: white;'>Information Technology Laboratory</h1>", unsafe_allow_html=True)

st.markdown("""
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
""", unsafe_allow_html=True)

st.markdown("""
<!-- Image and text -->
<nav class="navbar fixed-bottom navbar-expand-lg navbar-dark" style="background-color: #BA3EC8">
  <a class="navbar-brand" href="#">
    University of Gunadarma
  </a>
</nav>
""", unsafe_allow_html=True)

st.write("""
# **Final Score App AP2B 1IA21**
You can use this app to check your score on Saturday, 28 May 2022 20:00.
""")

npm = st.text_input("NPM : ")
search = st.button("Search")

if search or npm:
    if npm == "50421004":
        pretest = (780)/8
        posttest = (700)/8
        activity = (640)/8
        fnlrpt = (480)/8
        exscore = 80
        attdnc = (8/8)*100
        st.write("Name: ABDUL KAHPI")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "12345678":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        attdnc = (7/8)*100
        st.write("Name: CONTOH INPUT")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 1")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)
    
    elif npm == "50421056":
        pretest = (760)/8
        posttest = (800)/8
        activity = (640)/8
        fnlrpt = (650)/8
        exscore = 99
        attdnc = (8/8)*100
        st.write("Name: ADRIAN WARTONO")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50421107":
        pretest = (580)/8
        posttest = (560)/8
        activity = (560)/8
        fnlrpt = (580)/8
        exscore = 95
        attdnc = (7/8)*100
        st.write("Name: ALDY SYAHPUTRA HARIANJA")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 1")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50421163":
        pretest = (800)/8
        posttest = (760)/8
        activity = (640)/8
        fnlrpt = (685)/8
        exscore = 100
        attdnc = (8/8)*100
        st.write("Name: ANGEL PANDELAKI")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50421166":
        pretest = (740)/8
        posttest = (720)/8
        activity = (640)/8
        fnlrpt = (680)/8
        exscore = 100
        attdnc = (8/8)*100
        st.write("Name: ANGGA DAMARA PUTRA")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50421217":
        pretest = (760)/8
        posttest = (780)/8
        activity = (720)/8
        fnlrpt = (430)/8
        exscore = 100
        attdnc = (8/8)*100
        st.write("Name: ARYA ADHI PRATAMA")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50421282":
        pretest = (780)/8
        posttest = (800)/8
        activity = (720)/8
        fnlrpt = (580)/8
        exscore = 100
        attdnc = (8/8)*100
        st.write("Name: BINTANG ARMEYELIA")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50421319":
        pretest = (760)/8
        posttest = (780)/8
        activity = (720)/8
        fnlrpt = (590)/8
        exscore = 100
        attdnc = (8/8)*100
        st.write("Name: DAFFA RIZKY FADILAH")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50421380":
        pretest = (760)/8
        posttest = (720)/8
        activity = (700)/8
        fnlrpt = (560)/8
        exscore = 82
        attdnc = (6/8)*100
        st.write("Name: DIKA SUGIH ILMAN KUSUMA PUTRA")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 4/7")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51421591":
        pretest = (740)/8
        posttest = (700)/8
        activity = (680)/8
        fnlrpt = (530)/8
        exscore = 100
        attdnc = (7/8)*100
        st.write("Name: DIO RIZKY ANDIMA")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 4")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50421433":
        pretest = (740)/8
        posttest = (780)/8
        activity = (730)/8
        fnlrpt = (670)/8
        exscore = 100
        attdnc = (8/8)*100
        st.write("Name: Fadhilah Khusnul Khotami")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50421483":
        pretest = (660)/8
        posttest = (700)/8
        activity = (540)/8
        fnlrpt = (300)/8
        exscore = 90
        attdnc = (4/8)*100
        st.write("Name: FARIS RASYID")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 3/4/6/7")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50421517":
        pretest = (800)/8
        posttest = (760)/8
        activity = (660)/8
        fnlrpt = (550)/8
        exscore = 90
        attdnc = (8/8)*100
        st.write("Name: FIKAR MAULANA")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50421562":
        pretest = (780)/8
        posttest = (800)/8
        activity = (710)/8
        fnlrpt = (710)/8
        exscore = 100
        attdnc = (8/8)*100
        st.write("Name: Gideon Aprileo")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50421645":
        pretest = (780)/8
        posttest = (800)/8
        activity = (740)/8
        fnlrpt = (750)/8
        exscore = 100
        attdnc = (8/8)*100
        st.write("Name: IMAM HIDAYAT")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50421654":
        pretest = (780)/8
        posttest = (800)/8
        activity = (740)/8
        fnlrpt = (740)/8
        exscore = 100
        attdnc = (8/8)*100
        st.write("Name: INDAH TRI ASTUTI")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50421687":
        pretest = (660)/8
        posttest = (620)/8
        activity = (610)/8
        fnlrpt = (350)/8
        exscore = 95
        attdnc = (8/8)*100
        st.write("Name: JOHANNES TRISNO MANALU")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50421740":
        pretest = (700)/8
        posttest = (560)/8
        activity = (740)/8
        fnlrpt = (640)/8
        exscore = 90
        attdnc = (8/8)*100
        st.write("Name: KUKUH RAFI HERNAWAN")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51421646":
        pretest = (620)/8
        posttest = (620)/8
        activity = (740)/8
        fnlrpt = (660)/8
        exscore = 100
        attdnc = (7/8)*100
        st.write("Name: MARSEL CHRISTIAN JUNIOR")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week ")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51421610":
        pretest = (720)/8
        posttest = (720)/8
        activity = (720)/8
        fnlrpt = 0
        exscore = 95
        attdnc = (8/8)*100
        st.write("Name: MARSHALL GUNAPUTRA ARIFIANTO")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50421856":
        pretest = (500)/8
        posttest = (400)/8
        activity = (630)/8
        fnlrpt = (620)/8
        exscore = 90
        attdnc = (6/8)*100
        st.write("Name: MUHAMAD ALFIN SURYA PRATAMA")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 4/5")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50421907":
        pretest = (660)/8
        posttest = (640)/8
        activity = (620)/8
        fnlrpt = (580)/8
        exscore = 97
        attdnc = (7/8)*100
        st.write("Name: MUHAMMAD ALFIN FARHANSYAH")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 4")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "50421953":
        pretest = (780)/8
        posttest = (800)/8
        activity = (720)/8
        fnlrpt = (720)/8
        exscore = 100
        attdnc = (8/8)*100
        st.write("Name: MUHAMMAD FARHAN FATHURROHMAN")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51421011":
        pretest = (680)/8
        posttest = (700)/8
        activity = (630)/8
        fnlrpt = (600)/8
        exscore = 100
        attdnc = (7/8)*100
        st.write("Name: MUHAMMAD LUTFI APRIAMTO")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 5")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51421046":
        pretest = (800)/8
        posttest = (780)/8
        activity = (720)/8
        fnlrpt = (680)/8
        exscore = 100
        attdnc = (8/8)*100
        st.write("Name: MUHAMMAD RAIHAN PUTRA")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51421093":
        pretest = (740)/8
        posttest = (780)/8
        activity = (720)/8
        fnlrpt = (660)/8
        exscore = 92
        attdnc = (8/8)*100
        st.write("Name: Muhammad Try Ramdhani")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51421106":
        pretest = (540)/8
        posttest = (480)/8
        activity = (520)/8
        fnlrpt = (60)/8
        exscore = 87
        attdnc = (5/8)*100
        st.write("Name: NABILA DHEA HERLANGGENG")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 4/5/7")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51421163":
        pretest = (800)/8
        posttest = (680)/8
        activity = (710)/8
        fnlrpt = (670)/8
        exscore = 80
        attdnc = (7/8)*100
        st.write("Name: OKKY DHELFILANO")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 4")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51421210":
        pretest = (800)/8
        posttest = (780)/8
        activity = (720)/8
        fnlrpt = (690)/8
        exscore = 100
        attdnc = (8/8)*100
        st.write("Name: RAFLY RAMADAN")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51421212":
        pretest = (800)/8
        posttest = (800)/8
        activity = (720)/8
        fnlrpt = (650)/8
        exscore = 100
        attdnc = (8/8)*100
        st.write("Name: RAHADANI SYIFARIANI")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51421272":
        pretest = (660)/8
        posttest = (600)/8
        activity = (560)/8
        fnlrpt = (400)/8
        exscore = 100
        attdnc = (7/8)*100
        st.write("Name: REDIYA VIO DARMAWAN")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 8")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51421335":
        pretest = (800)/8
        posttest = (780)/8
        activity = (640)/8
        fnlrpt = (560)/8
        exscore = 95
        attdnc = (8/8)*100
        st.write("Name: RIZA PUTRA OCTAVIANTORO")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51421398":
        pretest = (800)/8
        posttest = (800)/8
        activity = (640)/8
        fnlrpt = (640)/8
        exscore = 100
        attdnc = (8/8)*100
        st.write("Name: SATRIO WIBOWO")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51421466":
        pretest = (800)/8
        posttest = (800)/8
        activity = (740)/8
        fnlrpt = (640)/8
        exscore = 100
        attdnc = (8/8)*100
        st.write("Name: TEGAR DWI SEPTIADI")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51421552":
        pretest = (800)/8
        posttest = (780)/8
        activity = (640)/8
        fnlrpt = (640)/8
        exscore = 90
        attdnc = (8/8)*100
        st.write("Name: ZAHIDAN ARDHIANSYAH")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    else:
        st.write("NPM not found")

    estgrade = (pretest+posttest+activity+fnlrpt+exscore)/5
    if estgrade >= 80:
        st.write("Estimation grade from LAB TI: A")
    elif estgrade >= 70:
        st.write("Estimation grade from LAB TI: B")
    elif estgrade >= 60:
        st.write("Estimation grade from LAB TI: C")
    else:
        st.write("Estimation grade from LAB TI: D")
    st.balloons()

#/home/mufin/.local/share/virtualenvs/My_Projects-23sAJxQN/bin/activate