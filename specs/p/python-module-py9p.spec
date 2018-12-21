%define modname py9p

Name: python-module-%modname
Version: 1.0.9
Release: alt1

Summary: Pure Python implementation of 9P protocol (Plan9)
License: MIT
Group: Development/Python
URL: https://github.com/svinota/py9p
BuildArch: noarch

Source: py9p-%version.tar

BuildRequires(pre): rpm-build-python
BuildRequires: python-module-setuptools
BuildRequires: python-devel

BuildPreReq: python3-module-setuptools
BuildPreReq: python3-devel


%description
Protocol 9P is developed for Plan9 operating system from Bell Labs.
It is used for remote file access, and since files are key objects
in Plan9, 9P can be used also for composite file access, RPC etc.

This library provides low-level 9p2000.u API. For high-level look
into python-module-pyvfs.

%package -n python3-module-%modname
Summary: Pure Python implementation of 9P protocol (Plan9)
License: MIT
Group: Development/Python
URL: https://github.com/svinota/py9p

%description -n python3-module-%modname
Protocol 9P is developed for Plan9 operating system from Bell Labs.
It is used for remote file access, and since files are key objects
in Plan9, 9P can be used also for composite file access, RPC etc.

This library provides low-level 9p2000.u API. For high-level look
into python-module-pyvfs.

%package -n fuse9p
Summary: Plan9 filesystem client for FUSE
License: MIT
Group: Development/Python
URL: https://github.com/svinota/py9p
Requires: %name = %version-%release

%description -n fuse9p
Protocol 9P is developed for Plan9 operating system from Bell Labs.
It is used for remote file access, and since files are key objects
in Plan9, 9P can be used also for composite file access, RPC etc.

This package contains FUSE client for the 9p protocol.

%package -n 9pfs
Summary: Plan9 filesystem server
License: MIT
Group: Development/Python
URL: https://github.com/svinota/py9p
Requires: %name = %version-%release

%description -n 9pfs
Protocol 9P is developed for Plan9 operating system from Bell Labs.
It is used for remote file access, and since files are key objects
in Plan9, 9P can be used also for composite file access, RPC etc.

This package contains simple 9p2000 file server.

%prep
%setup -n py9p-%{version}

rm -rf ../python3
cp -fR . ../python3

%build
make force-version
%python_build

pushd ../python3
make force-version
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc README* LICENSE
%{python_sitelibdir}/py9p*

%files -n python3-module-%modname
%doc README* LICENSE
%{python3_sitelibdir}/*

%files -n fuse9p
%doc LICENSE
%_bindir/fuse9p
%_man1dir/fuse9p.*

%files -n 9pfs
%doc LICENSE
%_bindir/9pfs
%_man1dir/9pfs.*

%changelog
* Fri Mar 23 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.9-alt1
- Version 1.0.9

* Sun Dec 16 2012 Peter V. Saveliev <peet@altlinux.org> 1.0.7-alt2
- fuse9p: read/write fixed
- fuse9p: rename support

* Sun Dec 16 2012 Peter V. Saveliev <peet@altlinux.org> 1.0.7-alt1
- pki auth fixed
- multiple fuse9p fixes
- 9pfs package

* Sat Dec 01 2012 Peter V. Saveliev <peet@altlinux.org> 1.0.6-alt2
- move mode2* and open2* routines to py9p module
- move FUSE client to the separated library
- reconnect feature fixed
- update documentation

* Thu Nov 29 2012 Peter V. Saveliev <peet@altlinux.org> 1.0.6-alt1
- fuse9p: stateful I/O
- fuse9p: symlink support
- fuse9p: do not use static fids
- py9p: Tcreate call fixed
- py9p: thread-safe I/O

* Sun Nov 04 2012 Peter V. Saveliev <peet@altlinux.org> 1.0.5-alt5
- fuse9p subpackage dependencies update

* Sat Nov 03 2012 Peter V. Saveliev <peet@altlinux.org> 1.0.5-alt4
- FUSE client: reconnect on errors

* Sat Nov 03 2012 Peter V. Saveliev <peet@altlinux.org> 1.0.5-alt3
- pki authentication fixed

* Sat Nov 03 2012 Peter V. Saveliev <peet@altlinux.org> 1.0.5-alt2
- FUSE client defaults to background mode

* Thu Nov 01 2012 Peter V. Saveliev <peet@altlinux.org> 1.0.5-alt1
- FUSE client added

* Fri Oct 26 2012 Peter V. Saveliev <peet@altlinux.org> 1.0.4-alt1
- support for arbitrary keys for PKI
- support sticky bit (Unix, 9P2000.u)

* Tue Oct 16 2012 Peter V. Saveliev <peet@altlinux.org> 1.0.2-alt1
- support AES-encrypted keys
- fixed authfs
 
* Fri Oct 12 2012 Peter V. Saveliev <peet@altlinux.org> 1.0.1-alt1
- Rebuild from new repo layout

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Wed Aug 24 2011 Peter V. Saveliev <peet@altlinux.org> 1.0-alt2
- file access mode for AF_UNIX socket

* Thu Aug 18 2011 Peter V. Saveliev <peet@altlinux.org> 1.0-alt1
- standalone git repo, version bump

* Thu Jul  7 2011 Peter V. Saveliev <peet@altlinux.org> 0.7.1-alt4
- iproute2 can add and delete addresses on interfaces
- more attributes parsed by rtnl
- wireless interfaces detection (ioctl) in rtnl
- get/set attributes in attr_msg class
- new utility function (make_map) that creates two-way mappings of set of attributes

* Wed Jun 17 2011 Peter V. Saveliev <peet@altlinux.org> 0.7.1-alt3
- cxkey utility added
- named parameters for py9p.Dir
- zeroconf.py fixed and tested

* Sun May 29 2011 Peter V. Saveliev <peet@altlinux.org> 0.7.1-alt2
- Sisyphus build fixed.

* Sun May 29 2011 Peter V. Saveliev <peet@altlinux.org> 0.7.1-alt1
- RPM prepared.

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt7.svn1392.1
- Rebuilt with python 2.6
