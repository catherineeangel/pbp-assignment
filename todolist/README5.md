# Assignment 5

<br>

<!--  Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
 Jelaskan tag HTML5 yang kamu ketahui.
 Jelaskan tipe-tipe CSS selector yang kamu ketahui.
 Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas. -->

## perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style <hr>

Inline CSS adalah cara penulisan styling CSS yang dilakukan langsung dalam tag elemen yang bersangkutan. Hal ini membuat stylingnya spesifik pada satu elemen dan tidak dependen dengan styling lainnya.
Contoh penulisan inline CSS :

```
<p style="color:blue;text-align:center;">Hello World</p>

```

Internal CSS adalah cara penulisan CSS yang berada di file yang sama pada file HTML. Styling CSS tersebut unik untuk file HTML itu saja.
Internal CSS ditulis menggunakan tag `<style> .selector {styling properties} </style>`.

Eksternal CSS adalah cara penulisan CSS pada satu file yang terpisah dari HTML. Untuk menggunakan CSS tersebut pada file HTML gunakan tag `<link rel="stylesheet" href="mystyle.css">`. File yang dituliskan dalam href adalah nama file .css yang telah dibuat.
Isi dari file CSS eksternal akan mengubah styling untuk semua file .html.

## Jelaskan tag HTML5 yang kamu ketahui. <hr>

Beberapa tag HTML yang umum digunakan adalah :  
`<head>` :  
`<body>` : berisi data yang ingin ditampilkan di website  
`<h1>, <h2>, <h3>, dst` : tag heading dari 1-6 dengan 1 ukuran paling gede  
`<p>` : paragraph, untuk text
`<div>` : division, sebagai container
`<form>` : untuk membuat form
`<input>` : untuk menerima input dari user

## Jelaskan tipe-tipe CSS selector yang kamu ketahui. <hr>

Ada 6 tipe selector CSS:

1. Tag : disebut juga type selector, memilih elemen berdasarkan tag. --> seperti tag p, button, table, dst

```
p {
    insert code here
}
```

2. Class : memilih elemen berdasarkan nama class yang sudah diberikan --> `<p class="nama-class"></p>`

```
.nama-class {
    insert code here
}
```

3. ID : memilih elemen berdasarkan id --> `<p id="nama-id"></p>`

```
#nama-id {
    insert code here
}
```

4. Atribut : memilih elemen berdasarkan attribut dari sebuah tag. Misal tag input memiliki beberapa tipe, salah satunya adalah text.

```
input[type=text] {
    insert code here
}
```

5. Universal : sesuai namanya selektor iniberlaku untuk semua atribut,

```
* {
    insert code here
}
```

6. Pseudo :
   a. pseudo-class : untuk state element, seperti saat di click, hover, dst

```
a:hover {
    insert code here
}
```

b. pseudo-element : untuk element semu di HTML , misal seperti elemen di dalam elemen

```
p span{
    insert code here
}
```

potongan kode diatas berarti styling akan berpengaruh pada elemen span yang berada di dalam tag p.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas <hr>

1. Install tailwind dengan mengikuti tutorial dari website [ini](https://django-tailwind.readthedocs.io/en/latest/installation.html).
2. Style card yang akan digunakan untuk task dengan membuat div sebagai container card.
3. Tambahkan styling, seperti warna, rounded, gap, margin, dll.
4. Pastikan responsif.
5. Deploy
