Name: perftest
Summary: IB Performance tests
Version: 4.4 
Release: alt1
License: %gpl2only
Group: Monitoring
Url: https://github.com/linux-rdma/perftest
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: librdmacm-devel
BuildRequires: libibumad-devel

%description
gen2 uverbs microbenchmarks.

%prep
%setup

%build
./autogen.sh
%configure
%make_build CFLAGS="%optflags -D_GNU_SOURCE"

%install
install -d -m 0755 %buildroot%_bindir
install -m 0755 ib_{read,send,write,atomic}_{bw,lat} %buildroot%_bindir/
install -m 0755 raw_ethernet_{bw,lat} %buildroot%_bindir/

%files
%doc README COPYING runme
%_bindir/*

%changelog
* Sun Nov 11 2018 Alexander Makeenkov <amakeenk@altlinux.org> 4.4-alt1
- New version

* Mon Sep 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.0-alt2
- Fixed build with gcc-6.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3.0-alt1.qa1
- NMU: rebuilt for debuginfo.

* Thu Dec 16 2010 Timur Aitov <timonbl4@altlinux.org> 1.3.0-alt1
- New version

* Thu Sep 02 2010 Andriy Stepanov <stanv@altlinux.ru> 1.2.3-alt2
- Rebuild with new libibumad

* Wed Aug 18 2010 Andriy Stepanov <stanv@altlinux.ru> 1.2.3-alt1
- OFED 1.5.1

* Tue Oct 28 2008 Led <led@altlinux.ru> 1.2-alt1
- initial build for ALTLinux

* Mon Jul 09 2007 - hvogel@suse.de
- Use correct version
* Wed Jul 04 2007 - hvogel@suse.de
- Add GPL COPYING file [#289509]
* Mon Jul 02 2007 - hvogel@suse.de
- Update to the OFED 1.2 version
* Fri Jun 22 2007 - hvogel@suse.de
- Initial Package, Version 1.1
