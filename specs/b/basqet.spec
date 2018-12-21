Name:		basqet
Version:	0.2.0
Release:	alt2
Summary:	Basqet - Notes and Data in Baskets
License:	GPL
Group:		Office
URL:		http://code.google.com/p/basqet/
Packager: 	Andrey Cherepanov <cas@altlinux.org>

Source:		%{name}_%version-src.tgz

BuildRequires:	gcc-c++, qt4-devel

%description
The idea is to use baskets to put, not eggs, but notes and ideas (text,
pictures, HTML-links etc), as well as tagged data in list-form with
filters etc. It shall be possible to use arrows to connect notes,
and possibly to add symbols like boxes, squares, UML etc.

Notes and data is labeled the same way as labels work here at
Google-Code, and some labels might imply a little symbol/icon
on the item or a change in font, text-, or background color.

%prep
%setup -q

%build
qmake-qt4 PREFIX=/usr
%make

%install
%make INSTALL_ROOT=%buildroot install

%files
%doc gpl-3.0.txt
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Mon May 20 2013 Andrey Cherepanov <cas@altlinux.org> 0.2.0-alt2
- Remove phonon-backend-xine requirement

* Wed Apr 17 2013 Andrey Cherepanov <cas@altlinux.org> 0.2.0-alt1
- New version 0.2.0

* Fri Feb 04 2011 Andrey Cherepanov <cas@altlinux.org> 0.1.4-alt1
- Initial build in Sisyphus

* Thu Nov 10 2009 - TI_Eugene <ti.eugene@gmail.com>
- Initial build for OBS
