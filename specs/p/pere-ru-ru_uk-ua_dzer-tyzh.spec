# ########################################################
# non latin symbols shouldn't be in first 256 byte block #
# ########################################################

%define dict_iln        ru-ru
%define dict_oln        uk-ua
%define dict_thm        dzer-tyzh

%define dict_name       %{dict_iln}_%{dict_oln}_%dict_thm

%define name_iln_en	Russian
%define name_oln_en	Ukrainian
%define name_thm_en	Social and political

%define name_iln_uk	��������
%define name_oln_uk	���������
%define name_thm_uk	���������-���������

%define name_iln_ru	��������
%define name_oln_ru	����������
%define name_thm_ru	���������-������������

%define name_nam_en	Pere
%define name_nam_uk	����
%define name_nam_ru	����

Name: pere-%dict_name
Version: 0.2.0
Release: alt3

Summary: %name_nam_en: %name_thm_en dictionary from %name_iln_en to %name_oln_en
Summary(uk_UA.CP1251): %name_nam_uk: %name_thm_uk ������� � %name_iln_uk �� %name_oln_uk
Summary(ru_RU.CP1251): %name_nam_ru: %name_thm_ru ������� � %name_iln_ru �� %name_oln_ru
License: GPL
Group: Text tools
Url: http://pere.org.ua/
BuildArch: noarch
Source: http://pere.org.ua/dwn/src/dmp/pere-dicsrc_%{dict_name}_%version.tar.bz2

BuildRequires: perl-Lingua-Pere >= 0.2.0 perl(Pod/Text.pm)
Requires: perl-Lingua-Pere >= 0.2.0 perl(Pod/Text.pm)

%description
%name_thm_en translation dictionary from %name_iln_en to %name_oln_en for %name_nam_en translator.

%description -l uk_UA.CP1251
%name_thm_uk ������� ��������� � %name_iln_uk �� %name_oln_uk ��� ������������ %name_nam_uk.

%description -l ru_RU.CP1251
%name_thm_ru ������� ��������� � %name_iln_ru �� %name_oln_ru ��� ����������� %name_nam_ru.

%prep
%setup -q -n pere-dicsrc_%dict_name

%build
export LANG=en_US.UTF-8
pere-src2dic -pfx=./ -csv=%dict_name.src -ovr -mem=100
pere-dic2dmp -pfx=./ -csv=%dict_name.dmp -ovr -mem=100

%install
install -p -m644 -D %dict_name.dmp %buildroot%_datadir/dict/pere/%dict_name/%dict_name.dmp

%post
pere-dmp2dic -pfx=%_datadir/dict/pere/%dict_name -csv=%_datadir/dict/pere/%dict_name/%dict_name.dmp -ovr -mem=100
pere-confupd -rut=%_datadir/dict/pere/ -cfg=/etc/pere-trans.config

%preun
rm -drf %_datadir/dict/pere/%dict_name

%postun
pere-confupd -rut=%_datadir/dict/pere/ -cfg=/etc/pere-trans.config

%files
%doc Changes README
%_datadir/dict/pere/%dict_name

%changelog
* Tue Sep 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt3
- NMU: fixed build

* Tue Nov 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2
- NMU: added missing Pod dependencies

* Mon Jul 24 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.2.0-alt1
- Rebuld with new Lingua-Pere

* Tue Jun 27 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.2.0-alt0
- Update fo Sisyphus

* Sat Jun  3 2006 Valentyn Solomko <val@pere.org.ua>
- rebuilt after some corrections

* Sat May 20 2006 Valentyn Solomko <val@pere.org.ua> 0.2.0
- First build
