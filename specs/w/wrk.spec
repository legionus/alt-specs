Summary: 	a HTTP benchmarking tool
Name: 		wrk
Version:	4.0.1
Release: 	alt1.1
Url: 		https://github.com/wg/wrk
Source: 	%name-%version.tar
Patch0:		wrk-3.1.1-alt1-install-fix.patch
Packager: 	Valentin Rosavitskiy <valintinr@altlinux.org>
License: 	Apache License
Group: 		Networking/WWW
ExclusiveArch: %ix86 x86_64

BuildRequires:	libssl-devel

%description
wrk is a modern HTTP benchmarking tool capable of generating significant
load when run on a single multi-core CPU. It combines a multithreaded
design with scalable event notification systems such as epoll and kqueue.

An optional LuaJIT script can perform HTTP request generation, response
processing, and custom reporting. Several example scripts are located in
scripts/


%prep
%setup
%patch0 -p1

%build
%make_build

%install
%makeinstall_std

%files
%_sbindir/wrk
%doc LICENSE NOTICE README

%changelog
* Wed Aug 29 2018 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt1.1
- NMU: Rebuild with new openssl 1.1.0.

* Tue Apr 28 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 4.0.1-alt1
- New version

* Thu Oct 16 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 3.1.1-alt1
- Initial build for ALT

