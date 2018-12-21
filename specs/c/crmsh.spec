%define gname haclient
%define uname hacluster



Name: crmsh
Summary: Pacemaker command line interface
Version: 3.0.3
Release: alt1
License: GPL-2.0+
Url: http://crmsh.github.io
Group: System/Configuration/Other
Source0: %name-%version.tar

BuildArch: noarch

Requires: pacemaker-cli
Requires: csync2 >= 2.0
Requires: %name-scripts = %version-%release
BuildRequires: asciidoc-a2x libpacemaker-devel time
#libcluster-glue-devel
BuildPreReq: python-devel python-module-setuptools

BuildRequires(pre): rpm-build-ubt

%description
The crm shell is a command-line interface for High-Availability
cluster management on GNU/Linux systems. It simplifies the
configuration, management and troubleshooting of Pacemaker-based
clusters, by providing a powerful and intuitive set of features.
crm shell, a Pacemaker command line interface.

%package test
Summary: Test package for crmsh
Group: System/Configuration/Other
Requires: %name = %version-%release

%description test
The crm shell is a command-line interface for High-Availability
cluster management on GNU/Linux systems. It simplifies the
configuration, management and troubleshooting of Pacemaker-based
clusters, by providing a powerful and intuitive set of features.
This package contains the regression test suite for crmsh.

%package scripts
Summary: Crm Shell Cluster Scripts
Group: System/Configuration/Other

%description scripts
Cluster scripts for crmsh. The cluster scripts can be run
directly from the crm command line, or used by user interfaces
like hawk to implement configuration wizards.

%package -n bash-completion-%name
Summary: Bash completion for %name
Group: Shells
Requires: bash-completion
Requires: %name = %version-%release

%description -n bash-completion-%name
Bash completion for %name.

%add_python_lib_path %_datadir/%name/utils

%prep
%setup

%build
%autoreconf
%configure \
	--localstatedir=%_var \
	--with-version=%version-%release \
	--docdir=%_defaultdocdir/%version-%release

%make_build VERSION="%version-%release" sysconfdir=%_sysconfdir localstatedir=%_var

%install
%makeinstall_std
install -Dm0644 contrib/bash_completion.sh %buildroot%_sysconfdir/bash_completion.d/crm.sh

mkdir -p %buildroot%_sbindir
mv %buildroot%_bindir/crm %buildroot%_sbindir/crm

%files
%_sbindir/crm
%python_sitelibdir/crmsh*

%_datadir/%name
%exclude %_datadir/%name/tests
%exclude %_datadir/%name/scripts

%dir %_sysconfdir/crm
%config(noreplace) %_sysconfdir/crm/*

%_man8dir/*
%_defaultdocdir/%version-%release
%dir %attr (770, %uname, %gname) %_var/cache/crm

%files scripts
%_datadir/%name/scripts

%files test
%_datadir/%name/tests

%files -n bash-completion-%name
%_sysconfdir/bash_completion.d/*

%changelog
* Tue Sep 04 2018 Anton Farygin <rider@altlinux.ru> 3.0.3-alt1
- 3.0.3

* Tue Apr 18 2017 Anton Farygin <rider@altlinux.ru> 3.0.0-alt1%ubt
- new version

* Mon Apr 17 2017 Anton Farygin <rider@altlinux.ru> 2.3.2-alt1%ubt
- new version
- fixed hostname resolution in crm init 

* Fri Jan 13 2017 Anton Farygin <rider@altlinux.ru> 2.3.1-alt2
- adapted for ALT

* Fri Sep 16 2016 Alexey Shabalin <shaba@altlinux.ru> 2.3.1-alt1
- 2.3.1
- add packages crmsh-scripts, crmsh-test, bash-completion-crmsh

* Fri Sep 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.git20140904
- Version 2.0

* Sat Oct 05 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.6-alt1
- New version

* Tue Aug 13 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.5-alt1
- Build for ALT
