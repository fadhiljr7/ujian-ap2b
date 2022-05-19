import streamlit as st

st.markdown("""
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
""", unsafe_allow_html=True)

st.markdown("""
<!-- Image and text -->
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #BA3EC8">
  <a class="navbar-brand" href="#">
    <img src="logolabti.png" width="30" height="30" class="d-inline-block align-top" alt="">
    Information Technology Laboratory
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
        pretest = (95+90+80+100+95+90+90+100)/8
        posttest = (95+90+80+100+95+90+100+100)/8
        activity = (100+70+70+70+70+90+100+100)/8
        fnlrpt = (100+70+70+70+70+90+100+70)/8
        exscore = 100
        st.write("Name: ABDUL KAHPI")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "12345678":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: CONTOH INPUT")
        st.write("Average pre-test score: ", pretest)
        st.write("Average post-test score: ", posttest)
        st.write("Average activity score: ", activity)
        st.write("Average final report score: ", fnlrpt)
        st.write("Exam Score: ", exscore)
    
    elif npm == "50421056":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: ADRIAN WARTONO")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "50421107":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: ALDY SYAHPUTRA HARIANJA")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "50421163":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: ANGEL PANDELAKI")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "50421166":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: ANGGA DAMARA PUTRA")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "50421217":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: ARYA ADHI PRARAMA")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "50421282":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: BINTANG ARMEYELIA")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "50421319":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: DAFFA RIZKY FADILAH")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "50421380":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: DIKA SUGIH ILMAN KUSUMA PUTRA")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "51421591":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: DIO RIZKY ANDIMA")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "50421433":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: Fadhilah Khusnul Khotami")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "50421483":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: FARIS RASYID")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "50421517":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: FIKAR MAULANA")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "50421562":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: Gideon Aprileo")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "50421645":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: IMAM HIDAYAT")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "50421654":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: INDAH TRI ASTUTI")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "50421687":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: JOHANNES TRISNO MANALU")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "50421740":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: KUKUH RAFI HERNAWAN")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "51421646":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: MARSEL CHRISTIAN JUNIOR")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "51421610":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: MARSHALL GUNAPUTRA ARIFIANTO")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "50421856":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: MUHAMAD ALFIN SURYA PRATAMA")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "50421907":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: MUHAMMAD ALFIN FARHANSYAH")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "50421953":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: MUHAMMAD FARHAN FATHURROHMAN")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "51421011":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: MUHAMMAD LUTFI APRIAMTO")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "51421046":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: MUHAMMAD RAIHAN PUTRA")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "51421093":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: Muhammad Try Ramdhani")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "51421106":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: NABILA DHEA HERLANGGENG")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "51421163":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: OKKY DHELFILANO")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "51421210":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: RAFLY RAMADAN")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "51421212":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: RAHADANI SYIFARIANI")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "51421272":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: REDIYA VIO DARMAWAN")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "51421335":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: RIZA PUTRA OCTAVIANTORO")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "51421398":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: SATRIO WIBOWO")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "51421466":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: TEGAR DWI SEPTIADI")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    elif npm == "51421552":
        pretest = (95+90+80+60+50+90+90+70)/8
        posttest = (95+90+80+50+95+90+20+70)/8
        activity = (20+70+70+70+70+90+20+70)/8
        fnlrpt = (20+70+70+70+70+90+100+70)/8
        exscore = 90
        st.write("Name: ZAHIDAN ARDHIANSYAH")
        st.write("Average pre-test score: ")
        st.write("Average post-test score: ")
        st.write("Average activity score: ")
        st.write("Average final report score: ")
        st.write("Exam Score: ")

    else:
        st.write("NPM not found")

    #estgrade = (pretest+posttest+activity+fnlrpt+exscore)/5
    #if estgrade >= 80:
        #st.write("Estimation grade from LAB TI: A")
    #elif estgrade >= 70:
        #st.write("Estimation grade from LAB TI: B")
    #elif estgrade >= 60:
        #st.write("Estimation grade from LAB TI: C")
    #else:
        #st.write("Estimation grade from LAB TI: D")
    st.balloons()

#/home/mufin/.local/share/virtualenvs/My_Projects-23sAJxQN