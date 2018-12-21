Summary: Library for full screen [S]VGA graphics
Summary(de):	Library f�r Vollbildschirm-[S]VGA-Grafiken
Summary(es):	Biblioteca para gr�ficos en pantalla llena [S]VGA
Summary(fr):	Une librairie graphique SVGA plein ecran de bas niveau
Summary(pl):	Biblioteki dla pe�noekranowej grafiki [S]VGA
Summary(pt_BR):	Biblioteca para gr�ficos em tela cheia [S]VGA
Summary(ru_RU.KOI8-R):	�������������� ���������� ������������� SVGA �������
Summary(tr):	Tam-ekran [S]VGA �izimleri kitapl���
Summary(uk_UA.KOI8-U):	������Ҧ����� ¦�̦����� �����������ϧ SVGA ���Ʀ��
Name: svgalib
Version: 1.9.25
Release: alt2.4
License: distributable
Group: System/Libraries
Source0: %name-%version.tar
Patch0: %name-alt.patch
Patch1: %name-tmp2TMPDIR.patch
Patch2: %name-threeDKit-make.patch
Patch3: %name-1.9.23-unresolved.patch
Patch4: %name-1.9.25-kernel-2.6.26.patch
Patch5: %name-1.9.25-gtf-patch.patch
Patch6: %name-threeDKit-glibc.patch
Url: http://www.arava.co.il/matan/svgalib/
ExclusiveArch: %ix86 x86_64

BuildRequires(pre): rpm-build-kernel

%define _sysconfdir	/etc/vga
%define module_source_dir kernel/svgalib_helper
%define module_name	svgalib_helper

%def_disable static

Packager: L.A.Kostis <lakostis@altlinux.ru>

%description
The svgalib package provides the SVGAlib low-level graphics library
for Linux. SVGAlib is a library which allows applications to use full
screen graphics on a variety of hardware platforms. Many games and
utilities use SVGAlib for their graphics.

%description -l de
SVGAlib ist eine Library, die es Applikationen gestattet, auf einer
Reihe von Plattformen Vollbild-Grafiken zu benutzen. Viele Games und
Utilities nutzen diese Library f�r den Grafikzugriff, da sie f�r
Maschinen mit wenig Speicher besser geeignet ist als X-Windows.

%description -l es
SVGAlib es una biblioteca que permite a las aplicaciones usar gr�ficos
de pantalla llena en una variedad de plataformas de hardware. Muchos
juegos y utilitarios son puestos a disposici�n para usar la SVGAlib
para acceso a gr�ficos, pues es m�s indicado en m�quinas con poca
memoria para ejecutar un sistema X Window.

%description -l fr
Le package svgalib apporte la librairie graphique SVGAlib de bas
niveau pour Linux. SVGAlib est une librairie qui permet aux
applications d'utiliser des graphismes en plein �cran sur diverses
plateformes mat�rielles. De nombreux jeux et utilitaires utilisent
SVGAlib pour leurs graphismes.

%description -l pl
Biblioteki dla pe�noekranowej grafiki [S]VGA. Wiele gier i program�w
u�ytkowych korzysta z tych bibliotek, gdy� wymagaj� mniej pami�ci ni�
X Window System.

%description -l pt_BR
SVGAlib � uma biblioteca que permite a aplica��es usar gr�ficos de
tela cheia em uma variedade de plataformas de hardware. Muitos jogos e
utilit�rios s�o disponibilizados para usar a SVGAlib para acesso a
gr�ficos, pois ele � mais indicado em m�quinas com pouca mem�ria para
rodar um sistema X Window.

%description -l ru_RU.KOI8-R
�������������� ����������� ���������� SVGAlib ������������ ������ �
������������ �������� VGA � SVGA � �������. SVGAlib ���������
����������� ������������ ������������� ������� �� �������������
���������� ����������.

���������� ��������� ��� � ������, ������������ SVGAlib ��� ������
�������. ��� ���������� ����� ���������� svgalib, ���� �� �����������
����� ���������.

%description -l tr
SVGAlib, de�i�ik donan�m platformlar� �zerinde, uygulamalar�n tam
ekran �izim kullanmalar�n� sa�layan bir kitapl�kt�r. Az bellekli
makinalar i�in X Windows'tan daha uygun olmas�n�n yan�s�ra, pek �ok
oyun ve yard�mc� programlar �izim eri�imi i�in bu kitapl��� kullan�r.

%description -l uk_UA.KOI8-U
������Ҧ����� ���Ʀ��� ¦�̦����� SVGAlib ��������դ ������ �
���Ʀ����� �������� VGA �� SVGA � �����̦. SVGAlib Ц�����դ
������������ ���Ʀ�� �� Ҧ�����Φ���� ��������� ����������.

���դ ������ ���� �� ���̦�, �˦ �������������� SVGAlib ��� ������
���Ʀ��. ��� ����Ȧ��� ���� ���������� svgalib, ���� �� ������դ����
������ ����������.

