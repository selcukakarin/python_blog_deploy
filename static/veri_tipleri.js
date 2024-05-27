// Değişken Oluşturma
// değişkenler programlama dillerinde bir veriyi tutacağımız zaman kullandığımız en temel birimlerdir.
// javascriptte değişkenlerimiz var, let ve const anahtar kelimeleriyle oluşturulabiliyor.
// şimdi sadece var anahtar kelimesini göreceğiz. dersimizin ilerleyen kısımlarında let ve const'u da göreceğiz

//var a = 20;
//var b = 10;
//var c = 50;
//
//console.log(a,b,c);

// Primitive
// sayı, yazı, undefined veri tiplerimiz olabilir
// javascript değişken tanımlarken dinamik tipleme yapar

//var a = 10
//var b = 3.14
//console.log(typeof a)
//console.log(typeof b)

//Stringler

//var yazi = "Nova Academy"
//console.log(yazi)
//console.log(typeof yazi)

// Boolean
//var a = true
//console.log(typeof a)

//var a = null;
//console.log(a)
//console.log(typeof a)
// biz burada null diye bir tanımlama yaparsak, javascript bu null tanımlamasını c veya c++ daki null pointer'ı olarak algılıyor.
// ve buna göre object olarak yazıyor. Ama biz bu kadar detaya girmeyeceğiz. Derslerimiz ilerlediği zaman siz
// bunların ne anlama geldiğini daha iyi anlayacaksınız.
// bu null tanımlamasıyla hiçbir veri taşımayan bir değişken oluşturduğumuzu bilseniz yeterli.
// bu null değer bizim şu şekilde karşımıza çıkabilir. Biz html elementlerimiz arasında var olmayan bir elemanı seçersek
// bu değer bizim karşımıza null diye gelir. Bu durumları yönetebilmek için gelen değerin null olup olmadığını bulup
// ona göre işlem yaptırabiliriz.

// referans tip - reference type

// şimdi ben size javascriptteki arraylerin, objectlerin, date objectlerin veya functionların birer referans object olduğunu
// göstermek istiyorum. javascriptte typeof metoduyla tipi object olarak gözüken tüm veri tipleri referans veri tipleridir.
//var numbers = [1,2,3,4,5]
//
// array
//console.log(numbers);
//console.log(numbers[0])
//console.log(numbers[3])
//console.log(typeof numbers)

// object
//var person = {
//    name: "Selçuk Akarın",
//    age: 29
//}
//console.log(person)
//console.log(typeof person)

// date
//var date = new Date();
//console.log(date);
//console.log(typeof date);

//var merhaba = function(){
//    console.log("Merhaba");
//}
//
//console.log(merhaba)
//console.log(typeof merhaba)

// primitive veritipleri ile referans veri tipleri arasındaki fark
// primitive veri tipleri sadece o değişkenin değeridir.
// referans veri tipleri bize o referans üzerinden bellekte bir yeri işaret ediyor ve biz bu adrese gidip o adresteki
// veriye ulaşabiliyoruz.

// primitive
//var a = 10;
//// adres kopyalanmadı, sadece değer kopyalandı
//// a = 10
//// b = 10
//var b = a;
//console.log(a,b)
//a = 20
//console.log(a,b)
//
//// aynı şeyi referans tip için yapalım
//var liste1 = [1,2,3];
//// liste2'ye adres ataması yapıldı.
//var liste2 = liste1;
//console.log(liste1,liste2)
//liste1.push(4)
//console.log(liste1,liste2)