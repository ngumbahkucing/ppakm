import pickle
import streamlit as st

model = pickle.load(open('prediksi_performa_akademik.sav', 'rb'))

st.title('Prediksi Performa Akademik Mahasiswa')

st.subheader("Masukkan Data Non Akademik")

Gender = st.radio(
        'Jenis Kelamin',
        ('Pria', 'Wanita'))
if Gender == 'Pria':
    Gender = 1
else:
    Gender = 0

Domicile = st.selectbox(
        'Domisili',
        ('Dalam Kota', 'Kota Sebelah', 'Jarak Satu Kota', 'Dalam Satu Pulau', 'Diluar Pulau'))

if Domicile == 'Dalam Kota':
    Domicile = 1
elif Domicile == 'Kota Sebelah':
    Domicile = 2
elif Domicile == 'Jarak Satu Kota':
    Domicile = 3
elif Domicile == 'Dalam Satu Pulau':
    Domicile = 4
else : Domicile = 5

Economy = st.selectbox(
        'Pendapatan Orang Tua',
        ('100.000 - 600.000', '500.000 - 1.000.000', '1.000.000 - 2.500.000', 
            '2.500.000 - 5.000.000', '5.000.000 - 7.500.000',
            '7.500.000 - 10.000.000', '> 10.000.000')) 
if Economy == '100.000 - 600.000':
    Economy = 1
elif Economy == '500.000 - 1.000.000':
    Economy = 2
elif Economy == '1.000.000 - 2.500.000':
    Economy = 3
elif Economy == '2.500.000 - 5.000.000':
    Economy = 4
elif Economy == '5.000.000 - 7.500.000':
    Economy = 5
elif Economy == '7.500.000 - 10.000.000':
    Economy = 6
else:
    Economy = 7

Campus_organization = st.slider('Jumlah Organisasi Kampus Yang Diikuti', 0, 4)

st.subheader("Masukkan Data Akademik (Kegiatan di LMS)")

col1,col2 = st.columns(2)

with col1:
    Total_login = st.slider('Jumlah Login LMS', 0, 132)
    N_access_forum = st.slider('Jumlah Akses Forum LMS', 0, 3269)
    N_access_didactic_units = st.slider('Jumlah Didactic Unit', 0, 746)
    Total_assignments = st.slider('Jumlah Mengerjakan Tugas', 0, 4517)
    N_assignments_submitted = st.slider('Jumlah Upload Tugas', 0, 141)
    N_access_questionnaires = st.slider('Jumlah Membuka Quiz', 0, 4107)
    N_attempts_questionnaires = st.slider('Jumlah Melengkapi Quiz', 0, 1908)

with col2:
    N_answered_questions = st.slider('Jumlah Menjawab Quiz', 0, 115)
    N_questionnaire_views = st.slider('Jumlah Melihat Quiz', 0, 4047)
    N_questionnaires_submitted = st.slider('Jumlah Mengirim Quiz', 0, 39)
    N_reviews_questionnaire = st.slider('Jumlah Mengoreksi Quiz', 0, 596)
    Days_first_access_x = st.slider('Minggu Keberapa Akses LMS', 0, 3)
    N_entries_course_x = st.slider('Jumlah Masuk LMS', 0, 4842)


predit = ''

if st.button('Prediksi Performa'):
    predit = model.predict(
        [[Gender, Domicile, Economy, Campus_organization, 
          Total_login, N_access_forum, N_access_didactic_units, 
          Total_assignments, N_assignments_submitted, N_access_questionnaires, 
          N_attempts_questionnaires, N_answered_questions, 
          N_questionnaire_views, N_questionnaires_submitted, 
          N_reviews_questionnaire, Days_first_access_x, N_entries_course_x]]
    )
    st.success (f"Hasil Prediksi : %.2f" % predit)
    

if Gender == 1:
    jekel = "Pria"
else: jekel ="Wanita"

if Economy == 1:
    pendap = '100.000 - 600.000'
elif Economy == 2:
    pendap = '500.000 - 1.000.000'
elif Economy == 3:
    pendap = '1.000.000 - 2.500.000'
elif Economy == 4:
    pendap = '2.500.000 - 5.000.000'
elif Economy == 5:
    pendap = '5.000.000 - 7.500.000'
elif Economy == 6:
    pendap = '7.500.000 - 10.000.000'
else:
    pendap = '> 10.000.000'


isi = ( "Prediksi Performa Akademik Mahasiswa Menggunakan Data Non-Akademik dan Akademik" + "\n" + "\n" +
        "#Data Non Akademik" + "\n" +
        "Jenis Kelamin = " + jekel + "\n" +
        "Domisili = " + str(Domicile) + "\n" +
        "Pendapatan Orang Tua = " + pendap + "\n" +
        "Jumlah Organisasi Kampus Yang Diikuti = " + str(Campus_organization) + "\n" + "\n" +
        
        "#Data Akademik (Kegiatan di LMS)" + "\n" +
        "Jumlah Login LMS = " + str(Total_login) + "\n" +
        "Jumlah Akses Forum LMS = " + str(N_access_forum) + "\n" +
        "Jumlah Didactic Unit = " + str(N_access_didactic_units) + "\n" +
        "Jumlah Mengerjakan Tugas = " + str(Total_assignments) + "\n" +
        "Jumlah Upload Tugas = " + str(N_assignments_submitted) + "\n" +
        "Jumlah Membuka Quiz = " + str(N_access_questionnaires) + "\n" +
        "Jumlah Melengkapi Quiz = " + str(N_attempts_questionnaires) + "\n" +
        "Jumlah Menjawab Quiz = " + str(N_answered_questions) + "\n" +
        "Jumlah Melihat Quiz = " + str(N_questionnaire_views) + "\n" +
        "Jumlah Mengirim Quiz = " + str(N_questionnaires_submitted) + "\n" +
        "Jumlah Mengoreksi Quiz = " + str(N_reviews_questionnaire) + "\n" +
        "Minggu Keberapa Akses LMS = " + str(Days_first_access_x) + "\n" +
        "Jumlah Masuk LMS = " + str(N_entries_course_x) + "\n" + "\n" +
        
        "#Hasil Prediksi adalah = " + str(predit)
        )

st.download_button('Download Hasil Prediksi', data=isi, file_name="Hasil-prediksi.txt")