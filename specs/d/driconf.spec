%define name driconf
%define version 0.9.1
%define release alt2

%setup_python_module %name

Summary: DRI Configuration GUI
Summary(ru_RU.KOI8-R): ����������� ������� ��� ��������� DRI
Name: %name
Version: %version
Release: alt2.qa1
Source0: %name-%version.tar.gz
Source1: %name-0.9.0-ru.po
Patch0:  driconf-0.9.1-fix_i_j.patch
License: GPL
Group: System/Configuration/Hardware
Url: http://dri.freedesktop.org/wiki/DriConf
Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): python-dev
BuildRequires: python-module-pygtk

%description
DRI configuration GUI

This is the first graphical configuration tool for DRI. In order to 
use it you need a recent development verion of DRI.

%description -l ru_RU.KOI8-R
����������� ������� ��� ��������� DRI

������ ������� ����� ��������� ����������� 3D ��������� ���
DRI-���������� ����������� ����, �������� ��� ��������� ����������� ��������
��� ������� ���������� � �����������. �.�. ��� ��������� ��� ���������
����������� �� �������������, ��� ����� ����� ��������� ������ DRI, ��� ����,
����� �������� ������������ ������������������ � �������� ������ �� ����
������������ DRI-������������ ��������.

%prep
%setup -q
install -m644 %SOURCE1 ru.po
sed -i 's|\/usr\/local|\%_prefix|' setup.cfg driconf
%patch -p2

%build
make mo
CFLAGS="%optflags" %__python setup.py build

%install
%__python setup.py install --root %buildroot --record=INSTALLED_FILES

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=driconf
Comment=DRI Configuration GUI
Icon=%name
Exec=%name
Terminal=true
Categories=Settings;HardwareSettings;X-ALTLinux-VideoSettings;
EOF


%files -f INSTALLED_FILES
%doc CHANGELOG README COPYING TODO
%_desktopdir/%name.desktop
%dir %_libexecdir/%name
#_libdir/%name/*.pyo

%changelog
* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt2.qa1
- NMU: applied repocop patch

* Fri Jun 08 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.1-alt2
- Fix program start (Closes: #31685).

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.1-alt1.qa3.1
- Rebuild with Python-2.7

* Fri Apr 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.9.1-alt1.qa3
- NMU: converted menu to desktop file

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.1.1
- Rebuilt with python 2.6

* Sat Sep 19 2009 Ilya Mashkin <oddity@altlinux.ru> 0.9.1-alt1.1
- remove deprecated Requires

* Sat May 02 2009 Ilya Mashkin <oddity@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.9.0-alt2.1
- Rebuilt with python-2.5.

* Sun Jan 07 2007 L.A. Kostis <lakostis@altlinux.ru> 0.9.0-alt2
- make it truly noarch.

* Sat Apr 01 2006 LAKostis <lakostis at altlinux dot ru> 0.9.0-alt1.1
- rebuild according policy.
- add missing dir.

* Sun Jan 29 2006 LAKostis <lakostis at altlinux dot ru> 0.9.0-alt1
- 0.9.0.
- update translation.

* Sat Aug 13 2005 LAKostis <lakostis at altlinux dot ru> 0.2.7-alt1
- 0.2.7.
- translation merged to upstream.

* Thu Aug 11 2005 LAKostis <lakostis at altlinux dot ru> 0.2.6-alt1.1
- update translation.

* Mon Aug 08 2005 LAKostis <lakostis at altlinux dot ru> 0.2.6-alt1
- 0.2.6.

* Sat Apr 02 2005 LAKostis <lakostis at altlinux dot ru> 0.2.5-alt1
- new upstream.
- update URL.
- cleanup buildreq/requires.
- add russian translation.

* Sat Jan 08 2005 LAKostis <lakostis at altlinux dot ru> 0.2.2-alt1
- initial build for Sisyphus.
