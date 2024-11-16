# ZenSwitcher

![image](https://github.com/user-attachments/assets/ee424afb-cd10-4001-a419-f14510a0b7ea)

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

<!--
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
-->

<!-- PROJECT LOGO -->
<div align="center">

  <h3 align="center">Zen Switcher - Profil Değiştirici</h3>

  <p align="center">
    ZenSwitcher, Debug ve Release 'in dışında Release Test, Distrubute vb. ek profillerin ihtiyacını karşılamak amacıyla ortaya çıkmıştır.
    .NET MAUI ile VS üzerinden projeleri yürütürken .xaml dosyalarında ek profillere ihtiyacım oldu. Bir program olsa ve hızlıca path üzerinden erişebilsem, profil değiştirebilsem dedim.
    Ve bu ihtiyacın karşılanması amacıyla ortaya çıkardığım bir ürün oldu.
    <br />
    <br/>
    <a href="#docs"><strong>Nasıl kullanılır?</strong></a>
    <br />
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>İçerik Tablosu</summary>
  <ol>
    <li>
      <a href="#about">Proje Hakkında</a>
      <ul>
        <li><a href="#docs">Dökümanlar</a></li>
        <li><a href="#requirements">Gereksinimler</a></li>
      </ul>
    </li>
    <li>
      <a href="#installations">Kurulum İşlemleri</a>
      <ul>
        <li><a href="#install-windows">Windows</a></li>
        <li><a href="#install-macos">Macos</a></li>
      </ul>
    </li>
    <li><a href="#git">Git Yapısı</a></li>
    <li><a href="#contributers">Emeği Geçenler</a></li>
    <li><a href="#licence">Lisans</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
<p id="about"></p>

## İhtiyaç Senaryosu

<p>
Örneğin, projenizde iki adet profil var. Birisi publish diğeri release. Fakat siz daha fazla profile ihtiyaç duruyorsunuz. Örneğin platforma bağlı bir koşul yazdığımızda #if ANDROID tarzında bir koşul ihtiyacınızı görecektir.
Ancak #if ANDROID bloklarını her kaynak dosyası desteklemeyebilir. Veya #if ANDROID RELEASE TESTING tarzında bir ihtiyacınız olabilir. Bu durumda belirttiğiniz metinleri seçtiğiniz profile göre switchleyen bir mini-program işinizi görebilir. 
</p>

<!-- Documents -->
<p id="docs"></p>

## Kullanım

<p>
Bu bölümde proje ile ilgili yazılı dosyalar ve çizimler bulabilirsiniz.
  
Geliştirici Dökümanları:
*[YemekPOS SharePoint -> Ceppos](https://yemekpos.sharepoint.com/:f:/s/developers-Mobil/Ei9iZ8yhY_JJmaFsV5BVFFIBpV9e3dp4YTVKh9aFSfOHZg?e=0iecOe)*
(Versiyon durumlarını, sürüm notları, geliştirici to-do vb. bilgileri içerir)
  
Analist Dökümanları:
*[YemekPOS SharePoint -> Analiz](https://yemekpos.sharepoint.com/:u:/s/developers-Mobil/EV6_IHceBwVHpN9Vj7qS0IsB7rWGpC2aJ0JKs9cm_1__Qg?e=dAMVKo)*
(Yapısal bilgiler, teknik analiz ve özet şeklinde bir çok bilgi bulunur)
</p>

<p align="right">(<a href="#readme-top">Tepeye dön</a>)</p>

<!-- Requirements -->
<p id="requirements"></p>

## Gereksinimler

<p>
Projeyi çalıştırmak için gerekli olan bazı gereksinimler:

* .NET 8 SDK (8.0.403)
* .NET MAUI
* YemekPOS aboneliği

Projenin kurulumu için lütfen <a href="#installations">Kurulum İşlemleri</a> kısmını ziyaret edin.
</p>

<p align="right">(<a href="#readme-top">Tepeye dön</a>)</p>

<!-- Installations -->
<p id="installations"></p>

## Kurulum İşlemleri

<p>
Cihazınıza projeyi kurabilmek için lütfen işletim sisteminize ve durumunuza uygun olan adımları takip edin.
</p>

<p id="install-windows"></p>

### Sıfırdan Kurulum - Windows

<p>
  <pre>
1- Microsoft 'un Visual Studio dağıtımını (VS) edinelim.
2- VS Installer kullanarak .NET MAUI yüklememizi gerçekleştirelim.
3- GitHub üzerinden repoyu edinelim.
4- Projeyi VS aracılığı ile açalım.
  </pre>
</p>

<p id="install-macos"></p>

### Sıfırdan Kurulum - MacOS

<p>
  <pre>
1- Microsoft 'un Visual Studio Code (VSC) dağıtımını edinelim.
2- VSC 'u açıp .NET MAUI eklentisini yükleyelim.
3- GitHub üzerinden repoyu edinelim.
4- Projeyi VSC aracılığı ile açalım.
  </pre>
</p>

### Mevcut Kurulum - Windows

<p>
Eğer cihazınızda hali hazırda Visual Studio (VS) var ise .NET MAUI paketini VS Installer kullanarak yükleyin.
Eğer cihazınızda hali hazırda .NET MAUI paketi var ise ve proje çalışmıyorsa, Clean, Rebuild adımlarını deneyin. Bunlar herhangi bir sonuç vermiyorsa, sıfırdan kurulum yapmanız zorunlu olacaktır.
</p>

### Mevcut Kurulum - MacOS

<p>
Eğer cihazınızda hali hazırda Visual Studio Code (VSC) var ise .NET MAUI uzantısını VSC 'a ekleyin.
Eğer cihazınızda hali hazırda .NET MAUI paketi var ise ve proje çalışmıyorsa, Clean, Rebuild adımlarını deneyin. Bunlar herhangi bir sonuç vermiyorsa, sıfırdan kurulum yapmanız zorunlu olacaktır.
</p>

### Kurulum vb. eylemler için bazı faydalı komutlar

* Dotnet sürümünü kontrol etmek için
  ```sh
  dotnet --version
  ```
* Dotnet komutlarını kullanarak .Net MAUI yüklemesi yapmak için
  ```sh
  dotnet workload install maui
  ```
* Dotnet komutlarını kullanarak .Net MAUI yüklemesini kaldırmak için
  ```sh
  dotnet workload uninstall maui
  ```

<p align="right">(<a href="#readme-top">Tepeye dön</a>)</p>

<p id="git"></p>

## Git Yapısı

![image](https://github.com/user-attachments/assets/9b3b610d-d308-474b-b4f4-a4da1ccd11c2)

1. Repoyu klonlayın
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
2. Dev branchine geçiş yapın
   ```sh
   git checkout dev
   ```
3. Jira üzerinden dev branchini kullanarak işlerinize ait branchler oluşturun.
4. İşler bittikten sonra mevcut task branchinizi dev branchine merge edin.
5. Test sürümlerini dev üzerinden çıkartın.
6. Testler onaylandıktan sonra main ile dev i merge edin.
7. Deploy işlemini main üzerinden yapın.

<p align="right">(<a href="#readme-top">Tepeye dön</a>)</p>

<!-- CONTRIBUTING -->
<p id="contributers"></p>

## Emeği Geçenler

<p>
Geçmişte projede emeği geçmiş kişiler ilgili kısımlar ile beraber bu bölümde listelenecektir.
</p>

* *[Ali SARIASLAN](http://github.com/alisariaslan)* (Database, QR, YemekPOS)
* *[Harun KIVRAK](http://github.com/)* (UI/UX)
* *[Mehmet GÜLPOLAT](http://github.com/)* (QR, Database)
* *[Mahmut KILIÇ](http://github.com/)* (QR, Database)
* *[Feyza İPEK](http://github.com/)* (YemekPOS)
* *[Anıl ALDOĞAN](http://github.com/)* (YemekPOS)

<p align="right">(<a href="#readme-top">Tepeye dön</a>)</p>

<!-- LICENSE -->
<p id="licence"></p>

## Lisans

<a href="https://www.yemekpos.com/">
   <img src="https://www.yemekpos.com/assets/images/Logo_177x47.svg" alt="yemekpos icon" width="200" height="80">
</a>
<p>
Copyright © 2024 ♥ Yemek POS
</p>

<p align="right">(<a href="#readme-top">Tepeye dön</a>)</p>
