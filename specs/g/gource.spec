Name: gource
Version: 0.49
Release: alt1

Summary: OpenGL-based 3D visualisation tool for source control repositories
License: %gpl3only
Group: Development/Tools
Url: http://gource.io/

# git clone git://github.com/acaudwell/Gource.git
# git clone git://github.com/acaudwell/Core.git
Source0: %name-main-%version.tar
Source1: %name-core-%version.tar
Patch0: %name-0.43-alt-build.patch

Requires: fonts-ttf-freefont

BuildPreReq: rpm-build-licenses
BuildPreReq: libSDL2-devel >= 1.2
BuildPreReq: libSDL2_image-devel >= 1.2
BuildPreReq: libpcre-devel
BuildPreReq: libfreetype-devel
BuildPreReq: libglew-devel
BuildPreReq: libglm-devel >= 0.9.3
BuildPreReq: boost-filesystem-devel >= 1.46
BuildPreReq: tinyxml-devel
BuildPreReq: gcc-c++
# zlib-devel be req by libfreetype
BuildPreReq: zlib-devel

BuildRequires: libpng-devel

%define _unpackaged_files_terminate_build 1

%description
OpenGL-based 3D visualisation tool for source control repositories. The
repository is displayed as a tree where the root of the repository is
the centre, directories are branches and files are leaves. Contributors
to the source code appear and disappear as they contribute to specific
files and directories.

%prep
%setup
tar xf %_sourcedir/%name-core-%version.tar -C src/
%patch0 -p0

%build
%autoreconf
%configure --with-tinyxml --with-x
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_datadir/%name/
%_man1dir/*

%changelog
* Wed Jun 27 2018 Mikhail Efremov <sem@altlinux.org> 0.49-alt1
- Updated to 0.49.

* Thu May 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.48-alt1.1
- NMU: rebuilt with boost-1.67.0

* Fri Mar 23 2018 Mikhail Efremov <sem@altlinux.org> 0.48-alt1
- Updated to 0.48.

* Thu Sep 28 2017 Mikhail Efremov <sem@altlinux.org> 0.47-alt1
- Updated to 0.47.

* Tue Sep 05 2017 Mikhail Efremov <sem@altlinux.org> 0.46-alt1
- Fix typo in man page.
- Drop obsoleted patch.
- Updated to 0.46.

* Mon Aug 28 2017 Mikhail Efremov <sem@altlinux.org> 0.44-alt3
- Rebuilt with libboost_*.so.1.65.0.

* Mon Jul 31 2017 Mikhail Efremov <sem@altlinux.org> 0.44-alt2
- Rebuilt with libboost_*.so.1.63.0.

* Thu Aug 04 2016 Mikhail Efremov <sem@altlinux.org> 0.44-alt1
- Patch from upstream: Fix crash.
- Own %%_datadir/%%name/.
- Updated to 0.44.

* Fri Feb 05 2016 Mikhail Efremov <sem@altlinux.org> 0.43-alt1
- Updated alt-build.patch.
- Updated Url.
- Updated to 0.43.

* Sat Jan 03 2015 Ivan A. Melnikov <iv@altlinux.org> 0.38-alt1.2
- rebuild with boost 1.57.0
- fix build with recent gcc

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.38-alt1.1.qa1
- NMU: rebuilt with libboost_*.so.1.53.0.

* Fri Nov 30 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.38-alt1.1
- Rebuilt with Boost 1.52.0

* Fri Sep 21 2012 Ivan Ovcherenko <asdus@altlinux.org> 0.38-alt1
- Initial build for ALT Linux Sisyphus, v0.38-46243b0+d42063b
