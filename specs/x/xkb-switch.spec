Summary:        Change keyboard layout from console
Name:           xkb-switch
Version:        1.4.0
Release:        alt1.git.d7c1856a
URL:            https://github.com/ierton/xkb-switch
Packager: 	Valentin Rosavitskiy <valintinr@altlinux.org>
License:	GPL v2+
Group:		Graphical desktop/Other

Source:		%name-%version.tar
BuildPreReq:	cmake rpm-macros-cmake gcc-c++ libX11-devel libxkbfile-devel


%description
xkb-switch is a C++ program that allows to query and change the XKB
layout state. Originally ruby-based code written by J.Broomley.

%prep
%setup -q

%build
#quick fix for libdir
sed -i 's/LIBRARY DESTINATION lib OPTIONAL/LIBRARY DESTINATION %_lib OPTIONAL/' CMakeLists.txt

cmake . -DCMAKE_INSTALL_PREFIX:PATH=%_usr -DINSTALL_LIBDIR=:PATH=%_libdir .


%install
%makeinstall_std PREFIX=/usr

%files
%_bindir/%name
%_libdir/libxkbswitch.so

%changelog
* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 1.4.0-alt1.git.d7c1856a
- New version

* Mon Aug 31 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 1.3.1-alt1.git532d92321
- New version

* Thu Oct 30 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0-alt1.git97bf2c86f
- Initial build for ALT

