%def_enable shared
%def_enable static
%def_disable debug
#--------------------------------------------------------------------------------
%if "%__cc" == "klcc"
%{?_enable_shared:%def_enable kshared}
%set_disable shared
%set_enable static
%endif

%define Name 4tH
Name: 4th
%define lname lib%name
Version: 3.62.2
Release: alt1
Summary: Basic framework for creating application specific scripting languages
Summary(uk_UA.CP1251): ������ �������� ��� ��������� ����������� ��� ������� ��� �������
Summary(ru_RU.CP1251): ������� �������� ��� �������� ������������� ��� �������� ������ ���������
License: GPLv3+
Group: Development/Other
URL: http://hansoft.come.to/
Source0: %name-%version-unix.tar
Source1: Makefile.ALT
Patch: %name-%version-%release.patch
%{?_enable_shared:Requires: %lname = %version-%release}

%if "%__cc" == "tcc"
BuildRequires: tcc >= 0.9.23-alt3
%endif
%if "%__cc" == "musl-gcc"
BuildRequires: musl-devel
%endif
%if "%__cc" == "klcc"
BuildRequires: klcc >= 2.0.2-alt3
%endif

%description
%Name is basic framework for creating application specific scripting
languages. It is a library of functions centered around a virtual
machine, which guarantees high performance, ease of use and low
overhead. But in the meanwhile %Name has acquired a reputation as an
educational tool. Its simplicity makes it perfectly suited to learn
Forth, from which it has been derived.
This package is an attempt to suit both audiences. It contains
instructions how to modify the package in order to fit your own
requirements. %Name in its current form is a calculator for simple
teletype applications.

%description -l uk_UA.CP1251
%Name - �� ������ �������� ��� ��������� ����������� ��� ������� ���
�������. � ���� - �������� ������� ������� ��������� ������, ���
������� ������ �������������, ������� ������������ �� �������
������� �������. ���, � ��� �� ���, %Name ����� ��������� �� ����������
����������. ������� ���� ������� �� ������ �������� ��� ��������
Forth'� (� ���� ��� � ����������). ����� ����� ���������� ����
�������� ���� ���������. ³� ������ � ���� ���������� � �����������
������ �� ���������� ��������. %Name � ���� ������� ���� - ��
���������� ��� ������� ����������� �������.

%description -l ru_RU.CP1251
%Name - ��� ������� �������� ��� �������� ������������� ��� �������
������ ���������. � ������ - ���������� ������� ������ �����������
������, ������� ����������� ������� ������������������, �������
������������� ��� �������������� ��������� ��������. ��, � �� �� �����,
%Name ������� ��������� ���������� �����������. ��������� ����� ��������
�� ������� �������� ��� �������� Forth'� (� ���� �� � ����������).
������ ����� �������� ���� �������� ����� ����������. �� �������� �
���� ���������� �� ����������� ������ �������� ������ ����������. %Name
� ��� ����������� ����� - ��� ����������� ��� ������� �����������
��������.


%package examples
Group: Development/Other
Summary: Examples for the %Name
Summary(uk_UA.CP1251): �������� ��� %Name
Summary(ru_RU.CP1251): ������� ��� %Name
BuildArch: noarch

%description examples
%Name is basic framework for creating application specific scripting
languages. It is a library of functions centered around a virtual
machine, which guarantees high performance, ease of use and low
overhead. But in the meanwhile %Name has acquired a reputation as an
educational tool. Its simplicity makes it perfectly suited to learn
Forth, from which it has been derived.

This package contains examples for the %Name.

%description -l uk_UA.CP1251 examples
%Name - �� ������ �������� ��� ��������� ����������� ��� ������� ���
�������. � ���� - �������� ������� ������� ��������� ������, ���
������� ������ �������������, ������� ������������ �� �������
������� �������. ���, � ��� �� ���, %Name ����� ��������� �� ����������
����������. ������� ���� ������� �� ������ �������� ��� ��������
Forth'� (� ���� ��� � ����������).