%package devel
Summary: Development libraries and include files for [S]VGA graphics
Summary(de):	Entwicklungs-Libraries und INCLUDE-Dateien f�r (S)VGA-Grafik
Summary(es):	Bibliotecas de desarrollo y archivos de inclusi�n para gr�ficos [S]VGA
Summary(fr):	Outils pour d�velopper des programmes utilisant SVGAlib
Summary(pl):	Pliki nag��wkowe i dokumentacja dla [S]VGA
Summary(pt_BR):	Bibliotecas de desenvolvimento e arquivos de inclus�o para gr�ficos [S]VGA
Summary(ru_RU.KOI8-R):	����� ��� ���������� ��������, ������������ SVGAlib
Summary(tr):	[S]VGA grafikleri i�in geli�tirme kitapl�klar� ve ba�l�k dosyalar�
Summary(uk_UA.KOI8-U):	����� ��� �������� �������, �� �������������� SVGAlib
Group: Development/C
Requires: %name = %version

%description devel
The svgalib-devel package contains the libraries and header files
needed to build programs which will use the SVGAlib low-level graphics
library.

%description devel -l de
Dies sind die Libraries und Header-Dateien, die zum Erstellen von
Programmen erforderlich sind, die SVGAlib verwenden. Mit SVGAlib
k�nnen Programme Vollbildgrafiken auf einer Reihe von Plattformen
verwenden, ohne den von X erforderlichen Overhead.

%description devel -l es
Estas son las bibliotecas y archivos de inclusi�n que son necesarios
para construir programas que usan SVGAlib. Permite que los programas
usen gr�ficos de pantalla llena en una variedad de plataformas de
hardware sin el overhead del X.

%description devel -l fr
Le package svgalib-devel contient les librairies et les fichiers
d'ent�tes n�cessaires pour construire des programmes qui utiliseront
la librairie graphique plein �cran de bas-niveau SVGAlib.

%description devel -l pl
Pliki nag��wkowe i dokumentacja dla [S]VGA.

%description devel -l pt_BR
Estas s�o as bibliotecas e arquivos de inclus�o que s�o necess�rios
para construir programas que usam SVGAlib. SVGAlib permite que
programas usem gr�ficos de tela cheia em uma variedade de plataformas
de hardware sem o overhead do X.

%description devel -l ru_RU.KOI8-R
��� �����, ����������� ��� ���������� ��������, ������������
���������� SVGAlib. SVGAlib ��������� ���������� ������������
������������� ������� �� ������������� ���������� ���������� � ���
������������� ��������� ��� ����� X Window.

%description devel -l tr
Bu paket, SVGAlib kitapl���n� kullanan programlar geli�tirmek i�in
gereken ba�l�k dosyalar�n� ve statik kitapl�klar� i�erir.

%description devel -l uk_UA.KOI8-U
�� �����, ����Ȧ�Φ ��� ���Ц��æ� �������, �� ��������������
¦�̦����� SVGAlib. SVGAlib ��� ��������� �����צ��� ��������� �
������������� ���Ʀ��� �� Ҧ�����Φ���� ��������� ���������� �� ���
����Ȧ����Ԧ ��������� ��� ����� X Window.

%package devel-static
Summary: Static [S]VGA graphics librarires
Summary(pl):	Biblioteki statyczne [S]VGA
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com SVGAlib
Summary(ru_RU.KOI8-R):	����������� ���������� ��� ���������� ��������, ������������ SVGAlib
Summary(uk_UA.KOI8-U):	������Φ ¦�̦����� ��� �������� �������, �� �������������� SVGAlib
Group: Development/C
Requires: %name-devel = %version

%description devel-static
Static [S]VGA graphics librarires.

%description devel-static -l pl
Biblioteki statyczne [S]VGA.

%description devel-static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com SVGAlib.

%description devel-static -l ru_RU.KOI8-R
��� �����, ����������� ��� ���������� ��������, ������������
���������� SVGAlib. SVGAlib ��������� ���������� ������������
������������� ������� �� ������������� ���������� ���������� � ���
������������� ��������� ��� ����� X Window.

%description devel-static -l uk_UA.KOI8-U
�� �����, ����Ȧ�Φ ��� ���Ц��æ� �������, �� ��������������
¦�̦����� SVGAlib. SVGAlib ��� ��������� �����צ��� ��������� �
������������� ���Ʀ��� �� Ҧ�����Φ���� ��������� ���������� �� ���
����Ȧ����Ԧ ��������� ��� ����� X Window.

%package utils
Summary: Various utils for using with %name.
Summary(ru_RU.KOI8-R): ��������� ������� ��� %name
Group: System/Configuration/Hardware
Requires: %name = %version-%release

%description utils
Various useful utils for %name.

%description utils -l ru_RU.KOI8-R
��������� ������� ��� %name, ����������� ��������� �����������������, ��
��������� X Window.

%package -n kernel-source-%module_name
Summary: %name kernel helper module sources
Summary(ru_RU.KOI8-R): kernel-space ������ ��� %name 
Group: Development/Kernel


%description -n kernel-source-%module_name
%name kernel helper module sources for Linux kernel.

