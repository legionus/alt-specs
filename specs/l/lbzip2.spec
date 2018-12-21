Name: lbzip2
Version: 2.5
Release: alt1

Summary: Parallel bzip2/bunzip2 filter
License: GPLv3+
Group: Archiving/Compression

Url: http://lacos.hu/
Source: %name-%version.tar.gz
Patch: lbzip2-2.1-alt-no-internal-stdio.h.patch

%description
Lbzip2 is a Pthreads-based parallel bzip2/bunzip2 filter, passable to GNU tar
with the --use-compress-program option.

It isn't restricted to regular files on input, nor output. Successful splitting
for decompression isn't guaranteed, just very likely (failure is detected).
Splitting in both modes and compression itself occur with an approximate 900k
block size.

%prep
%setup
%patch -p2

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_man1dir/*

%changelog
* Tue Apr 15 2014 Fr. Br. George <george@altlinux.ru> 2.5-alt1
- Autobuild version bump to 2.5

* Thu Dec 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.1
- Fixed build

* Sun Nov 27 2011 Victor Forsiuk <force@altlinux.org> 2.1-alt1
- 2.1

* Fri May 21 2010 Victor Forsiuk <force@altlinux.org> 0.23-alt1
- 0.23

* Mon Dec 14 2009 Victor Forsyuk <force@altlinux.org> 0.19-alt1
- 0.19

* Mon Oct 26 2009 Victor Forsyuk <force@altlinux.org> 0.16-alt1
- Initial build.
