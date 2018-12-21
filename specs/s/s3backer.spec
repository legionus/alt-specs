Name: s3backer
Version: 1.5.0
Release: alt1

Summary: FUSE-based single file backing store via Amazon S3
License: GPL
Group: System/Kernel and hardware
Url: https://github.com/archiecobbs/s3backer

Requires: fuse

Source: %name-%version-%release.tar
BuildRequires: libcurl-devel libexpat-devel libfuse-devel libssl-devel zlib-devel

%description
s3backer is a filesystem that contains a single file backed by the Amazon S3.
As a filesystem, it is very simple: it provides a single normal file having
a fixed size.  Underneath, the file is divided up into blocks, and the content
of each block is stored in a unique Amazon S3 object.  In other words, what
s3backer provides is really more like an S3-backed virtual hard disk device,
rather than a filesystem.

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc COPYING README*
%_bindir/s3backer
%_man1dir/s3backer.1*

%changelog
* Thu Oct 11 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.0-alt1
- 1.5.0 released

* Tue May 22 2012 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt7
- fix build

* Mon Mar 21 2011 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt6
- fix build

* Thu Feb 03 2011 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt5
- fix requires to fuse

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt4
- auto rebuild

* Sun Oct 10 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt3
- rebuild with new openssl

* Fri Feb 12 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt2
- fix buildrequires

* Fri Feb 12 2010 Denis Smirnov <mithraen@altlinux.ru> 1.3.1-alt1
- first build for Sisyphus
