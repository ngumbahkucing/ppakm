import numpy as np 
import pandas as pd 
import pickle
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu


from PIL import Image
import sklearn

image = Image.open('Bobot fitur.jpg')




def main():
    print(sklearn.__version__)
    choice = option_menu(None, ["Beranda","Prediksi","Hasil","Penilaian","Tentang"], 
    icons=['house','trophy', 'camera', 'list-task', 'book'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
    st.header('Prediksi Performa Akademik Mahasiswa')
    st.write('Oleh Sri Handayani') 
        
    if choice == "Beranda":
        st.subheader("Definisi dan penjelasan")
        st.write('Kinerja akademis mahasiswa mengacu pada pencapaian seorang mahasiswa dalam aspek nilai akademik, yang diukur melalui Indeks Prestasi Semester (IPS) dan Indeks Prestasi Kumulatif (IPK).') 
        st.write('Banyak variabel yang mempengaruhi performa akademik mahasiswa baik variabel perilaku didalam pembelajaran maupun variabel lainnya. Pada sistem informasi prediksi performa akademik mahasiswa ini variabel yang digunakan adalah variabel akademik dan non-akademik.') 
        st.write('Analisis prediksi kinerja akademis mahasiswa berperan vital dalam meningkatkan kualitas pendidikan. Melalui prediksi ini, pendidik dapat menyusun strategi dan alokasi sumber daya yang lebih tepat guna. Prediksi yang dilakukan sejak dini memungkinkan pengambil keputusan untuk mengidentifikasi mahasiswa yang membutuhkan bantuan lebih lanjut, sehingga dapat merencanakan program pembelajaran yang meningkatkan peluang sukses mereka.')
        st.write('Sistem Analisis Prediksi Kinerja Akademis Mahasiswa ini menjadi alat penting bagi Mahasiswa, Dosen, dan Staf Akademik. Dengan berbasis pada data yang digunakan untuk membangun model prediksi, sistem ini sangat efektif untuk memproyeksikan kinerja akademis mahasiswa.')
        st.write('Untuk memulai analisis prediksi kinerja akademis mahasiswa, silakan kunjungi menu Prediksi. Setelah melakukan prediksi, jangan ragu untuk memberikan feedback dan saran untuk pengembangan sistem lebih lanjut melalui menu Penilaian.')


    elif choice == "Prediksi":

        st.write('Prediksi performa akademik ini menggunakan dua sumber data yaitu 1). Data Akademik Mahasiswa IPK Semester dan Data Nilai Ijazah Calon Mahasiswa  2). Data non-akademik (gender, umur, gaji orang tua, jumlah saudara).')
        
        st.subheader("Masukkan Data Diri Anda")
        nama = st.text_input("Nama Lengkap")

        status = st.radio(
            'Status',
            ('Mahasiswa', 'Calon Mahasiswa'))


        st.subheader("Masukkan Data Akademik")

        if status == "Mahasiswa":
            Ipk = st.text_input('IPK Semester Lalu')
            Ijazah = 0
            Semester = st.selectbox('Semester ke-', ('2','3','4'))
            Prestasi = st.selectbox('Prestasi', ('Tidak Ada','Akademik','Non-Akademik'))
            if Prestasi == "Tidak Ada":
                Prestasi = 0;
            elif Prestasi == "Akademik":
                Prestasi = 1;
            else:
                Prestasi = 2;
        else:
            Ipk = 0
            Semester = 0
            Ijazah = st.text_input('Nilai Ijazah')
            Prestasi = st.selectbox('Prestasi', ('Tidak Ada','Akademik','Non-Akademik'))
            if Prestasi == "Tidak Ada":
                Prestasi = 0;
            elif Prestasi == "Akademik":
                Prestasi = 1;
            else:
                Prestasi = 2;        

        st.subheader("Masukkan Data Non Akademik")

        Gender = st.radio(
            'Jenis Kelamin',
            ('Pria', 'Wanita'))
        if Gender == 'Pria':
            Gender = 1
        else:
            Gender = 0

        Umur = st.text_input("Umur")

        Saudara = st.text_input("Jumlah Saudara")
            
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

        with open("prediksi_performa_akademik.sav", "rb") as file:
            model = pickle.load(file)

        predit = ''

        ipk = Ipk
        umur = Umur
        semester = Semester
        saudara = Saudara

        if Gender == 1:
            jekel = "Pria"
        else: 
            jekel ="Wanita"

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


        if st.button('Prediksi Performa'):
            predit = model.predict(
                [[Gender, Economy, Ipk]]
            )
            st.success (f"Hasil Prediksi : %.2f" % predit)

            #Simpan data
            df = pd.read_csv("Data_prediksi_pengguna.csv")
            new_data = {"Nama":nama, "Status":status, "Jenis Kelamin":jekel, "Umur":umur,
                        "Nilai Ijazah":Ijazah, "IPK":ipk, "Semester": semester,
                        "Ekonomi":pendap, "Saudara":saudara, "Hasil Prediksi":predit
                        }

            df = df.append(new_data, ignore_index=True)
            df.to_csv("Data_prediksi_pengguna.csv", index=False)
            v_data = df.iloc[:, 1:9]
            vlast= v_data.tail(1)
            st.dataframe(vlast.set_index(vlast.columns[0]))
            

        #menyimpan data agar bisa didownload di txt
        isi = ( "Prediksi Performa Akademik Mahasiswa Menggunakan Data Non-Akademik dan Akademik" + "\n" + "\n" +
                "#Data Non Akademik" + "\n" +
                "Gender = " + jekel + "\n" +
                "Umur = " + umur + "\n" +
                "Pendapatan Orang Tua = " + pendap + "\n" +
                "Jumlah Saudara = " + saudara + "\n" +
                
                "#Data Akademik" + "\n" +
                "IPK = " + str(Ipk) + "\n" +
                "Nilai Ijazah = " + str(Ijazah) + "\n" +
                "Prestasi = " + str(Prestasi) + "\n" +
                
                "#Hasil Prediksi adalah = " + str(predit)
                )

        st.download_button('Download Hasil Prediksi', data=isi, file_name="Hasil-prediksi.txt")


    elif choice == "Hasil":
        st.subheader("Data Hasil Prediksi")
        df = pd.read_csv("Data_prediksi_pengguna.csv")
        v_data = df.iloc[:, 1:9]
        st.dataframe(v_data.set_index(v_data.columns[0]))
        
    elif choice == "Penilaian":
        st.subheader("Nilai Aplikasi dan Saran")
        st.write('Berikan penilaian terhadap sistem ini')

        form= st.form("myform",clear_on_submit=True)
        col1,col2 = form.columns(2)
        with col1:

                kemudahan = st.radio(
                    'Kemudahan dalam menggunakan sistem',
                    ('Sangat Baik', 'Baik', 'Cukup Baik','Kurang Baik'))

                if kemudahan == 'Sangat Baik':
                    kemudahan = 4
                elif kemudahan == 'Baik':
                    kemudahan = 3 
                elif kemudahan == 'Cukup Baik':
                    kemudahan = 2 
                else:
                    kemudahan = 1

                kelengkapan = st.radio(
                    'Kelengkapan dalam memprediksi performa akademik',
                    ('Sangat Baik', 'Baik', 'Cukup Baik','Kurang Baik'))

                if kelengkapan == 'Sangat Baik':
                    kelengkapan = 4
                elif kelengkapan == 'Baik':
                    kelengkapan = 3 
                elif kelengkapan == 'Cukup Baik':
                    kelengkapan = 2 
                else:
                    kelengkapan = 1

                informasi = st.radio(
                    'Informasi yang disajikan',
                    ('Sangat Baik', 'Baik', 'Cukup Baik','Kurang Baik'))

                if informasi == 'Sangat Baik':
                    informasi = 4
                elif informasi == 'Baik':
                    informasi = 3 
                elif informasi == 'Cukup Baik':
                    informasi = 2 
                else:
                    informasi = 1

        with col2:

                kualitas = st.radio(
                    'Kualitas sistem informasi',
                    ('Sangat Baik', 'Baik', 'Cukup Baik','Kurang Baik'))

                if kualitas == 'Sangat Baik':
                    kualitas = 4
                elif kualitas == 'Baik':
                    kualitas = 3 
                elif kualitas == 'Cukup Baik':
                    kualitas = 2 
                else:
                    kualitas = 1

                kepuasan = st.radio(
                    'Kepuasan dalam menggunakan',
                    ('Sangat Puas', 'Puas', 'Cukup Puas','Kurang Puas'))

                if kepuasan == 'Sangat Puas':
                    kepuasan = 4
                elif kepuasan == 'Puas':
                    kepuasan = 3 
                elif kepuasan == 'Cukup Puas':
                    kepuasan = 2 
                else:
                    kepuasan = 1

        saran = form.text_area("Berikan saran untuk pengembangan sistem informasi ini dimasa mendatang")

        submit_button=form.form_submit_button("Simpan")

            #Simpan data penilaian
        if submit_button:
            dfs = pd.read_csv("PenilaianMasukan.csv")
            new_data = {"Kemudahan Penggunaan":kemudahan, "Kelengkapan Prediksi":kelengkapan, 
                        "Informasi Yang Disajikan":informasi, "Kualitas Sistem Informasi":kualitas, 
                        "Kepuasan Penggunaan":kepuasan, "Masukan":saran
                        }

            dfs = dfs.append(new_data, ignore_index=True)
            dfs.to_csv("PenilaianMasukan.csv", index=False)

            form.info("Data berhasil disimpan, Terima kasih atas penialaian dan saran Anda")


        df1 = pd.read_csv("PenilaianMasukan.csv")
        #st.write('Data Hasil Penilaian:', df1)  #Menampilkan tabel penilaian

        st.write('**Grafik Hasil Penilaian Pengguna**')

        colo1,colo2 = st.columns(2)
        with colo1:
            #Grafik penilaian kemudahan penggunaan
            st.write('*Kemudahan Penggunaan*')
            x= df1['Kemudahan Penggunaan'].tolist()
            count_value = 1
            counti = x.count(count_value)
            count_value = 2
            counti1 = x.count(count_value)
            count_value = 3
            counti2 = x.count(count_value)
            count_value = 4
            counti3 = x.count(count_value)

            # Pie chart
            labels = 'Kurang Baik', 'Cukup Baik', 'Baik', 'Sangat Baik'
            sizes = [counti, counti1, counti2, counti3]
            explode = (0, 0.05, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            #ax1.set_title("Kemudahan Penggunaan")
            st.pyplot(fig1)

            #Grafik penilaian kelengkapan prediksi
            st.write('*Kelengkapan Prediksi*')
            xs=df1['Kelengkapan Prediksi'].tolist()
            count_value2 = 1
            counti = xs.count(count_value2)
            count_value2 = 2
            counti1 = xs.count(count_value2)
            count_value2 = 3
            counti2 = xs.count(count_value2)
            count_value2 = 4
            counti3 = xs.count(count_value2)

            # Pie chart
            labels = 'Kurang Baik', 'Cukup Baik', 'Baik', 'Sangat Baik'
            sizes = [counti, counti1, counti2, counti3]
            explode = (0, 0.05, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig1)

            #Grafik penilaian informasi yang disajikan
            st.write('*Informasi Yang Disajikan*')
            xs2=df1['Informasi Yang Disajikan'].tolist()
            count_value = 1
            counti = xs2.count(count_value)
            count_value = 2
            counti1 = xs2.count(count_value)
            count_value = 3
            counti2 = xs2.count(count_value)
            count_value = 4
            counti3 = xs2.count(count_value)
       
            # Pie chart
            labels = 'Kurang Baik', 'Cukup Baik', 'Baik', 'Sangat Baik'
            sizes = [counti, counti1, counti2, counti3]
            explode = (0, 0.05, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            st.pyplot(fig1)

        with colo2:
            #Grafik penilaian kualitas sistem informasi
            st.write('*Kualitas Sistem Informasi*')
            xs3=df1['Kualitas Sistem Informasi'].tolist()
            count_value = 1
            counti = xs3.count(count_value)
            count_value = 2
            counti1 = xs3.count(count_value)
            count_value = 3
            counti2 = xs3.count(count_value)
            count_value = 4
            counti3 = xs3.count(count_value)

            #Bar chart
            #sizes = pd.DataFrame({
            #    'index': ['Kurang Baik', 'Cukup Baik', 'Baik', 'Sangat Baik'],
            #    'Penilaian':[counti, counti1, counti2, counti3],
            #}).set_index('index')
            #st.bar_chart(sizes)
            labels = 'Kurang Baik', 'Cukup Baik', 'Baik', 'Sangat Baik'
            sizes = [counti, counti1, counti2, counti3]
            fig5, ax5 = plt.subplots()
            plt.bar(labels, sizes)
            ax5.set_ylabel("Penilaian")
            ax5.set_xlabel("Kategori Nilai")
            #ax5.set_title("Layanan")
            #plt.grid(axis='y')
            st.pyplot(fig5)
         
            #Grafik penilaian kepuasan pengguna
            st.write('*Kepuasan Penggunaan*')
            xs4=df1['Kepuasan Penggunaan'].tolist()
            count_value = 1
            counti = xs4.count(count_value)
            count_value = 2
            counti1 = xs4.count(count_value)
            count_value = 3
            counti2 = xs4.count(count_value)
            count_value = 4
            counti3 = xs4.count(count_value)
           
            #Bae chart
            labels = 'Kurang Puas', 'Cukup Puas', 'Puas', 'Sangat Puas'
            sizes = [counti, counti1, counti2, counti3]
       
            fig5, ax5 = plt.subplots()
            plt.bar(labels, sizes)
            ax5.set_ylabel("Penilaian")
            ax5.set_xlabel("Kategori Nilai")
            #ax5.set_title("Layanan")
            #plt.grid(axis='y')
            st.pyplot(fig5)

    elif choice == "Tentang":
        st.subheader("Tentang Aplikasi")
        st.write('Sistem Informasi Prediksi Performa Akademik Mahasiswa ini dibuat dengan menggunakan bahasa pemprograman :blue[Python] dan :blue[Streamlit], sistem ini menggunakan model yang terbentuk dari algoritma :blue[LSTM dan SVM]. Sedangkan data yang digunakan untuk membangun model berasal dari data akademik dan data non-akademikdemik yang diperoleh dari :blue[Universitas Semarang].')
        st.write('Dalam melakukan prediksi Model ini memiliki tingkat kesalahan sebesar 22%')

        #st.image(image, caption='Bobot Fitur')

        st.write('Untuk informasi lebih lanjut terkait Prediksi Performa Akademik Mahasiswa ini, dapat menghubungi Sri Handayani: 081232566827 ')

        txt_input= st.text_input('Masukkan Kode Download, Untuk Mendownload Hasil Prediksi', type="password")

        with open('PenilaianMasukan.csv','rb') as f:
            if txt_input == "rahasia":    
                st.download_button('Download Penilaian', f, file_name='PenilaianMasukan.csv', disabled=not txt_input)  # Defaults to 'text/plain'

        with open('Data_prediksi_pengguna.csv','rb') as f:
           if txt_input == "rahasia": 
                st.download_button('Download Hasil Prediksi', f, file_name='HasilPrediksi.csv')  # Defaults to 'text/plain'


if __name__ == '__main__':
    main()
