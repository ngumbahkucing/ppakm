import numpy as np 
import pandas as pd 
import pickle
import streamlit as st

from PIL import Image

image = Image.open('Bobot fitur.jpg')

st.header('Prediksi Performa Akademik Mahasiswa')

def main():
    
    
    menu = ["Home","Prediksi Performa Akademik","Data Hasil Prediksi","Nilai Aplikasi","Tentang Aplikasi"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Definisi dan penjelasan")
        st.write('Performa akademik mahasiswa adalah capaian seorang mahasiswa dalam mendapatkan nilai akademik, indikator performa akademik diperoleh dari nilai Indek Prestasi Sementara (IPS) maupun Indek Prestasi Komulatif (IPK).') 
        st.write('Banyak variabel yang mempengaruhi performa akademik mahasiswa baik variabel perilaku didalam pembelajaran maupun variabel lainnya. Pada sistem informasi prediksi performa akademik mahasiswa ini variabel yang digunakan adalah variabel akademik dan non-akademik.') 
        st.write('Variabel akademik adalah variabel yang diperoleh dari kegiatan akademik yaitu variabel IPK/IPS dan perilaku mahasiswa dalam berinteraksi dengan Learning Management System (LMS). Sedangkan variabel non-akademik terdiri dari faktor ekonomi, domisili, gender dan keikutsertaan mahasiswa dalam berorganisasi kampus.')
        st.write('Prediksi performa akademik mahasiswa merupakan aktivitas yang sangat penting, hal ini dikarenakan dengan memprediksi performa akademik mahasiswa, dapat menciptakan peluang untuk meningkatkan hasil pendidikan. Selain itu dengan pendekatan prediksi performa yang efektif, instruktur dapat mengalokasikan sumber daya dan instruksi yang lebih akurat. Prediksi awal performa mahasiswa dapat membantu pengambil keputusan untuk memberikan tindakan pada saat yang tepat dan untuk merencanakan pembelajaran yang tepat dalam meningkatkan tingkat keberhasilan mahasiswa')
        st.write('Performa akademik mahasiswa perlu dipantau dengan cermat untuk membantu lembaga mengidentifikasi mahasiswa yang berisiko gagal, mencegah mereka DO atau lulus terlambat (Nachouki dan Abou Naaj 2022). Performa akademik yang buruk menjadi indikator mahasiswa kesulitan dalam menyesuaikan diri dengan perguruan tinggi dan berpeluang besar untuk putus dekolah/drop out (DO) (Lau 2003). Beberapa dampak negatif dari buruknya performa akademik dan tingginya DO diantaranya yaitu rendahnya tingkat kelulusan tepat waktu (Delen 2010), membuang biaya Pendidikan yang sia-sia (Costa, Bispo, dan Pereira 2018), pengurangan kesempatan hidup secara profesional dan sosial yang berdampak negatif kepada keluarga dan masyarakat (Casanova dkk. 2021), sulitnya perguruan tinggi dalam mendapatkan akreditasi yang baik (Delen, Topuz, dan Eryarsoy 2020), hilangnya kepercayaan dan motivasi untuk melanjutkan Pendidikan (Coussement dkk. 2020), dan lain sebagainya.')    
        st.write('Sistem informasi Prediksi Performa Akademik Mahasiswa ini sangat penting bagi Mahasiswa, Dosen, Staff Akademik dan lainnya. Berdasarkan data yang digunakan untuk membangun model, maka sistem informasi prediksi performa akademik mahasiswa ini sangat baik digunakan untuk memprediksi performa akademik mahasiswa semester dua dan empat')
        st.write('Untuk melakukan prediksi performa akademik mahasiswa, maka silahkan ke menu :blue[Prediksi Performa Akademik], jangan lupa setelah melakukan prediksi silahkan berikan penilaian dan masukan untuk pengembangan aplikasi selanjutnya di menu :blue[Nilai Aplikasi]')

    elif choice == "Prediksi Performa Akademik":

        st.write('Prediksi performa akademik ini menggunakan dua sumber data yaitu data aktifitas mahasiswa di LMS (Moodle) serta data non-akademik (ekonomi, domisili, gender, keikutsertaan mahasiswa dalam berorganisasi kampus). Sistem informasi prediksi ini sangat tepat jika digunakan untuk memprediksi performa akademik mahasiswa semester dua dan empat.')
        
        st.subheader("Masukkan Data Diri Anda")
        nama = st.text_input("Nama")

        status = st.radio(
                'Status',
                ('Mahasiswa', 'Dosen', 'Staff Akademik', 'Lainnya'))

        jenkel = st.radio(
                'Jenis Kelamin',
                ('Pria', 'Wanita'))


        kota_tinggal = st.text_input("Kota Tinggal")


        st.subheader("Masukkan Data Akademik (Kegiatan di LMS)")
        st.write('Perlu dipahami bahwasanya masing-masing fitur memiliki bobot yang berbeda, masing-masing bobot ditunjukkan pada caption fitur')

        col1,col2 = st.columns(2)

        with col1:
            Total_login = st.slider('Jumlah Login LMS :blue[(0,220)]', 0, 132)
            N_access_forum = st.slider('Jumlah Akses Forum LMS :blue[(0,201)]', 0, 3269)
            N_access_didactic_units = st.slider('Jumlah Akses Materi :blue[(0,037)]', 0, 746)
            Total_assignments = st.slider('Jumlah Tugas :blue[(-0,267)]', 0, 4517)
            N_assignments_submitted = st.slider('Jumlah Upload Tugas :blue[(0,431)]', 0, 141)
            N_access_questionnaires = st.slider('Jumlah Membuka Quiz :blue[(0,050)]', 0, 4107)
            N_attempts_questionnaires = st.slider('Jumlah Melengkapi Quiz :blue[(0,035)]', 0, 1908)

        with col2:
            N_answered_questions = st.slider('Jumlah Menjawab Quiz :blue[(0,029)]', 0, 115)
            N_questionnaire_views = st.slider('Jumlah Melihat Quiz :blue[(0,020)]', 0, 4047)
            N_questionnaires_submitted = st.slider('Jumlah Mengirim Quiz :blue[(-0.013)]', 0, 39)
            N_reviews_questionnaire = st.slider('Jumlah Ulasan Quiz :blue[(0,041)]', 0, 596)
            Days_first_access_x = st.slider('Minggu Keberapa Akses LMS :blue[(0,019)]', 0, 3)
            N_entries_course_x = st.slider('Jumlah Masuk Mata Kuliah :blue[(0,119)]', 0, 4842)


        st.subheader("Masukkan Data Non Akademik")

        Gender = st.radio(
                'Jenis Kelamin :blue[(0,056)]',
                ('Pria', 'Wanita'))
        if Gender == 'Pria':
            Gender = 1
        else:
            Gender = 0

        Domicile = st.selectbox(
                'Domisili :blue[(0,120)]',
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
                'Pendapatan Orang Tua :blue[(0,051)]',
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

        Campus_organization = st.slider('Jumlah Organisasi Kampus Yang Diikuti :blue[(0,073)]', 0, 4)


        with open("prediksi_performa_akademik.pkl", "rb") as file:
            model = pickle.load(file)

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
    
#menyimpan data agar bisa didownload di txt
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
                "Gender = " + jekel + "\n" +
                "Domisili = " + str(Domicile) + "\n" +
                "Pendapatan Orang Tua = " + pendap + "\n" +
                "Jumlah Organisasi Kampus Yang Diikuti = " + str(Campus_organization) + "\n" + "\n" +
                
                "#Data Akademik (Kegiatan di LMS)" + "\n" +
                "Jumlah Login LMS = " + str(Total_login) + "\n" +
                "Jumlah Akses Forum LMS = " + str(N_access_forum) + "\n" +
                "Jumlah Akses Materi = " + str(N_access_didactic_units) + "\n" +
                "Jumlah Mengerjakan Tugas = " + str(Total_assignments) + "\n" +
                "Jumlah Tugas = " + str(N_assignments_submitted) + "\n" +
                "Jumlah Membuka Quiz = " + str(N_access_questionnaires) + "\n" +
                "Jumlah Melengkapi Quiz = " + str(N_attempts_questionnaires) + "\n" +
                "Jumlah Menjawab Quiz = " + str(N_answered_questions) + "\n" +
                "Jumlah Melihat Quiz = " + str(N_questionnaire_views) + "\n" +
                "Jumlah Mengirim Quiz = " + str(N_questionnaires_submitted) + "\n" +
                "Jumlah Ulasan Quiz = " + str(N_reviews_questionnaire) + "\n" +
                "Minggu Keberapa Akses LMS = " + str(Days_first_access_x) + "\n" +
                "Jumlah Masuk Mata Kuliah = " + str(N_entries_course_x) + "\n" + "\n" +
                
                "#Hasil Prediksi adalah = " + str(predit)
                )

        st.download_button('Download Hasil Prediksi', data=isi, file_name="Hasil-prediksi.txt")

        df = pd.read_csv("Data_prediksi_pengguna.csv")
        df1 = pd.read_csv("PenilaianMasukan.csv")
        ##st.write(df)

        if st.button('Simpan Data'):
            new_data = {"NIM": Total_login, "Gender": jekel}
            df = df.append(new_data, ignore_index=True)
            df.to_csv("Data_prediksi_pengguna.csv", index=False)


            new_data = {"Nilai": Total_login, "Saran": jekel}
            df1 = df1.append(new_data, ignore_index=True)
            df1.to_csv("PenilaianMasukan.csv", index=False)

            st.write(df1)


    elif choice == "Data Hasil Prediksi":
        st.subheader("Data Hasil Prediksi")
        df = pd.read_csv("Data_prediksi_pengguna.csv")

        v_data = df.iloc[:, 4:22]

        st.write('Data Hasil Prediksi', v_data)

    elif choice == "Nilai Aplikasi":
        st.subheader("Nilai Aplikasi dan Saran")

        st.write('Berikan penilaian terhadap sisterm informasi ini')

        col1,col2 = st.columns(2)

        with col1:

            kemudahan = st.radio(
                'Kemudahan dalam menggunakan sistem',
                ('Sangat Baik', 'Baik', 'Cukup Baik','Kurang Baik'))

            kelengkapan = st.radio(
                'Kelengkapan dalam memprediksi performa akademik',
                ('Sangat Baik', 'Baik', 'Cukup Baik','Kurang Baik'))

            informasi = st.radio(
                'Informasi yang disajikan',
                ('Sangat Baik', 'Baik', 'Cukup Baik','Kurang Baik'))

        with col2:

            kualitas = st.radio(
                'Kualitas sistem informasi',
                ('Sangat Baik', 'Baik', 'Cukup Baik','Kurang Baik'))

            kepuasan = st.radio(
                'Kepuasan dalam menggunakan',
                ('Sangat Puas', 'Puas', 'Cukup Puas','Kurang Puas'))

        saran = st.text_area("Berikan saran untuk pengembangan dimasa mendatang")

        df1 = pd.read_csv("PenilaianMasukan.csv")
        st.write('Data Hasil Penilaian:', df1)

    elif choice == "Tentang Aplikasi":
        st.subheader("Tentang Aplikasi")

        st.write('Sistem Informasi Prediksi Performa Akademik Mahasiswa ini dibuat dengan menggunakan bahasa pemprograman :blue[Python] dan :blue[Streamlit], Sisfo ini menggunakan model yang terbentuk dari algoritma :blue[Gradient Boosting Trees] yang telah dioptimasi hyperparameternya dengan menggunakan algoritma :blue[Gread Search] dalam melakukan prediksi. Sedangkan data yang digunakan untuk membangun model berasal dari data akademik dan non-akademikdemik yang diperoleh dari :blue[Universitas Muria Kudus].')
        st.write('Dalam melakukan prediksi Model ini memiliki tingkat kesalahan sebesar 37%, Adapun nilai bobot dari masing-masing fitur ditunjukkan pada gambar dibawah ini.')

        st.image(image, caption='Bobot Fitur')

if __name__ == '__main__':
    main()