� ����� ����� ����������� �������� ��� %Name.

%description -l ru_RU.CP1251 examples
%Name - ��� ������� �������� ��� �������� ������������� ��� �������
������ ���������. � ������ - ���������� ������� ������ �����������
������, ������� ����������� ������� ������������������, �������
������������� ��� �������������� ��������� ��������. ��, � �� �� �����,
%Name ������� ��������� ���������� �����������. ��������� ����� ��������
�� ������� �������� ��� �������� Forth'� (� ���� �� � ����������).

� ���� ������ ��������� ������� ��� %Name.


%if_enabled shared
%package -n %lname
Group: System/Libraries
Summary: %Name shared library
Summary(uk_UA.CP1251): ��������� %Name
Summary(ru_RU.CP1251): ���������� %Name

%description -n %lname
%Name is basic framework for creating application specific scripting
languages. It is a library of functions centered around a virtual
machine, which guarantees high performance, ease of use and low
overhead. All its basic building blocks (compiler, interpreter,
decompiler, loader and saver) can be called with a single line of C. No
initialization necessary.

This package contains %Name shared library.

%description -n %lname -l uk_UA.CP1251
%Name - �� ������ �������� ��� ��������� ����������� ��� ������� ���
�������. � ���� - �������� ������� ������� ��������� ������, ���
������� ������ �������������, ������� ������������ �� �������
������� �������. �� ���� ����� �������� ����� (����������, �������������,
������������, ������������ �� �������) ������ ���� �������� �����
������ � C, ������� � ����������� ����.

� ����� ����� ����������� �������� %Name.

%description -n %lname -l ru_RU.CP1251
%Name - ��� ������� �������� ��� �������� ������������� ��� �������
������ ���������. � ������ - ���������� ������� ������ �����������
������, ������� ����������� ������� ������������������, �������
������������� ��� �������������� ��������� ��������. ��� ��� �������
���������� ����� (����������, �������������, ������������, ��������� �
���������) ����� ���� ������� ����� ������� � C, ������������� �
������������ ���.

� ���� ������ ��������� ���������� %Name.
%endif

%package -n %lname-devel
Group: Development/C
Summary: Files required to link software that uses %lname
Summary(uk_UA.CP1251): �����, �������� ��� ��������� �������, �� �������������� %lname
Summary(ru_RU.CP1251): �����, ����������� ��� ���������� ��������, ������� ���������� %lname
Requires: %lname%{!?_enable_shared:-devel-static} = %version-%release

%description -n %lname-devel
%Name is basic framework for creating application specific scripting
languages. It is a library of functions centered around a virtual
machine, which guarantees high performance, ease of use and low
overhead. All its basic building blocks (compiler, interpreter,
decompiler, loader and saver) can be called with a single line of C. No
initialization necessary.

This package contains headers for development whith %Name.

%description -n %lname-devel -l uk_UA.CP1251
%Name - �� ������ �������� ��� ��������� ����������� ��� ������� ���
�������. � ���� - �������� ������� ������� ��������� ������, ���
������� ������ �������������, ������� ������������ �� �������
������� �������. �� ���� ����� �������� ����� (����������, �������������,
������������, ������������ �� �������) ������ ���� �������� �����
������ � C, ������� � ����������� ����.

� ����� ����� ����������� ��������� ��� �������� � %Name.

%description -n %lname-devel -l ru_RU.CP1251
%Name - ��� ������� �������� ��� �������� ������������� ��� �������
������ ���������. � ������ - ���������� ������� ������ �����������
������, ������� ����������� ������� ������������������, �������
������������� ��� �������������� ��������� ��������. ��� ��� �������
���������� ����� (����������, �������������, ������������, ��������� �
���������) ����� ���� ������� ����� ������� � C, ������������� �
������������ ���.

� ���� ������ ��������� ��������� ��� ���������� � %Name.


%if_enabled static
%package -n %lname-devel-static
Group: Development/C
Summary: Static %Name library
Summary(uk_UA.CP1251): �������� �������� %Name
Summary(ru_RU.CP1251): ����������� ���������� %Name
Requires: %lname-devel = %version-%release

