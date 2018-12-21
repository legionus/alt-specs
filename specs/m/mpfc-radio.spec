%define bname mpfc
%define Name MPFC
Name: %bname-radio
Version: 0.1
Release: alt2.1
Summary: Radio input plugin for %Name
License: %gpl2plus
Group: Sound
URL: http://%bname.sourceforge.net
Source: %name-%version.tar
Patch: %name-0.1-alt.patch
Patch1: %name-0.1-alt-v4l.patch

BuildRequires: libmpfc-devel libv4l-devel
BuildRequires: rpm-build-licenses

%description
Radio input plugin for %Name.


%prep
%setup
%patch -p1
%patch1 -p2


%build
%autoreconf
%configure --enable-shared --disable-static --with-pic
%make_build


%install
%make_install DESTDIR=%buildroot install


%files
%doc AUTHORS
%_libdir/%bname/input/*.so


%changelog
* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.1
- Fixed build

* Thu Oct 16 2008 Led <led@altlinux.ru> 0.1-alt2
- remove alien README

* Thu Oct 16 2008 Led <led@altlinux.ru> 0.1-alt1
- initial revision