%description -n kernel-source-%module_name -l ru_RU.KOI8-R
kernel-space ������ ��� %name, ����������� �������� �������������� ������ �
��������������� �� ������� ���������� ������������.

%prep
%setup -q
%set_verify_elf_method textrel=relaxed
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p2
%patch6 -p2

# remove backup of svgalib.7 - we don't want it in package
rm -f doc/man7/svgalib.7?*

%build
%ifarch %ix86
NOASM=n
%else
NOASM=y
%endif
MOPT="%optflags"

%__mkdir_p sharedlib
ln -sf libvga.so.%version sharedlib/libvga.so
ln -sf libvgagl.so.%version sharedlib/libvgagl.so
%__make CC=%__cc OPTIMIZE="$MOPT" NO_ASM="$NOASM" shared

%__make CC=%__cc LDFLAGS="-L../sharedlib" OPTIMIZE="$MOPT" -C utils
%ifarch %ix86
%__make CC=%__cc CFLAGS="$MOPT" -C lrmi-0.9
%endif
%__make CC="%__cc -L../sharedlib $MOPT" -C threeDKit
%if_enabled static
%__make CC=%__cc OPTIMIZE="$MOPT" NO_ASM="$NOASM" static
%__make CC="%__cc $MOPT" -C threeDKit lib3dkit.a
%endif #static

%install
%__subst 's,\/lib\/,/$(libdir)/,' Makefile
%__make install TOPDIR=%buildroot libdir=%buildroot%_libdir sharedlibdir=%buildroot%_libdir

%if_enabled static
%__make installstaticlib
%__install threeDKit/lib3dkit.a %buildroot%_libdir/
%endif #static
%__mkdir_p %buildroot%_localstatedir/%name

# for separate helper build
%__cp src/vgaversion.h %module_source_dir
%__cp kernel/svgalib_helper/svgalib_helper.h %buildroot%_includedir/
%__subst 's,"../../src/vgaversion.h","vgaversion.h",' %module_source_dir/main.c

%__mkdir_p %kernel_srcdir
%__mv %module_source_dir kernel-source-%module_name-%version
%__tar -c kernel-source-%module_name-%version | bzip2 -c > \
	%buildroot%_usrsrc/kernel/sources/kernel-source-%module_name-%version.tar.bz2

for i in threeDKit/0-*; do %__cp $i $i.threeDKit; done

%files
%doc doc/{CHANGES*,DESIGN,READ*,TODO} threeDKit/*.threeDKit
%dir %_sysconfdir
%config(noreplace) %verify(not size mtime md5) %_sysconfdir/*
%_libdir/lib*.so.*
%_mandir/man[57]/*

%files devel
%doc demos
%_includedir/*.h
%_libdir/lib*.so
%_man3dir/*
%_man6dir/*

%if_enabled static
%files devel-static
%_libdir/lib*.a
%endif #static

%files utils
%_bindir/*
%_mandir/man[18]/*
%dir %_localstatedir/%name

%files -n kernel-source-%module_name
%_usrsrc/kernel

%changelog
* Sun May 22 2016 L.A. Kostis <lakostis@altlinux.ru> 1.9.25-alt2.4
- Fix build with recent glibc.

* Thu Mar 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.25-alt2.3
- Rebuilt for debuginfo

* Wed Dec 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.25-alt2.2
- Rebuilt for soname set-versions

* Wed Sep 02 2009 L.A. Kostis <lakostis@altlinux.ru> 1.9.25-alt2.1
- fix build with recent glibc.
- remove obsoleted macros.

* Wed Sep 17 2008 L.A. Kostis <lakostis@altlinux.ru> 1.9.25-alt2
- fix build with new glibc-kernheaders.
- s/kernel-build-tools/rpm-build-kernel/g

* Wed Sep 27 2006 L.A. Kostis <lakostis@altlinux.ru> 1.9.25-alt1
- new version.
- cleanup .spec & remove obsoleted patches.
- add svga_helper.h to -devel as requires for vidix.
- switch to lrmi-0.9.

* Wed Aug 16 2006 LAKostis <lakostis at altlinux.org> 1.9.23-alt2.1
- add x86_64 support.
- fix libdir.

* Wed Jul 12 2006 L.A. Kostis <lakostis@altlinux.ru> 1.9.23-alt2
- fix unresolved symbols in sharedlibs.

* Mon Dec 12 2005 LAKostis <lakostis at altlinux.ru> 1.9.23-alt1
- new version.
- update DESTDIR patch and remove unwanted 0-README (it's svgalib(7) actual).
- update kernel_helper for 2.6.14 kernel.
- disable -static build by default.

* Sun Jun 19 2005 LAKostis <lakostis at altlinux.ru> 1.9.21-alt1.1
- use memcpy instead loop.
- add BuildPreReq.

* Sat Jun 18 2005 LAKostis <lakostis at altlinux.ru> 1.9.21-alt1
- adopted spec & patches from PLD.
- make separate kernel-source package.
- make separate utils package.
- add demos to -devel package for future testing purposes.