%description -n %lname-devel-static
%Name is basic framework for creating application specific scripting
languages. It is a library of functions centered around a virtual
machine, which guarantees high performance, ease of use and low
overhead. All its basic building blocks (compiler, interpreter,
decompiler, loader and saver) can be called with a single line of C. No
initialization necessary.

This package contains static %Name library.

%description -n %lname-devel-static -l uk_UA.CP1251
%Name - �� ������ �������� ��� ��������� ����������� ��� ������� ���
�������. � ���� - �������� ������� ������� ��������� ������, ���
������� ������ �������������, ������� ������������ �� �������
������� �������. �� ���� ����� �������� ����� (����������, �������������,
������������, ������������ �� �������) ������ ���� �������� �����
������ � C, ������� � ����������� ����.

� ����� ����� ����������� �������� �������� %Name.

%description -n %lname-devel-static -l ru_RU.CP1251
%Name - ��� ������� �������� ��� �������� ������������� ��� �������
������ ���������. � ������ - ���������� ������� ������ �����������
������, ������� ����������� ������� ������������������, �������
������������� ��� �������������� ��������� ��������. ��� ��� �������
���������� ����� (����������, �������������, ������������, ��������� �
���������) ����� ���� ������� ����� ������� � C, ������������� �
������������ ���.

� ���� ������ ��������� ����������� ���������� %Name.
%endif

%package doc-txt
Summary: %Name manual in plain text format
Summary(uk_UA.CP1251): ������� ��� %Name � ���������� ������
Summary(ru_RU.CP1251): ����������� ��� %Name � ��������� �������
Group: Development/Documentation
BuildArch: noarch
Provides: %name-doc = %version-%release
Provides: %name-manual = %version-%release
Provides: %name-manual-txt = %version-%release

%description doc-txt
%Name is basic framework for creating application specific scripting
languages. It is a library of functions centered around a virtual
machine, which guarantees high performance, ease of use and low
overhead. But in the meanwhile %Name has acquired a reputation as an
educational tool. Its simplicity makes it perfectly suited to learn
Forth, from which it has been derived.

This package contains %Name manual in plain text format.

%description doc-txt -l uk_UA.CP1251
%Name - �� ������ �������� ��� ��������� ����������� ��� ������� ���
�������. � ���� - �������� ������� ������� ��������� ������, ���
������� ������ �������������, ������� ������������ �� �������
������� �������. �� ���� ����� �������� ����� (����������, �������������,
������������, ������������ �� �������) ������ ���� �������� �����
������ � C, ������� � ����������� ����.

� ����� ����� ����������� ������� ��� %Name � ���������� ������.

%description doc-txt -l ru_RU.CP1251
%Name - ��� ������� �������� ��� �������� ������������� ��� �������
������ ���������. � ������ - ���������� ������� ������ �����������
������, ������� ����������� ������� ������������������, �������
������������� ��� �������������� ��������� ��������. ��� ��� �������
���������� ����� (����������, �������������, ������������, ��������� �
���������) ����� ���� ������� ����� ������� � C, ������������� �
������������ ���.

� ���� ������ ��������� ����������� ��� %Name � ��������� �������.



%prep
%setup -n %name-%version-unix
%patch -p1
install -m 0644 %SOURCE1 sources/Makefile.ALT


%build
%if "%__cc" == "musl-gcc"
%define _optlevel s
%add_optflags -fno-asynchronous-unwind-tables
%endif
%add_optflags %{?_enable_shared:%optflags_shared} -fsigned-char -DUNIX -DDIR4TH='\"%_datadir/%name/\"'
%if "%__cc" == "gcc"
%add_optflags -DUSEGCCGOTO
%endif
%{?_enable_kshared:%global optflags -shared %optflags}
%make_build -C sources -f Makefile.ALT \
	BINARIES=%_bindir LIBRARIES=%_libdir INCLUDES=%_includedir \
	%{?_enable_shared:SHARED=1} %{?_enable_static:STATIC=1} \
	CFLAGS="%optflags" %{?__cc:CC=%__cc} all


