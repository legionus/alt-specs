Name: btfs
Version: 2.18
Release: alt1

Summary: A bittorrent filesystem based on FUSE

License: GPL
Group: Communications
Url: https://github.com/johang/btfs

# Source-url: https://github.com/johang/btfs/archive/v%version.tar.gz
Source: %name-%version.tar

# manually removed: python-module-google python3-dev python3-module-yieldfrom python3-module-zope ruby ruby-stdlibs
# Automatically added by buildreq on Thu Jun 23 2016
# optimized out: boost-asio-devel boost-devel boost-devel-headers libssl-devel libstdc++-devel libtorrent-rasterbar8 perl pkg-config python-base python-modules python3 python3-base
BuildRequires: gcc-c++ libcurl-devel libfuse-devel libtorrent-rasterbar-devel

%description
With BTFS, you can mount any .torrent file or magnet link and then use it
as any read-only directory in your file tree.
The contents of the files will be downloaded on-demand as they
are read by applications.
Tools like ls, cat and cp works as expected.
Applications like vlc and mplayer can also work without changes.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_bindir/btplay
%_bindir/btfsstat
%_man1dir/*

%changelog
* Sat Jun 30 2018 Vitaly Lipatov <lav@altlinux.ru> 2.18-alt1
- new version 2.18 (with rpmrb script)

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.13-alt3.1
- NMU: rebuilt with boost-1.67.0

* Wed Apr 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.13-alt3
- (NMU) Rebuilt with new libtorrent-rasterbar.

* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.13-alt2
- Rebuild with new libtorrent-rasterbar.

* Wed Mar 15 2017 Vitaly Lipatov <lav@altlinux.ru> 2.13-alt1
- new version 2.13 (with rpmrb script)

* Fri Jul 29 2016 Vitaly Lipatov <lav@altlinux.ru> 2.10-alt1
- new version 2.10 (with rpmrb script)

* Thu Jun 23 2016 Vitaly Lipatov <lav@altlinux.ru> 2.9-alt1
- initial build for ALT Linux Sisyphus
