Name: java-service
Version: 0.1
Release: alt2.1

Summary: Java service tools
License: GPL
Group: System/Servers
Packager: Eugene Prokopiev <enp@altlinux.ru>
BuildArch: noarch

Source: %name-%version.tar

Requires: apache-commons-daemon apache-commons-daemon-jsvc java

%description
Java service tools

%prep
%setup -c

%install
cp -a * %buildroot/

%files
%_sbindir/*
%_initdir/java-template
%_localstatedir/%name

%changelog
* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2.1
- NMU: corrected java deps

* Fri Oct 29 2010 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt2
- add requires and update service template

* Wed Apr 14 2010 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt1
- first build