%install
install -d -m 0755 %buildroot{%_bindir,%_libdir,%_datadir/%name/lib,%_includedir,%_man1dir,%_docdir/%name-%version/examples}
%make_install -C sources -f Makefile.ALT \
	BINARIES=%buildroot%_bindir LIBRARIES=%buildroot%_libdir INCLUDES=%buildroot%_includedir \
	%{?_enable_shared:SHARED=1} %{?_enable_static:STATIC=1} \
	CFLAGS="%optflags" %{?__cc:CC=%__cc} install
install -p -m 0644 documentation/%name.1 %buildroot%_man1dir/
ln -s %name.1 %buildroot%_man1dir/%{name}x.1
ln -s %name %buildroot%_bindir/%{name}x
install -p -m 0644 sources/%name.h %buildroot%_includedir/
install -p -m 0644 %name/lib/*.4th %buildroot%_datadir/%name/lib/
install -p -m 0644 %name/*.{4th,scr} %buildroot%_docdir/%name-%version/examples/
for d in 4pp{,/lib}; do
	install -d -m 0755 %buildroot%_docdir/%name-%version/examples/$d
	install -p -m 0644 %name/$d/*.4pp %buildroot%_docdir/%name-%version/examples/$d/
done
for d in %name/apps/*; do
	D=$(basename $d)
	install -d -m 0755 %buildroot%_docdir/%name-%version/examples/apps/$D
	install -p -m 0644 $d/* %buildroot%_docdir/%name-%version/examples/apps/$D/
done
for d in bench demo; do
	install -d -m 0755 %buildroot%_docdir/%name-%version/examples/$d
	install -p -m 0644 %name/$d/* %buildroot%_docdir/%name-%version/examples/$d/
done
install -p -m 0644 documentation/euro.txt %buildroot%_docdir/%name-%version/examples/
install -p -m 0644 README %buildroot%_docdir/%name-%version/
install -p -m 0644 {documentation/%{Name},%buildroot%_docdir/%name-%version/}manual.txt

# menu
install -d %buildroot%_desktopdir
iconv -f cp1251 -t utf-8 > %buildroot%_desktopdir/%name.desktop <<__MENU__
[Desktop Entry]
GenericName=%Name
Name=%Name System
Name[uk]=%Name-�������
Name[ru]=%Name-�������
Exec=%name
Icon=shells_section
Type=Application
Terminal=true
Categories=Development;IDE;ConsoleOnly;
__MENU__

%if "%__cc" == "musl-gcc" || "%__cc" == "tcc"
%add_verify_elf_skiplist %_bindir/*
%endif


%files
%doc %dir %_docdir/%name-%version
%doc %_docdir/%name-%version/README
%_bindir/*
%_datadir/%name
%_man1dir/*
%_desktopdir/*


%if_enabled shared
%files -n %lname
%_libdir/*.so.*
%endif


%files -n %lname-devel
%_includedir/*
%{?_enable_shared:%_libdir/*.so}


%if_enabled static
%files -n %lname-devel-static
%_libdir/*.a
%endif


%files examples
%dir %_docdir/%name-%version
%_docdir/%name-%version/examples


%files doc-txt
%dir %_docdir/%name-%version
%_docdir/%name-%version/*.txt


%changelog
* Wed Feb 26 2014 Led <led@altlinux.ru> 3.62.2-alt1
- 3.62.2

* Fri Sep 27 2013 Led <led@altlinux.ru> 3.62.1-alt1
- 3.62.1

* Wed Dec 26 2012 Led <led@altlinux.ru> 3.62.0-alt3
- added build with klcc support
- fixed License
- cleaned up spec
- fixed Makefile.ALT

* Wed Dec 26 2012 Led <led@altlinux.ru> 3.62.0-alt2
- Makefile.ALT: updated lib version

* Mon Dec 24 2012 Led <led@altlinux.ru> 3.62.0-alt1
- 3.62.0

* Tue Oct 23 2012 Led <led@altlinux.ru> 3.61.5-alt1
- 3.61.5
- added Makefile.ALT

* Fri Aug 19 2011 Led <led@massivesolutions.co.uk> 3.61.1-cx1
- 3.61.1

* Wed Feb 09 2011 Led <led@altlinux.ru> 3.61.0-tmc1
- 3.61.0

* Wed Feb 09 2011 Led <led@altlinux.ru> 3.60.1-tmc1
- build with _optlevel s
- 4th's "libs" moved into %%_datadir/%%name/lib
- clean up spec
- fixed License

* Tue Apr 27 2010 Led <led@altlinux.ru> 3.60.1-alt1
- 3.60.1

* Mon Jan 04 2010 Led <led@altlinux.ru> 3.60.0-alt1
- 3.60.0

* Mon Sep 28 2009 Led <led@altlinux.ru> 3.5d3-alt1
- 3.5d3:
  + the library files now support ANS Forth compatible versions of all
    floating point input and output words

* Sat Jun 20 2009 Led <led@altlinux.ru> 3.5d2-alt1
- 3.5d2:
  + added preprocessor to the toolchain
  + added another floating point library called ZEN float

* Mon May 11 2009 Led <led@altlinux.ru> 3.5d-alt1
- 3.5d

* Sat Dec 27 2008 Led <led@altlinux.ru> 3.5c3-alt4
- cleaned up spec

* Fri Aug 08 2008 Led <led@altlinux.ru> 3.5c3-alt3
- fixed %name.desktop

* Wed Jun 18 2008 Led <led@altlinux.ru> 3.5c3-alt2
- added %name-doc-txt subpackage

* Tue Jun 03 2008 Led <led@altlinux.ru> 3.5c3-alt1
- 3.5c3
- build with shared library

* Tue Mar 04 2008 Led <led@altlinux.ru> 3.5c2-alt2
- fixed %name.desktop

* Mon Jan 28 2008 Led <led@altlinux.ru> 3.5c2-alt1
- 3.5c2
- updated %name-3.5c2-alt.patch

* Thu Jan 10 2008 Led <led@altlinux.ru> 3.5c-alt1
- 3.5c
- fixed License
- cleaned up spec
- fixed %%description
- fixed x86_64 build (added %name-3.5c-alt.patch)

* Sat Dec 22 2007 Led <led@altlinux.ru> 3.5b2-alt1
- 3.5b2
- fixed License

* Mon May 21 2007 Led <led@altlinux.ru> 3.5b-alt1
- 3.5b
- cleaned up spec

* Thu Nov 23 2006 Led <led@altlinux.ru> 3.5a2-alt1
- 3.5a2

* Mon Nov 13 2006 Led <led@altlinux.ru> 3.5a-alt1
- 3.5a release

* Mon Oct 16 2006 Led <led@altlinux.ru> 3.5a-alt0.2
- fixed descriptions

* Thu Oct 12 2006 Led <led@altlinux.ru> 3.5a-alt0.1
- fixed %%version
- fixed %%changelog
- made ability compile with tcc

* Sun Sep 24 2006 Led <led@altlinux.ru> 3.5-alt0.1
- 3.5a-pre3
- remade spec
- added docs from 3.3d2

* Sun Sep 24 2006 Led <led@altlinux.ru> 3.3d2-alt4
- fixed spec

* Tue Feb 14 2006 Led <led@altlinux.ru> 3.3d2-alt3
- fixed spec

* Tue Feb 14 2006 Led <led@altlinux.ru> 3.3d2-alt2
- added menu icon
- fixed spec

* Wed Jan 25 2006 Led <led@altlinux.ru> 3.3d2-alt1
- 3.3d2
- added uk and ru menu, description and Summary
- moved examples to separate package
- added headers
- moved %lname.a and headers to separate package

* Sun Jan 22 2006 Led <led@altlinux.ru> 3.3d-alt1
- Initial build
