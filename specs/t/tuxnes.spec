Name: tuxnes
Version: 0.75
Release: alt5.2

Packager: Ilya Mashkin <oddity at altlinux dot ru>

Summary: Emulator for Nintendo (Dendy)
Summary(ru_RU.KOI8-R): �������� ������� ������� Nintendo (�����)
License: GPL
URL: http://tuxnes.sourceforge.net
Group: Emulators


Source0: tuxnes-0.75.tar.gz
Patch0: tuxnes-0.75-gcc34.patch
Patch1: tuxnes-0.75-include.patch
Patch2: tuxnes-0.75-fix-open-param.patch
Patch3: tuxnes-0.75-xshm.patch
Patch4: tuxnes-0.75-exec-stack.patch

# Automatically added by buildreq on Wed Feb 02 2005
BuildRequires: gcc gcc-c++ zlib-devel libSDL-devel libnetpbm-devel libXext-devel libXpm-devel

ExclusiveArch: %ix86

%description
Emulator for the 8-bit Nintendo Entertainment System (a.k.a. Dendy)

%description -l ru_RU.KOI8-R
�������� 8-������ ������� ������� Nintendo (��� �� ��������� ��� �����)


%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
#patch4 -p1

#set_gcc_version 4.3
#export CC=gcc-4.3 CXX=g++-4.3
%set_automake_version 1.9
%set_autoconf_version 2.5



%build

%configure --with-x
%make_build

%install

%make_install
install -D -pm 755 tuxnes %buildroot%_bindir/%name
install -D -pm 755 romfixer %buildroot%_bindir/romfixer
%__mkdir_p %buildroot%_docdir/%name-%version


%files
%doc COPYING AUTHORS BUGS NEWS README ChangeLog THANKS
%_bindir/*


%changelog
* Fri Apr 12 2013 Andrey Cherepanov <cas@altlinux.org> 0.75-alt5.2
- Fix build with new xorg

* Thu Aug 18 2011 Ilya Mashkin <oddity@altlinux.ru> 0.75-alt5.1
- update requires

* Tue Aug 17 2010 Ilya Mashkin <oddity@altlinux.ru> 0.75-alt5
- fix build

* Fri Dec 11 2008 Ilya Mashkin <oddity@altlinux.ru> 0.75-alt4
- fix build
- update requires

* Wed Feb 02 2005 Ilya Mashkin <oddity at altlinux dot ru> 0.75-alt3
- correct deps, add URL
- fix build for gcc3.4 (+patch0)

* Tue Sep 11 2003 Ilya Mashkin <oddity@altlinux.ru> 0.75-alt2
- Code & spec cleanup

* Tue Aug 12 2003 Ilya Mashkin <oddity@altlinux.ru> 0.75-alt1
- Update version

* Mon Aug 11 2003 Ilya Mashkin <oddity@altlinux.ru> 0.74-alt2
- Spec cleanup

* Mon Aug 11 2003 Ilya Mashkin <oddity@altlinux.ru> 0.74-alt1
- Initial build

