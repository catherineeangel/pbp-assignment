# Assignment 4

### Website Link: [ruby-pbp.herokuapp.com/todolist](https://ruby-pbp.herokuapp.com/todolist)

<br>

## Kegunaan {% csrf_token %} pada elemen `<form>` <hr>

CSRF token diperlukan ketika ingin menggunakan form pada django untuk meminimalisir security atau CSRF (Cross Site Request Forgery) attacks yang rentan terjadi ketika user ingin mengirimkan data ke website (seperti melalui forms). CRSF token merupakan built in feature dari Django yang dapat langsung digunakan oleh developer. CSRF token di Django berupa hidden form field yang berisi kode alphanumeric yang sudah di-generate oleh Django. Token yang digenerate untuk setiap user berbeda dan akan diperbaharui dalam jangka waktu tertentu. Ketika user sudah login dan ingin mengisi form, Django akan mengecek jika crsf tokennya sesuai untuk user tersebut. Jika tidak, berarti ada "man in the middle" yang berpura-pura menjadi user tersebut dan transaksi tidak dapat dilakukan.

Jika tidak ada potongan kode {% csrf_token %} untuk form yang dibuat, maka akan lebih mudah terjadi CSRF attacks untuk user yang mengirimkan data melalui website yang kita buat. Hal ini mengakibatkan kurangnya tingkat keamanan website tersebut.

<br>

## Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat `<form>`secara manual.<hr>

Bisa, form yang dibuat secara manual harus berisi data-data yang dibutuhkan. Lalu, data tersebut bisa didapatkan melalui parameter request di view. Form dapat dibuat secara manual dengan membuat tag `<form>` dan menyisipkin {% csrf_token %} setelahnya. Untuk setiap data yang dibutuhkan, dibuatkan tag `<input name="">` dengan name disesuaikan dengan data yang akan diinput (misal: username. Lalu, tambahkan CTA (call to action) seperti button supaya user dapat mensubmit form tersebut.

<br>

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.<hr>

Setelah user mengisi form dan melakukan submisi, data tersebut akan diolah di views sesuai dengan fungsi yang dibuat. Jika menggunakan forms yang sudah dibuat menggunakan forms dari Django, dapat menggunakan method forms.is_valid() untuk memvalidasi form tersebut. Jika dibuat secara manual, maka untuk mengecek setiap input dapat dilakukan dengan menggunakan request.POST.get(name) dan memvalidasi secara manual. Lalu, untuk menyimpan data pada database dapat menggunakan form.save(). Untuk memunculkan data pada template HTML, kita dapat mengambil data task sebagai berikut :

```
data = Task.objects.filter(user=request.user)
```

Lalu data ini akan di-passing ke template HTML melalui context. Pada HTML, data ini dapat ditampilkan dengan menggunakan syntax {{ data }} atau bisa ditampilkan dengan menggunakan for loop :

```
{% for x in data %}
{{ data.attr }}
{% endfor %}
```

<br>

## Implementasi <hr>

1. Buat app todolist dengan command `djangoadmin startapp todolist`. Tambahkan app todolist ke dalam installed_apps di settings.py.

2. Buat model Task di models.py yang memiliki attribut sebagai berikut:

```
class Task (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)  # menambahkan created at timestamp scr otomatis, gbs di override
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
```

3. Buat form CreateTaskForm di forms.py. Pastikan menggunakan modelForm supaya dapat forms dapat disesuaikan dengan model Task yang sudah dibuat sebelumnya.

```
class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description')
```

4. Buat views.py yang berisi fungsi-fungsi yang dibutuhkan, antara lain :  
   a. login_user  
   Mengambil username dan password yang telah diinput oleh user melalui request.POST.get(name) lalu mengecek apakah user tersebut ada dalam database. 'name' disesuaikan dengan name yang diberikan untuk tag input pada forms.
   User akan di-redirect ke page /todolist yang menampilkan semua todolist user.  
   b. logout_user  
   Logout user dan me-redirect ke page /login. Dalam fungsi ini, cookies untuk user juga dihapus.  
   c. register  
   Mendafatarkan user baru ke database dengan menggunakan UserCreationForms.
   d. show_todolist  
   Mengambil semua todolist sesuai dengan user yang login dan menampilkannya. Tambahkan decorator login_required untuk memastikan user telah login.  
   e. toggle_is_finished  
   Berfungsi untuk mengubah status task dari Open menjadi Closed atau sebaliknya. Fungsi ini dipanggil jika checklist berubah.  
   f. create_task
   Membuat task baru dengan menggunakan form CreateTaskForm yang dibuat di forms.py.  
   g. delete_task  
   Menghapus task berdasarkan id.

5. Buat templates untuk menampilkan website kita kepada user.

   a. register.html  
   b. login.html  
   c. todolist.html  
   d. create-task.html

6. Menambahkan styling dengan menggunakan css pada static/style.css

7. Deploy ke heroku.
