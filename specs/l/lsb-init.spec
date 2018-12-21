Name:         lsb-init
Summary:      ALT Linux implementation of LSB compliant init functions
Version:      4.0
Release:      alt5
License:      GPL
URL:          http://www.linuxbase.org
Source:       %name-%version.tar
Source101:    test-initscript.sh
Group:        System/Base
Packager:     Igor Vlasenko <viy@altlinux.ru>

# LSB 3.2 defined only for: IA32 IA64 PPC32 PPC64 S390 S390X AMD64
# http://www.linuxfoundation.org/en/Specifications
#Exclusivearch: %{ix86} x86_64
BuildArch: noarch

# Requires:     lsb-core
Patch: lsb-init-alt-log.patch

%description
The Linux Standard Base (http://www.linuxbase.org/) is a standard core
system that third-party applications written for Linux can depend
upon.

The package provides the ALT Linux implementation of LSB compliant
init functions for the Linux Standard Base %version core support package.

%prep
%setup
%patch -p1 -d lib/lsb
install -m 755 %SOURCE101 -t ./

%build

%install
mkdir -p %buildroot{/lib/lsb,%{_sysconfdir}/altlinux-lsb}
install -m 755 ./%{_sysconfdir}/altlinux-lsb/* %buildroot%{_sysconfdir}/altlinux-lsb/
install -m 644 ./lib/lsb/* %buildroot/lib/lsb

%files
%doc ./lib/lsb/copyright
%{_sysconfdir}/altlinux-lsb
/lib/lsb
%doc test-initscript.sh

%changelog
* Wed Oct 05 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0-alt5
- status_of_proc should not print DONE/FAILED.
- docs: test-initscript.sh (in a working system) added.

* Thu Sep 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0-alt4
- Do not remove log_daemon_msg
  (This doesn't break anything and helps Debian-oriented init-scripts,
  as all the other kept functions do.)
- The implementation of log_end_msg, log_action_end_msg improved
  so that it prints the ALT-style DONE/FAILED

* Fri Apr 16 2010 Andriy Stepanov <stanv@altlinux.ru> 4.0-alt3
- Fix build

* Fri Apr 16 2010 Andriy Stepanov <stanv@altlinux.ru> 4.0-alt2
- Do not remove log_begin_msg, log_end_msg

* Fri Apr 16 2010 Andriy Stepanov <stanv@altlinux.ru> 4.0-alt1
- Increase version.

* Fri Jul 03 2009 Igor Vlasenko <viy@altlinux.ru> 3.2-alt2
- replaced RH-based init-functions with debian-based.

* Mon Jun 29 2009 Igor Vlasenko <viy@altlinux.ru> 3.2-alt1
- first build

