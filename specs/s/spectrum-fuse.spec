%define oname fuse
Name: spectrum-fuse
Version: 1.5.7
Release: alt1

Summary: The Free Unix Spectrum Emulator

License: GPLv2
Group: Emulators
Url: http://fuse-emulator.sourceforge.net/

Packager: ZX Spectrum Development Team <spectrum@packages.altlinux.org>

Source: %name-%version.tar
Source3: README.z88sdk

Provides: fuse-emulator = %version

# Automatically added by buildreq on Sun Jul 29 2007
BuildRequires: flex gcc-c++ glibc-devel libgcrypt-devel libjsw-devel libspectrum-devel libxml2-devel xorg-cf-files

# Optional:
# libgcrypt: the ability to digitally sign RZX files (note that Fuse requires version 1.1.42 or later).
# libpng: the ability to save screenshots.
# libxml2: the ability to load and save Fuse's current configuration.
# libjsw: allow joystick input to be used (not required for joystick emulation).
# zlib: support for compressed RZX files.
# libbzip2: support for certain compressed files.
# libaudiofile: support for loading from .wav files.

BuildRequires: libspectrum-devel >= 1.4.1 libpng-devel libalsa-devel libgtk+3-devel

%description
Fuse is a Sinclair ZX Spectrum emulator. It supports several models
(including the 128), with quite faithful emulation of the display
and sound.

%prep
%setup -q -n %name-%version
sed -e "s/=fuse/=spectrum-fuse/" -e "s/=Fuse/=Spectrum Fuse/" -e "/Version/a Encoding=UTF-8" -i data/fuse.desktop.in
find -name "Makefile.am" -exec sed -e "s/fuse_/spectrum_fuse_/" -e "s/= fuse/= spectrum-fuse/" -i {} \;
sed -e "s/\[fuse]/[spectrum-fuse]/g" -i configure.ac
sed -e "s/\(^\|\" \|B \"\?\|IR \|TH \)fuse/\1spectrum\\\\-fuse/" -i man/fuse.1

%build
%autoreconf
%configure --disable-ui-joystick --enable-joystick --with-gtk --enable-desktop-integration
%make_build

%install
export DESTDIR=%buildroot
%makeinstall
install -D -m 0644 %buildroot/%buildroot/%_man1dir/fuse.1 %buildroot/%_man1dir/spectrum-fuse.1
rm %buildroot/%buildroot/%_man1dir/fuse.1
mv %buildroot/%_desktopdir/%oname.desktop  %buildroot%_desktopdir/%name.desktop
mv %buildroot/usr/share/mime/packages/fuse.xml %buildroot/usr/share/mime/packages/spectrum-fuse.xml
find %buildroot%buildroot -type f | while read f; do nf=$(sed "s|%buildroot||" <<< "$f"); echo "== $nf"; install -D -m 644 "$f" "$nf"; rm -f "$f"; done
find %buildroot -name 'fuse.png' -type f | while read f; do nf=$(sed "s|fuse.png|spectrum-fuse.png|" <<< "$f"); echo "== $nf"; install -D -m 644 "$f" "$nf"; rm -f "$f"; done

install -pm0644 %{SOURCE3} .

%files
%doc README.z88sdk
%doc README AUTHORS COPYING ChangeLog THANKS
%_bindir/%name
%_man1dir/*
%_desktopdir/*
%_datadir/%name
%_datadir/mime/*
%_iconsdir/hicolor/*/apps/spectrum-fuse.png
%_iconsdir/hicolor/*/mimetypes/application-x-spectrum.png

%changelog
* Wed Dec 12 2018 Pavel Skrylev <majioa@altlinux.org> 1.5.7-alt1
- Removed sources from gear.
- Cleaned up the spec.
- Bump to 1.5.7.

* Wed Sep 11 2013 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt2
- update buildreqs

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- new version 1.1.1 (with rpmrb script)

* Sat Dec 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0.1a-alt1
- new version
- added fuse-emulator-zlib.patch and README.z88sdk from Fedora

* Wed Oct 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0.1-alt1.qa2
- Rebuilt with libpng15

* Wed Dec 02 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.8.0.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for spectrum-fuse
  * postclean-05-filetriggers for spec file

* Sun Jul 29 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.0.1-alt1
- add patches from PLD, add icon from Fedora
- add desktop file, rename binary to spectrum-fuse

* Sun May 27 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.0.1-alt0.1
- new version 0.8.0.1 (with rpmrb script)

* Mon Jun 05 2006 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt2
- fixes for GCC4
- cleanup: fix URL, Source, remove COPYING

* Fri Feb 11 2005 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1.1
- add buildreq for libspectrum

* Sun Feb 06 2005 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- NMU: new version
- rename to spectrum-fuse (was conflicts with fuse as userspace fs)
- add menu file
- update buildreq

* Tue Sep 30 2003 Alexey Tourbin <at@altlinux.ru> 0.6.1-alt1
- initial revision
