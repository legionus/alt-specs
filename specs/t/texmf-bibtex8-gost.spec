%define truename gost

Name: texmf-bibtex8-%truename
Version: 0.20050820
Release: alt3

Summary: GOST cyrillic bibtex styles and extended cyrillic support for BibTeX8
Summary(ru_RU.CP1251): ������������� BibTeX ����� ����
License: GPL
Group: Publishing
Url: http://tug.ctan.org/tex-archive/biblio/bibtex/contrib/gost/
Packager: Igor Vlasenko <viy@altlinux.ru>

Obsoletes: tetex-bibtex8-gost <= 0.00000001

Source: ftp://tug.ctan.org/pub/tex-archive/biblio/bibtex/contrib/gost/gost.zip
BuildArch: noarch

# Automatically added by buildreq on Sat Dec 31 2005
BuildRequires: /usr/bin/latex unzip

BuildRequires(pre): rpm-build-tex

#TODO: bibtex8 does not support kpathsea

%description
USSR GOST 7.1-84 and Russian GOST 7.80-00 cyrillic BibTeX styles 
with russian, ukrainian and (partially) belarussian languages support.
ruscii, cp1251 and koi8-u code pages for BibTeX8 --- 
an 8-bit Implementation of BibTeX 0.99 with multilanguage support.

%description -l ru_RU.CP1251
����� BiBTeX ��� ���������� ������������ 
�� ����������, �������, ����������, ����������� ������ 
�������� ���� ���� 7.1-84 � ���� ������ 7.80-00
� ����� ����������� ��������� ��������� ��� BibTeX8.
�������� ruscii, cp1251 and koi8-u code pages.

��� ���������� ���������� ������������� ������������ BiBTeX8.

%prep
%setup -q -n %truename

%build
latex %truename.ins

%install
install -d %buildroot/usr/share/texmf/bibtex/csf
install -m644 *.csf %buildroot/usr/share/texmf/bibtex/csf/
#bibtex8 does not support kpathsea :( note: might not be true for texlive: check...
#install -d %buildroot/usr/share/texmf/bibtex/bst/%truename
#install -m644 *.bst %buildroot/usr/share/texmf/bibtex/bst/%truename/
install -d %buildroot/usr/share/texmf/bibtex/bst/
install -m644 *.bst %buildroot/usr/share/texmf/bibtex/bst/

%files
%doc README gost780.pdf gost71.pdf
/usr/share/texmf/bibtex/csf/*.csf
#/usr/share/texmf/bibtex/bst/%truename/*.bst
/usr/share/texmf/bibtex/bst/*.bst

%changelog
* Tue Mar 06 2018 Igor Vlasenko <viy@altlinux.ru> 0.20050820-alt3
- build with rpm-build-tex

* Fri Nov 13 2009 Igor Vlasenko <viy@altlinux.ru> 0.20050820-alt2
- fixed buildreqs

* Thu Nov 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.20050820-alt1
- renamed to texmf-bibtex8-gost

* Sat Dec 31 2005 Igor Vlasenko <viy@altlinux.ru> 0-alt1.20050820
- initial build
