Name: dbview
Version: 1.0.4
Release: alt2%ubt

License: GPL
Url: ftp://metalab.unc.edu/pub/Linux/apps/database/proprietary/
Summary: Dbview - view dBase files
Summary(ru_RU.CP1251): Dbview - ��������� ��� ��������� dBase ������
Group: Databases
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: %name-%version.tar.gz
Patch0: %name-makefile.patch.gz
Patch1: %name-fixes.patch.gz

BuildRequires(pre): rpm-build-ubt

%description
Dbview is a little tool that will display dBase III and IV files.
You can also use it to convert your old .dbf files for further use with Unix.

%description -l ru_RU.CP1251
Dbview ��� ��������� �������, ������� ���������� ���������� dBase ������ ������ III � IV.
�����, �� ������ ������������ � ��� �������������� ����� ������ .dbf ������ � �����
����������� ������������� �� Unix-��������.

%prep
%setup
#patch0
#patch1

%build
%make_build

%install
mkdir -p $RPM_BUILD_ROOT{%_bindir,%_man1dir}

install -m 755 %name $RPM_BUILD_ROOT%_bindir
install -m 644 %name.1 $RPM_BUILD_ROOT%_man1dir

%files
%doc README dBASE
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Wed Jun 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.4-alt2%ubt
- Updated spec to include man files with any compression

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.4-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Sep 26 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0.4-alt1
- 1.0.4 (Closes: #16975)

* Fri Oct 11 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.0.3-alt2
- rebuilded with gcc-3.2
- removed Summary & description in KOI8-R encoding

* Mon Feb 18 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.0.3-alt1
- first build for Sisyphus
- dbview-fixes.patch taken from PDL Linux Distribution
