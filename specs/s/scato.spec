Name: scato
Version: 0.3.7
Release: alt1
Group: Education
Summary: Scalable Tortoise is a programming language to drive the tortoise, that can draw lines with different width and colors
Summary(ru_RU.KOI8-R): ���� ��� �������� ��������, ����������� ���������������� �������� ������������ ���������
License: BSD
Url: http://code.google.com/p/scato
Source: %name-%version.tar.gz
# rm -rf doc; wget -P doc -E -H -k -K -p http://code.google.com/p/scato/wiki/{language_manual_ru,menu_overview_ru,language_manual_ru,history_ru,overview_ru,implementation_ru,features_and_changes_ru,features_and_changes,examples,menu_overview,BNF_ru,BNF}
Source1: doc.tar
BuildArch: noarch
%setup_python_module %name
Requires: %packagename = %version

# Automatically added by buildreq on Thu Jul 08 2010
BuildRequires: python-devel

%description
Scato (Scalable Tortoise) is a programming language to drive the
tortoise, that can draw lines with different width and colors. Scato is
designed to plot iterated function system (IFS), L-systems, Penrose
tile, and similar kinds of fractal objects. It's arm to make easy to
scale and rotate parts of plots, produce loops and recursions, and
create pretty self-similar colored curves.

Moreover, Scato is environment. You can execute your programs, debug
them, view results and export pictures in PostScript format. Also Scato
equipped with helpful build-in examples and demos.

%description -l ru_RU.KOI8-R
Scato -- �������� ��������� ���� (���� ��� �������� ��������,
����������� ���������������� �������� ������������ ���������). ����
��������� ������������������ �������� �������� �������������
����������������: ���������, �����, ������������, ���������. ����
�������������� ����� �������, �����, � ����� �������, ���� �����������
�������, � � ������ �������, ����������� ������� � �������� Pascal
(Pascal ������������ � ���). ������������� ����� �� ������ �������������
��������� ������ ���������, �� � ��������� ��������� ��������� ��������,
������������� ������� �������� ���������� � ��������� ���������. Scato
����������� � �ޣ��� ��������� �������������� � ��� ��� ����������� ��
���������� �������������� ������������.

%package -n %packagename
License: BSD
Group: Development/Python
Summary: Supplemental module for %name

%description -n %packagename
Supplemental module for %name, %summary

%prep
%setup
tar xvf %SOURCE1

%build
%python_build

%install
%python_install

# TODO documentation
%files
%doc README doc/*
%_bindir/*

%files -n %packagename
%python_sitelibdir/*

%changelog
* Sun Dec 23 2012 Fr. Br. George <george@altlinux.ru> 0.3.7-alt1
- Autobuild version bump to 0.3.7

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.6-alt1.1
- Rebuild with Python-2.7

* Fri Jan 21 2011 Fr. Br. George <george@altlinux.ru> 0.3.6-alt1
- Version up

* Fri Nov 05 2010 Fr. Br. George <george@altlinux.ru> 0.3.5-alt2
- Documentation update

* Tue Jul 27 2010 Fr. Br. George <george@altlinux.ru> 0.3.5-alt1
- Version up

* Thu Jul 08 2010 Fr. Br. George <george@altlinux.ru> 0.3.0-alt1
- Initial build for ALT

