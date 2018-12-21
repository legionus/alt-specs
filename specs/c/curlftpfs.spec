Name: curlftpfs
Version: 0.9.2
Release: alt3

Summary: FTP filesystem, based on Curl and FUSE
License: GPL
Group: System/Kernel and hardware
Url: http://curlftpfs.sourceforge.net

BuildRequires: glib2-devel libcurl-devel libfuse-devel

Source: %name-%version-%release.tar

%description
CurlFtpFS is a filesystem for accessing FTP hosts based on FUSE and
libcurl. CurlFtpFS differentiates itself from other FTP filesystems
because it features:
- SSLv3 and TLSv1 support
- connecting through tunneling HTTP proxies
- automatically reconnection if the server times out
- transform absolute symlinks to point back into the ftp file system

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall
mkdir %buildroot/sbin
ln -s /usr/bin/curlftpfs  %buildroot/sbin/mount.curlftpfs

%files
/sbin/mount.curlftpfs
%_bindir/curlftpfs
%_man1dir/curlftpfs.1.*

%changelog
* Mon Nov 19 2018 Pavel Skrylev <majioa@altlinux.org> 0.9.2-alt3
- Added symlink from sbin to usr/bin to allow mounting from fstab.

* Fri Nov 09 2012 Pavel Shilovsky <piastry@altlinux.org> 0.9.2-alt2
- Fix missed 0.9.2 sources

* Wed Aug 25 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.2-alt1
- 0.9.2 released

* Tue Dec 25 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.1-alt2
- fixed build with autofoo >= 2.60

* Sun Jul 15 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.1-alt1
- Initial build.
